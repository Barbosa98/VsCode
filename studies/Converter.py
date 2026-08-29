import tkinter as tk

## Screen

screen = tk.Tk()
screen.geometry(("300x100"))
screen.config(background= "Black")
screen.title("Converter")

## Screen2

Label = tk.Label(screen, text="Real == Dollar/Euro")
Label.config(foreground= "LightBlue",
              background= "Black",
               font= "Arial")
Label.pack()

## Lopping

screen.mainloop()