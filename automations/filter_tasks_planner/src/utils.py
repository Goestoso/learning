"Funções auxiliares do app Filter Tasks Planner"

import json, time, hashlib, yaml
import pandas as pd
from pathlib import Path

config, json_path, excel_path, moved_path, new_path, log_active, log_mode, log_path, tarefas_atuais, tarefas_antigas, option_new, option_moved = [None for _ in range(12)]

def load_config(config_path:Path):
    global config
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
        
def set_configs():
    global json_path, excel_path, moved_path, new_path, log_active, log_mode, log_path, option_new, option_moved
    # Acessa os caminhos do YAML
    json_path = Path(config['observe']['file'])
    excel_path = Path(config['data']['tasks_excel'])
    moved_path = Path(config['data']['tasks_moved'])
    new_path = Path(config['data']['tasks_new'])
    log_active = config['log']['active']
    log_mode = config['log']['mode']
    log_path = Path(config['log']['path'])
    option_new = config['options']['tasks_new']
    option_moved = config['options']['tasks_moved']
    
def load_tasksplanner_json():
    global tarefas_atuais, tarefas_antigas
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
    
def create_changedbucketes_json():
    # Compara os buckets
    tarefas_movidas = []
    for id_tarefa, bucket_atual in tarefas_atuais.items():
        bucket_anterior = tarefas_antigas.get(id_tarefa)
        if bucket_anterior != bucket_atual:
            tarefas_movidas.append({'id': id_tarefa})
    # Salva o resultado de buckets movidos no JSON
    with open(moved_path, 'w', encoding='utf-8') as f_out:
        json.dump(tarefas_movidas, f_out, ensure_ascii=False, indent=4)
    # Exibe tarefas movidas
    if tarefas_movidas:
        print(f"{len(tarefas_movidas)} tarefa(s) mudaram de bucket. Resultado salvo em {moved_path}.")
    else:
        print("Nenhuma tarefa mudou de bucket.")

def create_tasksnew_json():
    # Detecta novas tarefas
    tarefas_novas = []

    for id_tarefa, _ in tarefas_atuais.items():
        bucket_anterior = tarefas_antigas.get(id_tarefa)
        if bucket_anterior is None:
            tarefas_novas.append({'id': id_tarefa})
        
    # Salva o resultado de tarefas novas no JSON
    with open(new_path, 'w', encoding='utf-8') as f_out:
        json.dump(tarefas_novas, f_out, ensure_ascii=False, indent=4)
        
    if tarefas_novas:
        print(f"Você tem {len(tarefas_novas)} tarefa(s) novas que não estão em {excel_path}. Resultado salvo em {new_path}.")
    else:
        print("Nenhuma tarefa nova.")