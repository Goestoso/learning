"Módulo de funções auxiliares do app Filter Tasks Planner"

import json, yaml, logging, sys, shutil
from logging.handlers import MemoryHandler
import pandas as pd
from pathlib import Path

# Variáveis globais
config = None
json_path = None 
excel_path = None 
moved_path = None 
new_path = None
log_path = None
tarefas_atuais = None 
tarefas_antigas = None 
option_new = None
option_moved = None
log_active = None
observe_schedule = None
logger = logging.getLogger("filter_tasks_planner")
memory_log = None  # salvar referência para flush futuro

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
        print("[ERRO] Configuração incompleta. Verifique se todas as chaves estão presentes.")
        if log_active:
            logger.error(f"Chave de configuração ausente: {e}")

    except ValueError as e:
        print("[ERRO] Valor inválido encontrado na configuração.")
        if log_active:
            logger.error(f"Valor inválido na configuração: {e}")

    except TypeError as e:
        print("[ERRO] Tipo de dado incorreto na configuração.")
        if log_active:
            logger.error(f"Tipo inesperado na configuração: {e}")

    except Exception as e:
        print("[ERRO] Falha ao carregar as configurações.")
        if log_active:
            logger.exception(f"Erro inesperado ao carregar configurações: {e}")
        
def setup_log_early():
    """Cria um logger temporário antes do carregamento das configurações."""
    global memory_log
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s: %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )

    fallback_path = Path.cwd() / "temp"
    fallback_path.mkdir(parents=True, exist_ok=True)
    early_log_file = fallback_path / "FilterTasksPlanner_init.log"

    file_handler = logging.FileHandler(early_log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)

    memory_log = MemoryHandler(capacity=1000, flushLevel=logging.ERROR, target=file_handler)
    logger.addHandler(memory_log)
    
def cleanup_log_early():
    fallback_path = Path.cwd() / "temp"
    if fallback_path.exists() and fallback_path.is_dir():
        try:
            shutil.rmtree(fallback_path)
            if log_active:
                logger.info(f"Diretório de log temporário '{fallback_path}' removido com sucesso.")
        except Exception as e:
            if log_active:
                logger.warning(f"Falha ao remover diretório de log temporário '{fallback_path}': {e}")
            print(f"\n[AVISO] Falha ao remover diretório de log temporário. Erro: {e}\n")
        
def setup_log_after():
    """Cria um logger fixo (se log for ativado) após o carregamento das configurações."""
    if not log_active:
        return

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s: %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )

    fallback_used = False
    fallback_path = Path.cwd() / "log"
    fallback_path.mkdir(parents=True, exist_ok=True)
    full_log_path = fallback_path / "FilterTasksPlanner.log"

    try:
        if log_path.suffix == ".log":
            # É um arquivo .log
            log_path.parent.mkdir(parents=True, exist_ok=True)
            full_log_path = log_path

        elif log_path.suffix == "":
            # É um diretório
            full_log_path = log_path / "log" / "FilterTasksPlanner.log"
            full_log_path.parent.mkdir(parents=True, exist_ok=True)

        else:
            raise ValueError(f"O caminho de log '{log_path}' deve ser um diretório ou um arquivo '.log'.")

        file_handler = logging.FileHandler(full_log_path, encoding='utf-8')

    except (OSError, ValueError) as e:
        fallback_used = True
        full_log_path = fallback_path / "FilterTasksPlanner.log"
        file_handler = logging.FileHandler(full_log_path, encoding='utf-8')
        print(f"\n[AVISO] Não foi possível acessar o caminho de log em '{log_path}'. Usando fallback em '{full_log_path}'. Erro: {e}\n")

    # Substitui os handlers anteriores (inclusive o early logger)
    for handler in logger.handlers[:]:
        handler.close()          # Fecha o handler (libera o arquivo)
        logger.removeHandler(handler)  # Remove o handler do logger 


    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    if fallback_used:
        logger.warning(f"Arquivo de log redirecionado para '{full_log_path}' pois '{log_path}' não pôde ser acessado.")
    else:
        logger.info(f"Logger configurado com sucesso em '{full_log_path}'.")


def verify_observe_schedule():
    global observe_schedule
    if observe_schedule < 60:
        logger.warning("O intervalo de tempo escolhido para o agendamento é muito baixo. Portanto o valor de observe schedule será alterado para o mínimo suportado de 60 segundos.")
        observe_schedule = 60
        
def initialize(config_path):
    setup_log_early()

    try:
        load_config(config_path)
        set_configs()
        setup_log_after()  # Reconfigura destino do log
        cleanup_log_early()
        verify_observe_schedule()

    except Exception as e:
        logger.exception(f"Erro crítico durante a inicialização: {e}")
        if memory_log:
            memory_log.flush()
            sys.exit(1)  # termina o programa com código 1

