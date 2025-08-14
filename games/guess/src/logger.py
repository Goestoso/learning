import logging, shutil
from pathlib import Path

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def setup_logger():

    base_dir = Path(__file__).resolve().parent.parent
    log_dir = base_dir / "log"
    log_dir.mkdir(exist_ok=True)

    log_path = log_dir / "guess.log"
    
    # Evita duplicação de handlers
    if not logger.hasHandlers():
        # Handler para arquivo
        file_handler = logging.FileHandler(log_path)
        formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s: %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )

        # Adiciona os handlers
        logger.addHandler(file_handler)
        file_handler.setFormatter(formatter)
    
def log_error(message:str):
    logging.error(msg=message)

def close_logger():
    
    handlers = logger.handlers[:]

    for handler in handlers:
        handler.close()
        logger.removeHandler(handler)

    base_dir = Path(__file__).resolve().parent.parent
    log_dir = base_dir / "log"

    # Tenta remover com segurança
    if log_dir.exists() and log_dir.is_dir():
        try:
            shutil.rmtree(log_dir)
        except Exception as e:
            print(f"Error removing log directory: {e}")
