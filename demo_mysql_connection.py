import tkinter as tk
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="ci_test"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM category")

myresult = mycursor.fetchall()


def print_users():
  for x in range(len(myresult)):
    if x == 0:
      for z in myresult:
        if z == 0:
          print(myresult[0][x])
    
     


window = tk.Tk()
window.geometry("250x100")
frame = tk.Frame(window)
frame.pack()


slogan = tk.Button(frame,
                   text="Submit",
                   command=print_users)
slogan.pack(side=tk.LEFT)


window.mainloop()