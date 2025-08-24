#importando bibliotecas
from  tkinter import Tk, Toplevel, Frame, Label, Button, Entry, messagebox, StringVar
from src import utils
import os

#variáveis globais
largura_janela = 400
altura_janela = 150
root = Tk()
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
posicaoX = (largura_tela - largura_janela) // 2
posicaoY = (altura_tela - altura_janela) // 2

# Caminho relativo do arquivo atual (gui.py)
base_path = os.path.dirname(__file__)

# Caminho completo até o ícone
icon_path = os.path.join(base_path, "..", "assets", "lamp.ico")

# Normaliza o caminho para o sistema operacional
icon_path = os.path.normpath(icon_path)

def show_error(message):
    posicaoX = (largura_tela - largura_janela) // 2
    posicaoY = (altura_tela - altura_janela) // 2
    root.resizable(False, False)
    root.geometry(f"{largura_janela}x{altura_janela}+{posicaoX}+{posicaoY}")
    root.iconbitmap(icon_path)
    root.withdraw()
    messagebox.showerror("❌ Error", message)
    root.destroy()

def main_window(icon_path):
    root.title("Artificial Guess")
    posicaoX = (largura_tela - largura_janela) // 2
    posicaoY = (altura_tela - altura_janela) // 2
    root.resizable(False, False)
    root.geometry(f"{largura_janela}x{altura_janela}+{posicaoX}+{posicaoY}")
    root.iconbitmap(icon_path)
    label = show_main_message()
    root.after(5000, lambda l=label, msg="🤖 Created by Artificial",f=("Times", 20): change_main_message(l, msg, f))
    root.after(8000, clear_root_window)
    root.after(8000, menu_options)
    root.mainloop()
    
def show_main_message(msg:str="🎮 Welcome to Guess"):
    frame = Frame(root)
    frame.pack(expand=True, fill="both")
    label = Label(frame, text=msg, font=("Arial", 20))
    label.pack(expand=True)
    return label
    
def menu_options():
    frame_top = Frame(root)
    frame_top.pack()
    label = Label(frame_top, text="🔢 Choose an option:", font=("Arial", 16, "bold"))
    label.pack(anchor="center")
    frame_center = Frame(root)
    frame_center.pack(expand=True, fill="both")
    button_start = Button(frame_center, text="▶ Start", command= difficulty_options, cursor="hand2")
    button_start.pack(pady=5, padx=80, fill="x")
    button_help = Button(frame_center, text="❓ Help", command= lambda: messagebox.showinfo("📜 Instructions for Guess Game 📜", "🔹 The goal is to guess the secret word chosen randomly.\n🔹 The word will be represented by underscores (_ _ _).\n🔹 You can guess one letter at a time or try to guess the full word.\n🔹 If the letter is in the word, it will be revealed in the correct positions.\n🕹️ The game ends when:\n        ✅ You correctly guess the word 🎉\n        ❌ You run out of tries and lose 😢\n🔹 Good luck and have fun! 🚀\n🔹 If you guess wrong, you lose a try. 📉\n 🔹 When you start a match you can choose the difficulty (hard, medium or easy) to define the number of attempts. ⚖️"), cursor="hand2")
    button_help.pack(pady=5, padx=80, fill="x")
    button_exit = Button(frame_center, text="↩ Exit", command= exit_game, cursor="hand2")
    button_exit.pack(pady=5, padx=80, fill="x")

def change_main_message(label:Label, msg:str, f:tuple[str,str]):
    label.config(text=msg,font=f)
    
def clear_root_window():
    for widget in root.winfo_children():
        widget.destroy()
        
def exit_game():
    clear_root_window()
    show_main_message("👋 See you later!")
    root.after(4000, root.destroy)
    
def difficulty_options():
    clear_root_window()
    root.withdraw()
    options = Toplevel(root)
    options.title("🧠 Difficulty options")
    options.resizable(False, False)
    options.geometry(f"350x200+{posicaoX}+{posicaoY}")
    options.iconbitmap(icon_path)

    label = Label(options, text="Choose the difficulty:", font=("Arial", 14, "bold"))
    label.pack(pady=10)

    def change_difficulty(level, attempts):
        utils.level = level
        utils.attempts = attempts
        options.destroy()  # Remove a janela após escolha
        root.deiconify()
        loading_secret_word()

    Button(options, text="😄 Easy (12 attempts)", font=("Arial", 12), width=25,
           command=lambda: change_difficulty("Easy", 12), cursor="hand2").pack(pady=5)

    Button(options, text="😐 Medium (8 attempts)", font=("Arial", 12), width=25,
           command=lambda: change_difficulty("Medium", 8), cursor="hand2").pack(pady=5)

    Button(options, text="😈 Hard (4 attempts)", font=("Arial", 12), width=25,
           command=lambda: change_difficulty("Hard", 4), cursor="hand2").pack(pady=5)
    
    options.protocol("WM_DELETE_WINDOW", lambda: go_back_menu_options(options))
    
