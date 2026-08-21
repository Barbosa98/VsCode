import tkinter as tk

# Screen Calculator

screen = tk.Tk()
screen.title("Calculator")
screen.geometry("300x300")
screen.config(bg= "Black")

# Button 1

buttons_frame = tk.Frame(screen)
buttons_frame.grid(row=3, column= 0)
button = tk.Button(buttons_frame, text="1" , width=10, height=4)
button.config(bg= "Orange")
button.grid(row=1, column=0)

# Button 2


buttons_frame = tk.Frame(screen)
buttons_frame.grid(row=3, column= 1)
button2 = tk.Button(buttons_frame, text="2", width=10, height= 4)
button2.config(bg= "Orange")
button2.grid(row=2, column=1)


# Button 3


buttons_frame = tk.Frame(screen)
buttons_frame.grid(row=3, column= 4)
button3 = tk.Button(buttons_frame, text="3", width=10, height= 4)
button3.config(bg= "orange")
button3.grid(row=0, column= 4)

# Button 4
button4 = tk.Button(screen, text="4", width=10, height= 4)
button4.config(bg= "orange")



# Button 5

button5 = tk.Button(screen, text="5", width=10, height= 4)
button5.config(bg= "orange")


# Button 6

button6 = tk.Button(screen, text="6", width=10, height= 4)
button6.config(bg= "orange")


# Button 7

button7 = tk.Button(screen, text="7", width=10, height= 4)
button7.config(bg= "orange")

# Button 8

button8 = tk.Button(screen, text="8", width=10, height= 4)
button8.config(bg= "orange")


# Button 9
button9 = tk.Button(screen, text="9", width=10, height= 4)
button9.config(bg= "orange")



# Loop Interface
screen.mainloop()

