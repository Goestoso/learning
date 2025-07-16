"Módulo de funções auxiliares do app Filter Tasks Planner"

import json, yaml, traceback, logging
import pandas as pd
from pathlib import Path

# Variáveis globais
config, json_path, excel_path, moved_path, new_path, log_path, tarefas_atuais, tarefas_antigas, option_new, option_moved, log_active, observe_schedule = [None for _ in range(12)]

logger = logging.getLogger("filter_tasks_planner")

def load_config(config_path: Path):
    global config
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

def set_configs():
    global json_path, excel_path, moved_path, new_path, log_active, log_path, option_new, option_moved, observe_schedule

    try:
        log_active = bool(config['log']['active'])
        json_path = Path(config['observe']['file'])
        excel_path = Path(config['data']['tasks_excel'])
        moved_path = Path(config['data']['tasks_moved'])
        new_path = Path(config['data']['tasks_new'])
        log_path = Path(config['log']['path'])
        option_new = bool(config['options']['tasks_new'])
        option_moved = bool(config['options']['tasks_moved'])
        observe_schedule = int(config['observe']['schedule'])
        
    except KeyError as e:
        print(f"Chave de configuração ausente: {e}")
    except ValueError as e:
        print(f"Valor inválido na configuração: {e}")
    except TypeError as e:
        print(f"Tipo inesperado na configuração: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        
def setup_log():
    if not log_active:
        return

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s: %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )

    try:
        # Verifica se o caminho é um diretório (sem extensão)
        if log_path.suffix == "":
            # Cria subdiretório 'log' e define o nome padrão do arquivo
            log_dir = log_path / 'log'
            log_dir.mkdir(parents=True, exist_ok=True)
            full_log_path = log_dir / 'FilterTasksPlanner.log'
        elif log_path.suffix == ".log":
            # Se for um caminho de arquivo, cria diretório pai se necessário
            log_path.parent.mkdir(parents=True, exist_ok=True)
            full_log_path = log_path
        else:
            raise ValueError(f"O caminho de log '{log_path}' deve ser um diretório ou um arquivo '.log'.")

        file_handler = logging.FileHandler(full_log_path, encoding='utf-8')

    except (OSError, ValueError) as e:
        fallback_path = Path("C:/Temp/FilterTasksPlanner")
        fallback_path.mkdir(parents=True, exist_ok=True)
        full_log_path = fallback_path / "filter_tasks_planner.log"
        file_handler = logging.FileHandler(full_log_path, encoding='utf-8')
        print(f"[AVISO] Não foi possível acessar o caminho de log em '{log_path}'. Usando fallback em '{full_log_path}'. Erro: {e}")

    # Aplica formatter e adiciona handler
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Log inicial
    logger.info("Logger configurado com sucesso.")

    if str(full_log_path) != str(log_path):
        logger.warning(f"Arquivo de log redirecionado para '{full_log_path}' pois '{log_path}' não pôde ser acessado.")


def verify_observe_schedule():
    global observe_schedule
    if observe_schedule < 60:
        logger.warning("O intervalo de tempo escolhido para o agendamento é muito baixo. Portanto o valor de observe schedule será alterado para o mínimo suportado de 60 segundos.")
        observe_schedule = 60
        
def initialize(config_path):
    load_config(config_path)
    set_configs()
    setup_log()
    verify_observe_schedule()
        
def load_tasksplanner_json():
    global tarefas_atuais, tarefas_antigas
    try:
        with open(json_path, 'r') as f:
            tarefas_json = json.load(f)
        tarefas_atuais = {t['id']: t['bucketId'] for t in tarefas_json['value']}

        df_antigo = pd.read_excel(excel_path)
        if not {'Identificação da tarefa', 'ID do Bucket'}.issubset(df_antigo.columns):
            raise ValueError("A planilha deve conter as colunas 'Identificação da tarefa' e 'ID do Bucket'.")

        duplicados = df_antigo['Identificação da tarefa'][df_antigo['Identificação da tarefa'].duplicated()]
        if not duplicados.empty:
            logger.warning(f"Foram encontradas {duplicados.nunique()} tarefas duplicadas na planilha. IDs: {duplicados.unique().tolist()}")
        
        tarefas_antigas = dict(zip(df_antigo['Identificação da tarefa'], df_antigo['ID do Bucket']))
        if log_active:
            logger.info(f"Conteúdo do arquivo {json_path} carregado com sucesso.")
    except ValueError as v:
        if log_active:
            logger.error(str(v))
        else:
            print(str(v))
    except Exception as e:
        if log_active:
            logger.exception("Erro inesperado ao carregar JSON e Excel.")
        else:
            print(str(e))

def create_changedbucketes_json():
    try:
        tarefas_movidas = [
            {'id': id_tarefa}
            for id_tarefa, bucket_atual in tarefas_atuais.items()
            if tarefas_antigas.get(id_tarefa) != bucket_atual
        ]

        with open(moved_path, 'w', encoding='utf-8') as f_out:
            json.dump(tarefas_movidas, f_out, ensure_ascii=False, indent=4)

        if log_active:
            if tarefas_movidas:
                logger.info(f"{len(tarefas_movidas)} tarefa(s) mudaram de bucket. Resultado salvo em {moved_path}.")
            else:
                logger.info("Nenhuma tarefa mudou de bucket.")
    except Exception:
        if log_active:
            logger.exception("Erro ao salvar tarefas movidas.")
        else:
            print(traceback.format_exc())

def create_tasksnew_json():
    try:
        tarefas_novas = [
            {'id': id_tarefa}
            for id_tarefa in tarefas_atuais
            if tarefas_antigas.get(id_tarefa) is None
        ]

        with open(new_path, 'w', encoding='utf-8') as f_out:
            json.dump(tarefas_novas, f_out, ensure_ascii=False, indent=4)

        if log_active:
            if tarefas_novas:
                logger.warning(f"{len(tarefas_novas)} tarefa(s) novas que não estão em {excel_path}. Resultado salvo em {new_path}.")
            else:
                logger.info("Nenhuma tarefa nova encontrada.")
    except Exception:
        if log_active:
            logger.exception("Erro ao salvar novas tarefas.")
        else:
            print(traceback.format_exc())
