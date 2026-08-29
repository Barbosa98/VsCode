from tkinter import Tk
from zoneinfo import ZoneInfo
from datetime import datetime
import calendar

#screen = Tk()
#screen.title("Time")
#screen.geometry("640x480")
#screen.config(background= "Black")


Year = int(input
           ("Type the year: "))
Month = int(input
            ("Type the month: "))

Hora = (datetime.now(ZoneInfo("Asia/Manila")))

print(calendar.month(Year, Month))
print("Seu horario é: ", Hora.strftime("%H:%M:%S"))


