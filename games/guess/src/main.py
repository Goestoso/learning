""""Arquivo Principal do jogo Guess"""
 
# importando bibliotecas
from src.gui import main_window, show_error
from src.utils import load_words, get_icon_path
from src.logger import setup_logger, log_error, close_logger

def main(): # funcao principal
    setup_logger()
    
    words_error = load_words() # valida se o arquivo foi carregado com sucesso
    icon_path, icon_error = get_icon_path() # valida se o icon ainda existe
    
    if words_error and icon_error:
        log_error(icon_error)
        log_error(words_error.replace('\n', ' '))
        return
    
    if icon_error:
        log_error(icon_error)
        return
    
    if words_error:
        show_error(words_error)
        log_error(words_error.replace('\n', ' '))
        return
    
    close_logger()

    main_window(icon_path)

