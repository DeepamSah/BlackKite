from pytube import YouTube
from tkinter import *
import sys

window = Tk()
window.geometry('500x400')
window.title('Youtube Video Downloader')
window.config(bg='black')

var = StringVar()
title = StringVar()

clicked_resolution = StringVar()  # Declare a global variable

def clicked(resolution):
    clicked_resolution.set(resolution)
    return resolution

def process():
    video = var.get()
    you = YouTube(video)
    if title.get() == '':
        file = str(you.streams.filter(res=clicked_resolution.get()).first().default_filename)
    else:
        file = str(title.get()) + '.mp4'
    you.streams.filter(res=clicked_resolution.get()).first().download(filename=file)
    try:
        print("File Size: " + str(you.streams.filter().first().filesize_mb) + "MB")
    except Exception as e:
        print("Error: File size information unavailable.")
    print("Video Name: " + str(you.streams.filter().first().default_filename))
    sys.exit()

    
    
def clicked(resolution):
        print(resolution)
        return resolution

Label(window, fg='white', text='Youtube Video Downloader', font=('lucida sans', 23), bg='black').grid(pady=10, column=0, row=0, padx=19)

input_frame = Frame(window, bg="black")
input_frame.grid(pady=10)

input_label = Label(input_frame, text="Enter the URL:  ", bg="black", fg="white")
input_label.pack(side="left", anchor="center")

user_input_entry = Entry(input_frame, width=40, font="arial", textvariable=var)
user_input_entry.pack(anchor="center")
user_input_entry.focus()

title_frame = Frame(window, bg = 'black')
title_frame.grid(pady=10)

titl_label = Label(title_frame, text= "Enter the name of the file: ", bg='black', fg='white')
titl_label.pack(side='left', padx=10)

title_ = Entry(title_frame, textvariable=title)
title_.pack(side='left')

Checkbutton_grid = Frame(window, bg = 'black')
Checkbutton_grid.grid()

cb1 = Checkbutton(Checkbutton_grid, text='Resolution: 4k', command=lambda: clicked('2160p'))
cb2 = Checkbutton(Checkbutton_grid, text='Resolution: 1080p', command=lambda: clicked('1080p'))
cb3 = Checkbutton(Checkbutton_grid, text='Resolution: 720p', command=lambda: clicked('720p'))

cb1.grid(column=0, row=3, sticky=W, padx=10)
cb2.grid(column=1, row=3, sticky=W, padx=10)
cb3.grid(column=2, row=3, sticky=W, padx=10)

submit = Button(window, text='Submit', command=process, bg='grey', font=('arial', 20))
submit.grid(pady=10)

print(clicked)

mainloop()