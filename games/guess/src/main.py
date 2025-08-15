""""Arquivo Principal do jogo Guess"""
 
# importando bibliotecas
from src.gui import main_window, show_error
from src.utils import load_words, get_icon_path
from src.logger import setup_logger, log_error, close_logger

def main(): # funcao principal
    setup_logger()
    
    error = load_words() # valida se o arquivo foi carregado com sucesso
    if error:
        show_error(error)
        log_error(error.replace('\n', ' '))
        return
    
    icon_path, icon_error = get_icon_path() # valida se o icon ainda existe
    if icon_error:
        log_error(icon_error)
        return
    
    close_logger()

    main_window(icon_path)

