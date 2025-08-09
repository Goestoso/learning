#importando bibliotecas
from  tkinter import Tk, Frame, Label, Button, Entry, messagebox, StringVar
from src import utils

#variáveis globais
largura_janela = 340
altura_janela = 160
root = Tk()

def main_window():
    root.title("Artificial Guess")
    root.geometry()
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    posicaoX = (largura_tela - largura_janela) // 2
    posicaoY = (altura_tela - altura_janela) // 2
    root.resizable(False, False)
    root.geometry(f"{largura_janela}x{altura_janela}+{posicaoX}+{posicaoY}")
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
    button_start = Button(frame_center, text="▶ Start", command= loading_secret_word, cursor="hand2")
    button_start.pack(pady=5, padx=80, fill="x")
    button_help = Button(frame_center, text="❓ Help", command= lambda: messagebox.showinfo("📜 Instructions for Guess Game 📜", "🔹 The goal is to guess the secret word chosen randomly.\n🔹 The word will be represented by underscores (_ _ _).\n🔹 You can guess one letter at a time or try to guess the full word.\n🔹 If the letter is in the word, it will be revealed in the correct positions.\n🕹️ The game ends when:\n        ✅ You correctly guess the word 🎉\n        ❌ You run out of tries and lose 😢\n🔹 Good luck and have fun! 🚀\n🔹 If you guess wrong, you lose a try."), cursor="hand2")
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
    
def loading_secret_word(): # função que mostra que uma nova palavra secreta está sendo carregada
    clear_root_window()
    utils.load_secret_word()
    label = show_main_message(msg="Loading secret word...")
    root.after(4000, lambda l=label, msg="🧍 Attention...",f=("Arial", 20): change_main_message(l, msg, f))
    root.after(8000, lambda l=label, msg="🚶 Get ready...",f=("Arial", 20): change_main_message(l, msg, f))
    root.after(12000, lambda l=label, msg="🏃 Go!",f=("Arial", 20): change_main_message(l, msg, f))
    clear_root_window()    
    
def start_game():
    loading_secret_word()
    utils.load_guessed_word()
    guess_top_frame(' '.join(utils.guessed_word))
    frame_center = Frame(root)
    frame_center.pack(expand=True, fill="both")
    input_guess = StringVar()
    entry = Entry(frame_center, relief="groove", textvariable=input_guess)
    entry.pack(expand=True, fill="both")
    verify_button = Button(frame_center, text="🔎 Verify", command= lambda: guess_verify, cursor="hand2")
    verify_button.pack(pady=5, padx=80, fill="x")

    def guess_verify():
        utils.guessing(guess=input_guess.get())
        if utils.win:   
            messagebox.showinfo(title="🏆 Congratulations!", message="You guess the secret word!")
        elif utils.invalid:
            messagebox.showerror(title="🚨 Oops!", message=utils.invalid_msg)
        elif utils.good_letter:
            messagebox.showinfo(title="✅ Very good!", message=f'\nThe letter "{input_guess.get()}" is correct!')
        elif utils.already_attempted:
            messagebox.showinfo(title="👁️ Pay attention!", message=f'\nThe word or letter "{input_guess.get()}" has already been tried, try another guess!')
        elif utils.fail: 
            messagebox.showinfo(title="💪 Nice try!", message=f"Incorrect guess. Try again.\n Do you still have {utils.attempts} attempts.")
        elif  utils.attempts == 0:
            messagebox.showinfo(title="👾 Game over!",message=f'You lose! The word was: "{utils.secret_word}"')
        
    
    def guess_top_frame(word:str):
        frame_top = Frame(root)
        frame_top.pack()
        label = Label(frame_top, text=f"🔡 The secret word: {word}", font=("Arial", 16, "bold"))
        label.pack(anchor="center")
        