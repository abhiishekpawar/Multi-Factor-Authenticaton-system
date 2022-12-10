from tkinter import *
from tkinter import messagebox


from PIL import ImageTk
from  PIL import Image
import sqlite3
import os
root = Tk()
root.geometry('1366x768')
root.title("MultiFactor")

canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)
def readimg():
    os.system('python capturevideo.py')
    os.system('python convertframe.py')
def verify():
    os.system('python verify.py')
def hash1():
    os.system('python hash.py')
def auth():
        os.system('python auth.py')
def reg():
    os.system('python register.py')
Button(root, text='Register', width=25, height=1,bg='yellow', fg='black',  font=("bold", 10),command=reg).place(x=1000, y=250)
Button(root, text='Capture Video', width=25, height=1,bg='yellow', fg='black',  font=("bold", 10),command=readimg).place(x=1000, y=200)
Button(root, text='Verify', width=25, height=1,bg='yellow', fg='black',  font=("bold", 10),command=verify).place(x=1000, y=300)
Button(root, text='Hashing', width=25,height=1, bg='yellow', fg='black',  font=("bold", 10),command=hash1).place(x=1000, y=360)
#Button(root, text='Authentication', width=25, height=1,bg='yellow', fg='black',  font=("bold", 10),command=auth).place(x=1000, y=420)
root.mainloop()
