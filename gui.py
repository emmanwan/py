import tkinter as tk

def esc_window():
    window.destroy()

window = tk.Tk()
window.geometry("380x200")

label1 =  tk.Label(window, text="Firstname").grid(row=0)
label2 =  tk.Label(window, text="Lastname").grid(row=1, column=0)

label3 = tk.Label(window, text="Contact no.").grid(row=0, column=2)
label4 = tk.Label(window, text="E-mail").grid(row=1, column=2)
label5 = tk.Label(window, text="Given Data").grid(row=2, column=1)

input1 = tk.Entry(window).grid(row=0, column=1)
input2 = tk.Entry(window).grid(row=1, column=1)

input3 = tk.Entry(window).grid(row=0, column=3)
input4 = tk.Entry(window).grid(row=1, column=3)
input5 = tk.Text(window, height=10, width=10)

button1 = tk.Button(window, text="ADD", width=10).grid(row=3, column=3)
button2 = tk.Button(window, text="UPDATE", width=10).grid(row=4, column=3)
button3 = tk.Button(window, text="DELETE", width=10).grid(row=5, column=3)

window.bind('<Escape>', esc_window)

window.mainloop()