def go_back_menu_options(window:Toplevel):
    clear_root_window()
    window.destroy()
    root.deiconify()
    menu_options()
    
    
def loading_secret_word(): # função que mostra que uma nova palavra secreta está sendo carregada
    clear_root_window()
    utils.load_secret_word()
    label = show_main_message(msg="⌛ Loading secret word...")
    root.after(4000, lambda l=label, msg="🧍 Attention...",f=("Arial", 20): change_main_message(l, msg, f))
    root.after(8000, lambda l=label, msg="🚶 Get ready...",f=("Arial", 20): change_main_message(l, msg, f))
    root.after(12000, lambda l=label, msg="🏃 Go!",f=("Arial", 20): change_main_message(l, msg, f))
    root.after(16000, start_game)
    
def start_game():
    
    def guess_verify(event=None):  # Aceita evento opcional
        entry.unbind("<Return>")  # Evita múltiplos disparos
        verify_button.config(state="disabled")
        
        utils.guessing(guess=input_guess.get())
        
        if utils.attempts == 0:
            root.withdraw()
            show_defeat_popup()
        elif utils.win:
            root.withdraw()
            show_victory_popup()
        elif utils.invalid:
            messagebox.showerror(title="🚨 Oops!", message=utils.invalid_msg)
        elif utils.good_letter:
            messagebox.showinfo(title="✅ Very good!", message=f'\nThe letter "{input_guess.get()}" is correct!')
            update_secret_frame()
        elif utils.already_attempted:
            messagebox.showinfo(
                title="👁️ Pay attention!",
                message=f'\nThe word "{input_guess.get()}" has already been tried, try another guess!' if len(input_guess.get()) >= 2 else f'\nThe letter "{input_guess.get()}" has already been tried, try another guess!'
            )
        elif utils.fail:
            messagebox.showinfo(title="💪 Nice try!", message=f"Incorrect guess. Try again.\nYou still have {utils.attempts} attempts.")
        
        verify_button.config(state="normal")
        entry.bind("<Return>", guess_verify)  # Reativa o Enter

    def update_secret_frame():
        word = ' '.join(utils.guessed_word)
        font_size = 14 if len(word) < 20 else 12 if len(word) < 30 else 10
        label.config(text=f"🔡 The secret word: {word}", font=("Arial", font_size, "bold"))
        
    def show_victory_popup():
        trophy = rf"""
        Congratulations! 

    You guessed the secret word!

          '._==_==_=_.'     
           ___________      
          .-\:      /-.    
         | (|:.     |) |    
          '-|:.     |-'     
            \::.    /      
             '::. .'        
               ) (          
             _.' '._        
            '-------'       
                
    The secret word: {utils.secret_word}   
"""

        popup = Toplevel(root)
        popup.title("🎉 Victory!")
        popup.resizable(False, False)
        popup.geometry(f"350x350+{posicaoX}+{posicaoY}")
        popup.iconbitmap(icon_path)
        
        label = Label(popup, text=trophy, font=("Courier", 10), justify="left")
        label.pack(padx=10, pady=5)
        
        ok_button = Button(popup, text="Nice", font=("Arial", 10, "bold"), command= lambda: end_game(popup), cursor="hand2")
        ok_button.pack(pady=5)
        
        popup.protocol("WM_DELETE_WINDOW", lambda: end_game(popup))
        popup.bind("<Return>", lambda event: end_game(popup))
        
    def show_defeat_popup():
        hangman = rf"""
        The word was: "{utils.secret_word}"

        ███████████████████████████
        ███████▀▀▀░░░░░░░▀▀▀███████
        ████▀░░░░░░░░░░░░░░░░░▀████
        ███│░░░░░░░░░░░░░░░░░░░│███
        ██▌│░░░░░░░░░░░░░░░░░░░│▐██
        ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
        ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
        ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
        ██▌░│██████▌░░░▐██████│░▐██
        ███░│▐███▀▀░░▄░░▀▀███▌│░███
        ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
        ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
        ████▄─┘██▌░░░░░░░▐██└─▄████
        █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
        ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
        █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
        ███████▄░░░░░░░░░░░▄███████
        ██████████▄▄▄▄▄▄▄██████████
        ███████████████████████████        
"""

        popup = Toplevel(root)
        popup.title("👾 Game Over!")
        popup.resizable(False, False)
        popup.geometry(f"400x420+{posicaoX}+{posicaoY}")
        popup.iconbitmap(icon_path)
        
        label = Label(popup, text=hangman, font=("Courier", 10), justify="left")
        label.pack(padx=10, pady=5)
        
        ok_button = Button(popup, text="OK", font=("Arial", 10, "bold"), command= lambda: end_game(popup), cursor="hand2")
        ok_button.pack(pady=5)
        
        popup.protocol("WM_DELETE_WINDOW", lambda: end_game(popup))
        popup.bind("<Return>", lambda event: end_game(popup))
        
    def pause():
        popup = Toplevel(root)
        popup.title("⏸️ Paused")
        popup.resizable(False, False)
        popup.geometry(f"550x250+{posicaoX}+{posicaoY}")
        popup.iconbitmap(icon_path)
        
        # Torna a janela modal
        popup.grab_set()       # Bloqueia interação com outras janelas
        popup.transient(root) # Mantém a janela acima da principal
        popup.focus_force()   # Foca automaticamente na janela de pause

        # Label de tentativas no topo, centralizado
        label_qt_attempts = Label(popup, text=f"🔢 Remaining attempts: {str(utils.attempts)}", font=("Arial", 14, "bold"))
        label_qt_attempts.pack(pady=10)

        # Preparar os textos
        tried_words = ", ".join(utils.attempted_words)
        tried_letters = ", ".join(utils.attempted_letters)

        # Frame horizontal para os dois labels
        info_frame = Frame(popup)
        info_frame.pack(pady=10, fill="both", expand=True)

        # Label de palavras à esquerda
        label_tried_words = Label(
            info_frame,
            text=f"🔤 Words already tried:\n\n{tried_words}",
            font=("Arial", 14, "bold"),
            justify="left",
            wraplength=240
        )
        label_tried_words.pack(side="left", padx=10, anchor="n")

        # Separador central
        separator = Frame(info_frame, width=2, bg="gray")
        separator.pack(side="left", fill="y", padx=30)

        # Label de letras à direita
        label_tried_letters = Label(
            info_frame,
            text=f"🔡 Letters already tried:\n\n{tried_letters}",
            font=("Arial", 14, "bold"),
            justify="left",
            wraplength=240
        )
        label_tried_letters.pack(side="left", padx=10, anchor="n")
        
        # Frame para os botões no rodapé
        button_frame = Frame(popup)
        button_frame.pack(pady=10)

        # Botão "Give Up"
        give_up_button = Button(button_frame, text="🏴 Give Up", font=("Arial", 10, "bold"),
                                command=lambda: go_back_menu_options(popup), cursor="hand2", width=10)
        give_up_button.pack(side="left", padx=10)

        # Botão "Close"
        close_button = Button(button_frame, text="✖️ Close", font=("Arial", 10, "bold"),
                            command=lambda: popup.destroy(), cursor="hand2", width=10)
        close_button.pack(side="left", padx=10)

    clear_root_window()
    utils.load_guessed_word()
    word = ' '.join(utils.guessed_word)

    frame_top = Frame(root)
    frame_top.pack()
    font_size = 14 if len(word) < 20 else 12 if len(word) < 30 else 10
    label = Label(frame_top, text=f"🔡 The secret word: {word}", font=("Arial", font_size, "bold"))
    label.pack(anchor="center")

    frame_center = Frame(root)
    frame_center.pack(expand=True, fill="both")

    input_guess = StringVar()
    entry = Entry(frame_center, textvariable=input_guess, font=("Arial", 18), relief="groove", width=30)
    entry.pack(fill="x", padx=20, pady=10, ipady=8)

    # Frame para os botões no rodapé
    bottom_frame = Frame(root)
    bottom_frame.pack(pady=10)

    verify_button = Button(bottom_frame, text="🔎 Verify", command=guess_verify, cursor="hand2")
    verify_button.pack(side="left", padx=10)
    pause_button = Button(bottom_frame, text="⏸️ Pause", command=pause, cursor="hand2")
    pause_button.pack(side="left", padx=10)

    # Faz o bind uma única vez
    entry.bind("<Return>", guess_verify)

def end_game(popup:Toplevel):
    popup.destroy()
    try_again = messagebox.askyesno(title="🤔 What now?", message="Would you like to try again?")
    if try_again:
        clear_root_window()
        difficulty_options()
    else:
        clear_root_window()
        root.deiconify()
        menu_options()
        
       