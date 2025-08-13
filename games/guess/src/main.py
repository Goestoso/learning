""""Arquivo Principal do jogo Guess"""
 
# importando bibliotecas
from src.gui import main_window, show_error
from src.utils import load_words

def main(): # funcao principal
    error = load_words() # valida se o arquivo foi carregado com sucesso
    if error:
        show_error(error)
        return
    main_window()

