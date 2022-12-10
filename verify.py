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
img = Image.open('back3.png')
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
def reg():
    root.destroy()
    os.system('python register.py')

def open_File():
    faceimg = askopenfilename(filetypes=[(".jpg", "*.jpg")])
    conn = sqlite3.connect('Form.db')
    cursor = conn.cursor()
    cursor.execute('delete from imgsave')
    cursor.execute('INSERT INTO imgsave(img ) VALUES(?)', (faceimg,))

    conn.commit()
    Faceimg.set(faceimg)
    fm = Faceimg.get()
    load = Image.open(fm)
    render = ImageTk.PhotoImage(load)
    # labels can be text or images
    img = Label(root, image=render)
    img.image = render
    img.place(x=700, y=200)
# Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
# Read the input image
    img = cv2.imread(faceimg)

# Convert into grayscale
    gray = cv2.cvtColor(img, 1)
# Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        messagebox.showinfo("Multifactor","Phase 1 Authentication is successful")
# Display the output
    cv2.imshow('img', img)

    cv2.waitKey()



Button(root, text='Cancel', width=10, bg='gray', fg='white', command=back).place(x=200, y=50)
Button(root, text='Browse Photo', width=10, bg='gray', fg='white', command=open_File).place(x=100, y=50)

root.mainloop()
