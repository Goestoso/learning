""""Arquivo Principal do jogo Guess"""
 
#importando bibliotecas
import random
import tkinter

def play():
    welcome()

    print("Jogando...")



def welcome():
    print("*************************************")
    print("***********Welcome to Guess**********")
    print("*************************************")
    
    print("\nList of options:") 
    print("\nOption 1: Start new game")
    print("Option 2: Quit")
    print("Option 3: Help")
    option_invalid = True
    option = 0
    while option_invalid or (option < 1 or option > 3):
        try:
            option = int(input("\nChoose an option: "))
            option_invalid = False
        except:
            print("Por favor, insira um valor válido de 1 a 3")
        if option == 1:
            return

        elif option == 2:
            print("Até a próxima!")
            exit()

        elif option == 3: 
            print("Para jogar, jogue!")

        else:
            print("Please, choose a value a between 1 and 3")
            
    print(f"Option selected: {option}")

if(__name__ == "__main__"):
    play()


