from tkinter import *
import datetime

def update_time():
    current_time = datetime.datetime.now().strftime('%I:%M:%S %p')
    time_label.config(text=current_time)
    window.after(1000, update_time)  

# Create the main window
window = Tk()
window.geometry('600x200')
window['bg'] = 'green'

canvas = Canvas(window)

canvas.create_line(50, 0, 50, 1000 , fill='white')


# Create a label for displaying the time
time_label = Label(canvas, fg='white', bg = 'green',font=('calibri', 50))
time_label.pack()

canvas.pack()

# Start updating the time
update_time()

# Run the Tkinter event loop
window.mainloop()