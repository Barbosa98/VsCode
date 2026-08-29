import tkinter as tk
from datetime import datetime


# Tela do Timer
screen = tk.Tk()
screen.title("Timer")
screen.geometry("500x100")
screen.config(bg= "Black")

# Texto 

text = tk.Label(screen, text= datetime.now().strftime("%H:%M:%S") , font=("Arial", 60))
text.config(fg= "lightgreen")
text.config(bg= "Black")
text.pack()

# Atualizaçao da tela

def atualizar_time():
    text.config(text=datetime.now().strftime("%H:%M:%S"))
    screen.after(1000, atualizar_time)

# Iniciar loop da Interface
atualizar_time()
screen.mainloop()

