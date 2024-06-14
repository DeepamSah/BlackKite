from datetime import datetime
from tkinter import *

def update():
    year_ = int(year.get())
    month_ = int(month.get())
    day_ = int(day.get())

    today = datetime.now()

    if today.month < month_ or (today.month == month_ and today.day < day_):
        real_year = today.year - year_ - 1
    else:
        real_year = today.year - year_

    real_month = today.month - month_
    if real_month < 0:
        real_month += 12

    real_day = today.day - day_
    if real_day < 0:
        real_day += 30
    result_label.config(text=f"You are {real_year} years, {real_month} months, and {real_day} days old")

window = Tk()
window.title = "Age Calculator"
window.geometry('600x500')
window['bg'] = 'black'

# variables
year = IntVar()
month = IntVar()
day = IntVar()

Label(window, text='Age Calculator', fg='white', bg='black', font=('Arial', 31)).pack()

frame = Frame(window, bg='black')

frame.columnconfigure(0, weight=3)

Label(frame, text="Enter the Year:", bg="black", fg="white", font=('Arial', 12)).grid(row=0, column=0)
InputYear = Entry(frame, width=40, font="arial", textvariable=year)
InputYear.grid(row=0, column=1)

Label(frame, text="Enter the Month:", bg="black", fg="white", font=('Arial', 12)).grid(row=1, column=0)
InputMonth = Entry(frame, width=40, font="arial", textvariable=month)
InputMonth.grid(row=1, column=1)

Label(frame, text="Enter the Day:", bg="black", fg="white", font=('Arial', 12)).grid(row=2, column=0)
InputDay = Entry(frame, width=40, font="arial", textvariable=day)
InputDay.grid(row=2, column=1)

frame.pack()

submit_button = Button(window, text="Submit", command=update, bg='grey', fg='white')
submit_button.pack()

result_label = Label(window, text="", fg='white', bg='black', font=('arial', 16))
result_label.pack()

window.mainloop()