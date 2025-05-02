""""Arquivo Principal do jogo Guess"""
 
#importando bibliotecas
from test_utils import main_menu, start_game, end_game

def main(): #função principal do jogo
    main_menu()
    start_game()
    end_game()
    
if(__name__ == "__main__"): #contexto de execução do programa
    main()

