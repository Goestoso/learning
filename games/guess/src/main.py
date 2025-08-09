""""Arquivo Principal do jogo Guess"""
 
#importando bibliotecas
from src.gui import main_window
from src.utils import load_words

def main(): #função principal do jogo
    load_words()
    main_window()

