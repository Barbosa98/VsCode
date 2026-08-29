from tkinter import *

# Screen

root = Tk()
root.geometry("300x400")
root.config(bg= "Black")
root.title("Translater")

# Creating a Label Widget
myLabel = Label(root, text="I dont know")
myLabel.config(bg= "Black",fg="White", font=("Arial", 20))

# Shoving it onto the screen 
myLabel.pack()

# Main Looping
root.mainloop()