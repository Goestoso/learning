""""Arquivo Principal do jogo Guess"""
 
#importando bibliotecas
import random
import tkinter
import time

def play():
    welcome()
   
    print("\nLoading secret word...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1\n")
    time.sleep(1)

    words = load_words()
    secret_word = random.choice(words)
    #print(f'Palavra selecionada: {secret_word}\n')

    start_game(secret_word)

    print("\nWhat do you want to do? \n")

    close_or_again = '' 
    while True:
        close_or_again = input('Close game or start again?')
        if close_or_again == ("Again"):
            time.sleep(2)
            play()
            break
        elif close_or_again == ("Close"):
         print("\nThank you very much for playing")
         print("See you later")
         break
        
        else:
            print('Please, enter "Start" or "Close"\n ')

def load_words():
    words = []
    try:
        with open("words.txt", "r") as file:
            words = [line.strip() for line in file.readlines()]
    except Exception as error:
        print(f'Error: {error}')
        exit()
    
    return words

def start_game(secret_word):
    # Mostrar a palavra com underscores
    guessed_word = ['_'] * len(secret_word)
    print(f'The secret word: {" ".join(guessed_word)}')

    attempts = 6  # O jogador tem 6 tentativas
    while attempts > 0:
        guess = input("\nGuess a letter or the whole word: ").lower()

        # Verificar se o jogador adivinhou a palavra inteira
        if len(guess) == len(secret_word) and guess.isalpha():
            if guess == secret_word:
                print("\ncongratulations! You guess the secret word!")
                break
            else:
                print("incorrect guesses. Try again.")
                print(f"Do you still have {attempts} attempts.")
                attempts -= 1
        # Verificar se o jogador adivinhou uma letra
        elif len(guess) == 1 and guess.isalpha():
            if guess in secret_word:
                print(f'\nThe letter "{guess}" está correta!')
                for i in range(len(secret_word)):
                    if secret_word[i] == guess:
                        guessed_word[i] = guess
                if '_' not in guessed_word:
                    print("congratulations! You guess the secret word!")
                    break
            else:
                print(f'\nThe Letter "{guess}" do not is in word.')
                print(f"Do you still have {attempts} attempts.")
                attempts -= 1

        elif len(guess) >= 2:
            print("Input just one letter")
            #attempts -= 1

        elif not guess.isalpha():
            print("Error: Value invalid. Please, enter a letter!")

        else:
            print("Please, input a letter or a valid word.")

        print(f"\nThe word: {' '.join(guessed_word)}")

    if attempts == 0:
        print(f'You lose! The word was: "{secret_word}"')


def welcome():
    print("*************************************")
    print("***********Welcome to Guess**********")
    print("*************************************")
    
    print("\nWhat do you want to do? ") 
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

if(__name__ == "__main__"):
    play()