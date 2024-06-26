from tkinter import *
import PyDictionary

root = Tk()
root.geometry('600x400')
root.title('Dictionary By Deepam')
root['bg'] = 'black'

user_input_var = StringVar()

def get_meaning():
    user_input = user_input_var.get()
    meaning = PyDictionary.PyDictionary.meaning(user_input)

    formatted_output = ""
    for speech, meanings in meaning.items():
        for meaning_temp in meanings:
            formatted_output += f"{speech}: {meaning_temp}\n"
    return formatted_output

def update_meaning():
    text = get_meaning()
    meaning_text.delete(1.0, END) 
    meaning_text.insert(END, text)

root.columnconfigure(0, weight=1) 

title_label = Label(root, text='Dictionary', font=('times new roman', 41), background='black', foreground='white')
title_label.grid(row=0, column=0, sticky=NSEW) 

input_frame = Frame(root, bg="black")
input_frame.grid()

input_label = Label(input_frame, text="Enter the word:", bg="black", fg="white")
input_label.pack(side="left", anchor="center")

user_input_entry = Entry(input_frame, width=40, font="arial", textvariable=user_input_var)
user_input_entry.pack(anchor="center")
user_input_entry.focus()

submit_button = Button(root, text="Submit", command=update_meaning, bg='grey', fg='white')
submit_button.grid(pady=10)

meaning_label = LabelFrame(root, border=6,width=550, height=235,  text="", font=('arial', 10))
meaning_label.grid()
meaning_label.pack_propagate(False)

meaning_text = Text(meaning_label, wrap='word', state='normal', bg='black', fg='white', font='parable')
meaning_text.pack(fill='both', expand=True)

root.mainloop()