import tkinter as tk

# Screen Calculator

screen = tk.Tk()
screen.title("Calculator")
screen.geometry("300x400")
screen.config(bg= "Black")

# Display

display = tk.Entry(screen, width=18, font=("Arial", 20), justify="right")
display.config(bg= "Black", fg= "White")
display.grid(row=0, column=0, padx=10, pady=10)

# Display Frame

def display_frame():
    display_frame = tk.Frame(screen)
    display_frame.config(bg= "Black")
    display_frame.grid(row=0, column=0, padx=10, pady=10)

# add number to display

def add_number(number):
    display.insert(tk.END, number)

# Frame for the buttons

buttons_frame = tk.Frame(screen)
buttons_frame.config(bg= "Black")
buttons_frame.grid(row=1, column= 0, padx= 10, pady= 10)

# calculate the result

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Button Equal

buttonEqual = tk.Button(buttons_frame, text="=", width=8, height=3, bg="orange", command=lambda: (add_number("=")))
buttonEqual.grid(row=3, column=2)
buttonEqual.config(command=lambda: calculate())

# Button Clear

buttonClear = tk.Button(buttons_frame, text="C", width=8, height=3, bg="orange", command=lambda: display.delete(0, tk.END))
buttonClear.grid(row=3, column=0)

# button Plus

buttonPlus = tk.Button(buttons_frame, text="+", width=8, height=3, bg="orange", command=lambda: add_number("+"))
buttonPlus.grid(row=3, column=1)

# Button Minus

buttonMinus = tk.Button(buttons_frame, text="-", width=8, height=3, bg="orange", command=lambda: add_number("-"))
buttonMinus.grid(row=4, column=0)

# Button Multiply

buttonMultiply = tk.Button(buttons_frame, text="*", width=8, height=3, bg="orange", command=lambda: add_number("*"))
buttonMultiply.grid(row=4, column=1)

# Button Divide

buttonDivide = tk.Button(buttons_frame, text="/", width=8, height=3, bg="orange", command=lambda: add_number("/"))
buttonDivide.grid(row=4, column=2)

# Button 1

button1 = tk.Button(
    buttons_frame,
    text="1",
    width=8,
    height=3,
    bg="orange",
    command=lambda: add_number("1")
)
button1.grid(row=0, column=0)

# Button 2

button2 = tk.Button(buttons_frame, text="2", width=8, height=3, bg="orange", command=lambda: add_number("2"))
button2.grid(row=0, column=1)

# Button 3

button3 = tk.Button(buttons_frame, text="3", width=8, height=3, bg="orange", command=lambda: add_number("3"))
button3.grid(row=0, column=2)

# Button 4
button4 = tk.Button(buttons_frame, text="4", width=8, height=3, bg="orange", command=lambda: add_number("4"))
button4.grid(row=1, column=0)

# Button 5

button5 = tk.Button(buttons_frame, text="5", width=8, height=3, bg="orange", command=lambda: add_number("5"))
button5.grid(row=1, column=1)

# Button 6

button6 = tk.Button(buttons_frame, text="6", width=8, height=3, bg="orange", command=lambda: add_number("6"))
button6.grid(row=1, column=2)

# Button 7

button7 = tk.Button(buttons_frame, text="7", width=8, height=3, bg="orange", command=lambda: add_number("7"))
button7.grid(row=2, column=0)

# Button 8

button8 = tk.Button(buttons_frame, text="8", width=8, height=3, bg="orange", command=lambda: add_number("8"))
button8.grid(row=2, column=1)

# Button 9
button9 = tk.Button(buttons_frame, text="9", width=8, height=3, bg="orange", command=lambda: add_number("9"))
button9.grid(row=2, column=2)




# Loop Interface
screen.mainloop()

