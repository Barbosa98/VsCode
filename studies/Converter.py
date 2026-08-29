import tkinter as tk

## Screen

screen = tk.Tk()
screen.title("Converter")
screen.geometry(("300x100"))
screen.config(background= "Black")



# Converter Real --> Dollar

print("Choose a currency:")
print("1 - Dollar")
print("2 - Euro")

choice = input("Type your choice: ")

Real = float(input("Type any value to converting: "))

## Converter Real --> Dollar

if choice == "Dollar":
    Dollar = Real * 0.1925
    print(f"You converted: ${Dollar:.2f}")

## Converter Real --> Euro

elif choice == "Euro":
    Euro = Real * 0.1662
    print(f"You converted: ${Euro:.2f}")

## Invalid

else:
    print("Invalid choice!")

## Lopping

screen.mainloop()