def load_tasksplanner_json():
    global tarefas_atuais, tarefas_antigas
    try:
        # Leitura do JSON
        with open(json_path, 'r', encoding='utf-8') as f:
            tarefas_json = json.load(f)
        tarefas_atuais = {t['id']: t['bucketId'] for t in tarefas_json['value']}

        # Leitura do Excel
        df_antigo = pd.read_excel(excel_path)

        # Validação de colunas
        colunas_esperadas = {'Identificação da tarefa', 'ID do Bucket'}
        if not colunas_esperadas.issubset(df_antigo.columns):
            raise ValueError(f"A planilha deve conter as colunas {colunas_esperadas}.")

        # Verificação de duplicadas
        duplicados = df_antigo['Identificação da tarefa'][df_antigo['Identificação da tarefa'].duplicated()]
        if not duplicados.empty:
            logger.warning(f"Foram encontradas {duplicados.nunique()} tarefas duplicadas na planilha. IDs: {duplicados.unique().tolist()}")

        # Conversão para dicionário
        tarefas_antigas = dict(zip(df_antigo['Identificação da tarefa'], df_antigo['ID do Bucket']))

        if log_active:
            logger.info(f"Conteúdo dos arquivos '{json_path}' e '{excel_path}' carregados com sucesso.")

    except FileNotFoundError as fnf:
        msg = f"Arquivo não encontrado: {fnf.filename}"
        logger.error(msg) if log_active else print(f"[ERRO] {msg}")

    except PermissionError as p:
        msg = f"Permissão negada ao acessar o arquivo: {p.filename}"
        logger.error(msg) if log_active else print(f"[ERRO] {msg}")

    except json.JSONDecodeError as jde:
        msg = f"Erro ao decodificar JSON: {jde.msg} (linha {jde.lineno}, coluna {jde.colno})"
        logger.error(msg) if log_active else print(f"[ERRO] {msg}")

    except ValueError as v:
        # Colunas ausentes ou outros valores inválidos
        msg = f"Erro nos dados da planilha: {str(v)}"
        logger.error(msg) if log_active else print(f"[ERRO] {msg}")

    except Exception as e:
        msg = f"Erro inesperado ao carregar JSON e planilha: {str(e)}"
        logger.exception(msg) if log_active else print(f"[ERRO] {msg}")


def create_changedbucketes_json():
    try:
        tarefas_movidas = [
            {'id': id_tarefa}
            for id_tarefa, bucket_atual in tarefas_atuais.items()
            if tarefas_antigas.get(id_tarefa) != bucket_atual
        ]
    except Exception as e:
        msg = f"Erro ao comparar buckets das tarefas: {str(e)}"
        logger.error(msg) if log_active else print(f"\n[ERRO] {msg}\n")
        return

    try:
        with open(moved_path, 'w', encoding='utf-8') as f_out:
            json.dump(tarefas_movidas, f_out, ensure_ascii=False, indent=4)

        if log_active:
            if tarefas_movidas:
                logger.warning(f"{len(tarefas_movidas)} tarefa(s) mudaram de bucket. Resultado salvo em {moved_path}.")
            else:
                logger.info("Nenhuma tarefa mudou de bucket.")

    except PermissionError as p:
        msg = f"Permissão negada ao escrever em {moved_path}."
        logger.error(msg) if log_active else print(f"\n[ERRO] {msg}\n")

    except OSError as o:
        msg = f"Erro de sistema ao salvar tarefas movidas: {str(o)}"
        logger.error(msg) if log_active else print(f"\n[ERRO] {msg}\n")

    except Exception as e:
        msg = f"Erro inesperado ao salvar tarefas movidas: {str(e)}"
        logger.exception(msg) if log_active else print(f"\n[ERRO] {msg}\n")

def create_tasksnew_json():
    try:
        tarefas_novas = [
            {'id': id_tarefa}
            for id_tarefa in tarefas_atuais
            if tarefas_antigas.get(id_tarefa) is None
        ]
    except Exception as e:
        msg = f"Erro ao identificar novas tarefas: {str(e)}"
        logger.error(msg) if log_active else print(f"\n[ERRO] {msg}\n")
        return

    try:
        with open(new_path, 'w', encoding='utf-8') as f_out:
            json.dump(tarefas_novas, f_out, ensure_ascii=False, indent=4)

        if log_active:
            if tarefas_novas:
                logger.warning(f"{len(tarefas_novas)} tarefa(s) novas que não estão em {excel_path}. Resultado salvo em {new_path}.")
            else:
                logger.info("Nenhuma tarefa nova encontrada.")

    except PermissionError as p:
        msg = f"Permissão negada ao escrever em {new_path}."
        logger.error(msg) if log_active else print(f"\n[ERRO] {msg}\n")

    except OSError as o:
        msg = f"Erro de sistema ao salvar tarefas novas: {str(o)}"
        logger.error(msg) if log_active else print(f"\n[ERRO] {msg}\n")

    except Exception as e:
        msg = f"Erro inesperado ao salvar tarefas novas: {str(e)}"
        logger.exception(msg) if log_active else print(f"\n[ERRO] {msg}\n")