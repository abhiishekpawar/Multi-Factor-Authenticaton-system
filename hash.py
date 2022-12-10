import sqlite3
from tkinter import messagebox

from PIL import Image
import imagehash
from tkinter import *
from tkinter import messagebox


from PIL import ImageTk, Image
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
conn = sqlite3.connect('Form.db')
with conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM imgsave")
    rows = cursor.fetchall()
    for row in rows:
        filename1 = row[0]
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM register")
    rows = cursor.fetchall()
    for row in rows:
        filename = row[8]
    print(filename)
    print(filename1)
    HDBatmanHash = imagehash.average_hash(Image.open(filename))
    print('Hash: ' + str(HDBatmanHash))

    SDBatmanHash = imagehash.average_hash(Image.open(filename1))
    print('Hash: ' + str(SDBatmanHash))


    if(HDBatmanHash == SDBatmanHash):
        print("The pictures are perceptually the same !")
        messagebox.showinfo("Multifactor","Phase 2 Authentication is Successful")
        os.system('python auth.py')
    else:
        print("The pictures are different, distance: " , (HDBatmanHash - SDBatmanHash))
        messagebox.showinfo("Multifactor", "Try Again")
