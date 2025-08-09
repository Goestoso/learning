"""Arquivo de Funções Auxiliares do jogo Guess"""

#importando bibliotecas
import random
from pathlib import Path

words: list[str] = list()
secret_word: str = ''
guessed_word: str = ''
attempted_letters : set = set() # conjunto para armazenar letras que já foram usadas
attempted_words: set = set() # para palavras já usadas
attempts: int = 6
win: bool = False
already_attempted: bool = False # flag para caso a palavra ou letra já ter sido testada
fail: bool = False # Flag para caso não ter acertado a tentativa
good_letter: bool = False # Flag para caso a letra estiver correta
invalid: bool = False # Flag para tentativas inválidas
invalid_msg: str = ""

def load_words(): #carrega as palavras do arquivo words na lista words
    global words
    base_dir = Path(__file__).resolve().parent.parent  # volta ao diretório raiz do projeto
    file_path = base_dir / 'data' / 'words.txt' #concatena com o diretório que contém o arquivo words
    load_words = []
    try:
        with open(file_path, "r") as file:
            load_words = [line.strip() for line in file.readlines()]
    except Exception as error:
        print(f'Error: {error}')
        exit()
    
    words = load_words

def load_secret_word():
    global secret_word
    secret_word = random.choice(words)
    
def load_guessed_word():
    global guessed_word
    guessed_word = ['_'] * len(secret_word)
    
def guessing(guess:str): #função para as partidas do jogo
    global guessed_word, attempted_letters, attempted_words, attempts, win, already_attempted, fail, good_letter, invalid, invalid_msg
    
    already_attempted, fail, good_letter, invalid = [False for _ in range(4)]

    #print(f'Palavra selecionada: {secret_word}\n')
    #print(f'The secret word: {" ".join(guessed_word)}')
    
    guess.lower()
    # Verificar se o jogador adivinhou a palavra inteira
    if len(guess) == len(secret_word) and guess.isalpha():
        if guess == secret_word: 
            win = True
            return
        elif guess in attempted_words:  
            already_attempted = True
            return
        else:
            attempted_words.add(guess)
            attempts -= 1
            fail = True
            return
    # Verificar se o jogador adivinhou uma letra
    elif len(guess) == 1 and guess.isalpha():
        if guess in attempted_letters:
            already_attempted = True
            return
        elif guess in secret_word:
            attempted_letters.add(guess)
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
            if '_' not in guessed_word:
                win = True
                return
            good_letter = True
            return 
        else:
            fail = True
            attempted_letters.add(guess)
            attempts -= 1
            return          

    elif len(guess) >= 2:
        invalid = True
        invalid_msg = f"Input just one letter or the whole word"
        return

    elif not guess.isalpha():
        invalid = True
        invalid_msg = "Error: Value invalid. Please, enter a letter!"

    else:
        invalid = True
        invalid_msg = "Please, input a letter or a valid word."       
        return
    

"""def main_menu(): #função de abertura do jogo
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
        global words, secret_word
        words = load_words()
        secret_word = random.choice(words)
        
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
        time.sleep(4)
        print("\n🎮 The game ends when:\n ")
        time.sleep(2)
        print("✅ You correctly guess the word 🎉")
        time.sleep(1.5)
        print("❌ You run out of tries and lose 😢")
        time.sleep(1.5)
        print("\n🔹 Good luck and have fun! 🚀\n")
        time.sleep(4)
        main_menu()
        print("🔹 If you guess wrong, you lose a try.")"""

"""def win_or_lose(win:bool):
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

def end_game():
    global words, secret_word
    close_or_again = '' 
    while True:
        print("\nWhat do you want to do? \n")
        close_or_again = input('Options: \n\n- Try again (type Again)\n\n- Go back to beginning (type Back)\n\nChoose an option: ').upper()
        if close_or_again == ("AGAIN"):
            time.sleep(2)
            secret_word = random.choice(words)
            guessing()
        elif close_or_again == ("BACK"):
            print("\nReturning to the main menu...\n")
            time.sleep(1)
            main_menu()
        else:
            print('Please, enter "Again" or "Back"\n ')"""