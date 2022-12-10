from tkinter import *
import sqlite3
import os
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

import cv2
from PIL import ImageTk, Image
root = Tk()
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back1.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)
root.geometry('1366x768')
root.title("Login")
Faceimg=StringVar()
Un = StringVar()
Pw = StringVar()
def back():
    root.destroy()
    os.system('python main.py')

def login():
    un = Un.get()
    pw = Pw.get()
    if un=="":
        messagebox.showinfo("Enter Username")
    else:
        if pw == "":
            messagebox.showinfo("Enter Password")
        else:
            conn = sqlite3.connect('Form.db')
            with conn:
                    cur = conn.cursor()
                    cur.execute("SELECT * FROM register where Un=? and pw=?",(un,pw))
                    rows = cur.fetchall()
                    for row in rows:
                         dbuser = row[3]
                         dbpw=row[4]
                    if dbuser == un and dbpw == pw:
                            root.destroy()
                            messagebox.showinfo("Login", " Login Successful")

                    else:
                            messagebox.showinfo("Login", " Try Again")
#main program



label_0 = Label(root, text="Login...", bg='white', width=20, font=("bold", 20))
label_0.place(x=205, y=350)
label_1 = Label(root, text="Username",  bg='white', font=("bold", 10))
label_1.place(x=250, y=450)
entry_2 = Entry(root, textvar=Un)
entry_2.place(x=400, y=450)
label_3 = Label(root, text="Password", bg='white', font=("bold", 10))
label_3.place(x=250, y=500)
entry_6 = Entry(root, textvar=Pw, show="*")
entry_6.place(x=400, y=500)
Button(root, text='Login', width=10, bg='gray', fg='white', command=login).place(x=250, y=550)
Button(root, text='Cancel', width=10, bg='gray', fg='white', command=back).place(x=350, y=550)

root.mainloop()
