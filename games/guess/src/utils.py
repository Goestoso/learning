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

def get_icon_path():
    base_dir = Path(__file__).resolve().parent.parent
    icon_path = base_dir / 'assets' / 'lamp.ico'

    if not icon_path.exists():
        return None, f"Icon not found in: {icon_path}"
    
    return icon_path, None


def load_words(): # carrega as palavras do arquivo words.txt
    global words
    base_dir = Path(__file__).resolve().parent.parent
    file_path = base_dir / 'data' / 'words.txt'
    words = []

    try:
        with open(file_path, "r") as file:
            words = [line.strip() for line in file.readlines()]
    except Exception as error:
        return f"Error loading file: {file_path}\n\nDetails: {error}"

    return None  # Nenhum erro

def load_secret_word(): # carrega uma palavra secreta aleatória da lista words
    global secret_word, attempted_letters, attempted_words, attempts
    attempted_letters = set()
    attempted_words = set()
    attempts = 6
    secret_word = random.choice(words)
    
def load_guessed_word(): # carrega o valor inicial da palavra a ser advinhada
    global guessed_word
    guessed_word = ['_'] * len(secret_word)
    
def guessing(guess:str): # função para as partidas do jogo
    global guessed_word, attempted_letters, attempted_words, attempts, win, already_attempted, win, fail, good_letter, invalid, invalid_msg
    
    win, already_attempted, fail, good_letter, invalid = [False for _ in range(5)]
    
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
        invalid_msg = "Error: Value invalid. Please, enter a letter or a word!"

    else:
        invalid = True
        invalid_msg = "Please, input a letter or a valid word."       
        return