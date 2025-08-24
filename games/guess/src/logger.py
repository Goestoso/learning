import logging, shutil, sys
from pathlib import Path

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def setup_logger():
    # Detecta se está rodando como executável
    if getattr(sys, 'frozen', False):
        base_dir = Path(sys.executable).parent
    else:
        base_dir = Path(__file__).resolve().parent.parent

    log_dir = base_dir / "log"
    log_dir.mkdir(exist_ok=True)

    log_path = log_dir / "guess.log"

    # Evita duplicação de handlers
    if not logger.hasHandlers():
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s: %(message)s',
            datefmt='%d/%m/%Y %H:%M:%S'
        )
        # Adiciona os handlers
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    
def log_error(message:str):
    logging.error(msg=message)

def close_logger():
    handlers = logger.handlers[:]

    for handler in handlers:
        handler.close()
        logger.removeHandler(handler)

    # Detecta se está rodando como executável
    if getattr(sys, 'frozen', False):
        base_dir = Path(sys.executable).parent
    else:
        base_dir = Path(__file__).resolve().parent.parent

    log_dir = base_dir / "log"

    # Tenta remover com segurança
    if log_dir.exists() and log_dir.is_dir():
        try:
            shutil.rmtree(log_dir)
        except Exception as e:
            print(f"Error removing log directory: {e}")

