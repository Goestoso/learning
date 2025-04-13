""""Arquivo Principal do jogo Guess"""
 
#importando bibliotecas
import random
import tkinter
import time
from pathlib import Path

def play(): #função principal do jogo
    welcome()
    load_secret_word()

    words = load_words()
    secret_word = random.choice(words)
    #print(f'Palavra selecionada: {secret_word}\n')

    start_game(secret_word)

    close_or_again = '' 
    while True:
        print("\nWhat do you want to do? \n")
        close_or_again = input('Options: \n\n- Try again (type Again)\n\n- Go back to beginning (type Back)\n\nChoose an option: ').upper()
        if close_or_again == ("AGAIN"):
            load_secret_word()
            time.sleep(2)
            secret_word = random.choice(words)
            start_game(secret_word)
        elif close_or_again == ("BACK"):
            print("\nReturning to the main menu...\n")
            time.sleep(1)
            play()
        else:
            print('Please, enter "Again" or "Back"\n ')

def load_words(): #carrega as palavras do arquivo words na lista words
    base_dir = Path(__file__).resolve().parent.parent  # volta ao diretório raiz do projeto
    file_path = base_dir / 'data' / 'words.txt' #concatena com o diretório que contém o arquivo words
    words = []
    try:
        with open(file_path, "r") as file:
            words = [line.strip() for line in file.readlines()]
    except Exception as error:
        print(f'Error: {error}')
        exit()
    
    return words

def load_secret_word(): #função que mostra que uma nova palavra secreta está sendo carregada
    print("\nLoading secret word...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1\n")
    time.sleep(1)

def start_game(secret_word): #função para as partidas do jogo
    # Mostrar a palavra com underscores
    attempted_letters = set() #conjunto para armazenar letras que já foram usadas
    attempted_words = set() #para palavras já usadas
    guessed_word = ['_'] * len(secret_word)
    print(f'The secret word: {" ".join(guessed_word)}')
    attempts = 6  # O jogador tem 6 tentativas
    while attempts > 0:
        guess = input("\nGuess a letter or the whole word: ").lower()
        # Verificar se o jogador adivinhou a palavra inteira
        if len(guess) == len(secret_word) and guess.isalpha():
            if guess == secret_word:
                end_match(True)
                break
            elif guess in attempted_words:
                print(f'\nThe word "{guess}" has already been tried, try another guess!')
            else:
                attempted_words.add(guess)
                print("Incorrect guess. Try again.")
                print(f"Do you still have {attempts} attempts.")
                attempts -= 1
        # Verificar se o jogador adivinhou uma letra
        elif len(guess) == 1 and guess.isalpha():
            if guess in attempted_letters:
                print(f'\nThe letter "{guess}" has already been tried, try another guess!')
            elif guess in secret_word:
                print(f'\nThe letter "{guess}" is correct!')
                attempted_letters.add(guess)
                for i in range(len(secret_word)):
                    if secret_word[i] == guess:
                        guessed_word[i] = guess
                if '_' not in guessed_word:
                    end_match(True)
                    break
            else:
                attempted_letters.add(guess)
                print(f'\nThe letter "{guess}" is not in th secret word.')
                print(f"\nDo you still have {attempts} attempts.")
                attempts -= 1

        elif len(guess) >= 2:
            print("Input just one letter or the whole word")
            #attempts -= 1

        elif not guess.isalpha():
            print("Error: Value invalid. Please, enter a letter!")

        else:
            print("Please, input a letter or a valid word.")

        print(f"\nThe word: {' '.join(guessed_word)}")

    if attempts == 0:
        print(f'\nYou lose! The word was: "{secret_word}"')
        end_match(False)

def welcome(): #função de abertura do jogo
    print("*************************************")
    print("***********Welcome to Guess**********")
    print("*************************************")
    
    print("\nWhat do you want to do?") 
    print("\nOption 1: Start new game")
    print("Option 2: Quit")
    print("Option 3: Help")


    option_invalid = True
    option = 0

    while option_invalid:
        try:
            option = int(input("\nChoose an option: "))
            if option < 1 or option > 3:    
                print("Please, choose avalue between 1 and 3") 
            else:
                option_invalid = False
        except ValueError:
            print("Invalid input! Please, enter a number between 1 and 3.")
            
    if option == 1:
            return
    elif option == 2:
            print("See you later!")
            exit()

    elif option == 3: 
            print("\n📜 Instructions for Guess Game 📜\n")
            time.sleep(1)
            print("🔹 The goal is to guess the secret word chosen randomly.")
            time.sleep(1.5)
            print("🔹 The word will be represented by underscores (_ _ _).")
            time.sleep(1.5)
            print("🔹 You can guess one letter at a time or try to guess the full word.")
            time.sleep(1.5)
            print("🔹 If the letter is in the word, it will be revealed in the correct positions.")
            time.sleep(1.5)
            print("🔹 If you guess wrong, you lose a try.")
            time.sleep(4)
            print("\n🎮 The game ends when:\n ")
            time.sleep(2)
            print("✅ You correctly guess the word 🎉")
            time.sleep(1.5)
            print("❌ You run out of tries and lose 😢")
            time.sleep(1.5)
            print("\n🔹 Good luck and have fun! 🚀\n")
            time.sleep(4)
            welcome()

def end_match(win:bool):
    if win:
        print("\nCongratulations! You guess the secret word!\n")
        print("      '._==_==_=_.'     ")
        print("       ___________      ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("    _______________         ")
        print("   /               \\       ")
        print("  /                 \\     ")
        print("//                   \\/\\  ")
        print("\\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \\__      XXX      __/     ")
        print("   |\\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \\_             _/       ")
        print("     \\_         _/         ")
        print("       \\_______/           ")

if(__name__ == "__main__"): #contexto de execução do programa
    play()