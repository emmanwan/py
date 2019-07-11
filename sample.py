import tkinter as tk
from tkinter import messagebox

def write_slogan(event=None):
    # print(inputext.get())
    messagebox.showinfo(titolo, inputext.get())

def close_window():
    window.destroy()

def esc_window(event):
    window.withdraw()

window = tk.Tk()
titolo = 'Hello'
window.title(titolo)
window.geometry("250x100")
frame = tk.Frame(window)
frame.pack()

labelin = tk.Label(frame, text="Input Text")
labelin.pack()

inputext = tk.Entry(frame)
inputext.pack()

slogan = tk.Button(frame,
                   text="Submit",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

window.bind('<Return>', write_slogan)

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=close_window)
button.pack(side=tk.LEFT)

window.bind('<Escape>', esc_window)

window.mainloop()

