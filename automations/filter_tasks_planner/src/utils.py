import json
import pandas as pd
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# Classe para monitorar eventos de arquivos
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('plannertasks.json'):  # Verifica se o arquivo modificado é o plannertasks.json
            print(f"Arquivo modificado: {event.src_path}")
            create_file_change_buckets()  # Chama a função principal quando o arquivo for modificado

    def on_created(self, event):
        if event.src_path.endswith('plannertasks.json'):  # Verifica se o arquivo criado é o plannertasks.json
            print(f"Arquivo criado: {event.src_path}")
            create_file_change_buckets()  # Chama a função principal quando o arquivo for criado


# Função para iniciar o watchdog
def watch_file():
    base_dir = Path(__file__).resolve().parent.parent
    path_to_watch = base_dir / 'data'  # Diretório onde o arquivo plannertasks.json está localizado

    event_handler = MyHandler()  # Define o que fazer quando houver uma modificação/criação
    observer = Observer()  # Cria um observador
    observer.schedule(event_handler, path_to_watch, recursive=False)  # Inicia a observação do diretório

    observer.start()  # Inicia o observador

    try:
        while True:
            time.sleep(1)  # Espera enquanto observa as mudanças
    except KeyboardInterrupt:
        observer.stop()  # Para o observador quando o script é interrompido

    observer.join()

def create_file_change_buckets():
    base_dir = Path(__file__).resolve().parent.parent
    json_path = base_dir / 'data' / 'plannertasks.json'
    excel_path = base_dir / 'data' / 'Tarefas Teste.xlsx'
    output_path = base_dir / 'data' / 'change_buckets.json'

    # Carrega tarefas do JSON atual
    with open(json_path, 'r') as f:
        tarefas_json = json.load(f)
    tarefas_atuais = {t['id']: t['bucketId'] for t in tarefas_json['value']}

    # Carrega a planilha anterior
    df_antigo = pd.read_excel(excel_path)

    # Garante que tem as colunas esperadas
    if not {'Identificação da tarefa', 'ID do Bucket'}.issubset(df_antigo.columns):
        raise ValueError("A planilha deve conter as colunas 'Identificação da tarefa' e 'ID do Bucket'.")

    # Cria um dicionário com o histórico anterior
    tarefas_antigas = dict(zip(df_antigo['Identificação da tarefa'], df_antigo['ID do Bucket']))

    # Compara os buckets
    tarefas_movidas = []
    for id_tarefa, bucket_atual in tarefas_atuais.items():
        bucket_anterior = tarefas_antigas.get(id_tarefa)
        if bucket_anterior and bucket_anterior != bucket_atual:
            tarefas_movidas.append({
                'id': id_tarefa,
            })

    # Salva o resultado no JSON
    with open(output_path, 'w', encoding='utf-8') as f_out:
        json.dump(tarefas_movidas, f_out, ensure_ascii=False, indent=4)

    # Exibe tarefas movidas
    if tarefas_movidas:
        print(f"{len(tarefas_movidas)} tarefa(s) mudaram de bucket. Resultado salvo em {output_path.name}.")
    else:
        print("Nenhuma tarefa mudou de bucket.")