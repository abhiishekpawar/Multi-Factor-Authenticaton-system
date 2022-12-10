
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#import image
import os
from PIL import ImageTk, Image
root = Tk()
root.geometry('1366x768')
root.title("Registration Form")
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back2.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)
Fullname = StringVar()
Email = StringVar()
Contact = StringVar()
Un = StringVar()
Pw = StringVar()
Age = StringVar()
Gkey = StringVar()
Faceimg = StringVar()
def cancel():
    root.destroy()
    os.system('python Main.py')



def database():
    name1 = Fullname.get()
    email = Email.get()
    contact = Contact.get()

    l=len(contact)


    un = Un.get()
    pw = Pw.get()
    age= Age.get()
    gkey = "-"
    faceimg = Faceimg.get()
    status="-"

    if name1=="":
        messagebox.showinfo("Multifactor","Enter Name")
    else:
        if email == "":
            messagebox.showinfo("Multifactor","Enter Email")
        else:
            if contact == "":
                messagebox.showinfo("Multifactor", "Enter Contact")
            else:
                if age == "":
                    messagebox.showinfo("Multifactor", "Enter Age")
                else:
                    if un == "":
                        messagebox.showinfo("Multifactor", "Username")
                    else:
                        if pw == "":
                         messagebox.showinfo("Multifactor", "Enter Password")
                        else:
                            if not (re.search(regex, email)):
                                messagebox.showinfo("Multifactor", "Enter valid Email")
                            else:
                                if l != 10:
                                    messagebox.showinfo("Multifactor", "Enter 10 digits only")
                                else:
                                    if  not name1.isalpha():
                                        messagebox.showinfo("Multifactor", "Enter Name in alphabets Only ")
                                    else:
                                        if  age.isalpha():
                                            messagebox.showinfo("Multifactor", "Enter Age in digits Only ")
                                        else:




                                                conn = sqlite3.connect('Form.db')
                                                with conn:
                                                    cursor = conn.cursor()
                                                    cursor.execute("SELECT * FROM register")
                                                    rows = cursor.fetchall()
                                                    for row in rows:
                                                        dbuser = row[0]
                                                       
                                                        ph1 = row[1]
                                                    if dbuser == name1 and email == ph1:
                                                        messagebox.showinfo("Multifactor", "Already Registered")
                                                    else:
                                                        cursor.execute(
                                                        'CREATE TABLE IF NOT EXISTS register (Fullname TEXT,Email TEXT,Contact TEXT,Un TEXT,Pw TEXT,Age TEXT,Status TEXT,Gkey TEXT,Faceimg TEXT)')
                                                        cursor.execute('INSERT INTO register (FullName,Email,Contact,Un,Pw,Age,Status,Gkey,Faceimg) VALUES(?,?,?,?,?,?,?,?,?)',
                                                        (name1, email, contact, un, pw, age, status,gkey,faceimg,))

                                                        conn.commit()
                                                        messagebox.showinfo("Multifactor","Record Saved")

def open_File():
    faceimg = askopenfilename(filetypes=[(".jpg", "*.jpg")])
    Faceimg.set(faceimg)
    fm = Faceimg.get()
    load = Image.open(fm)
    render = ImageTk.PhotoImage(load)

    # labels can be text or images
    img = Label(root, image=render,width=200,height=200)
    img.image = render
    img.place(x=500, y=300)



label_0 = Label(root, justify=LEFT, bg='white', text="Registration Here..", width=30, font=("bold", 20))
label_0.place(x=100, y=180)


label_1 = Label(root, text="FullName", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_1.place(x=100, y=300)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=250, y=300)

label_2 = Label(root, text="Email", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_2.place(x=100, y=350)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=250, y=350)

label_3 = Label(root, text="Contact",bg='white',justify=LEFT, width=20, font=("bold", 10))
label_3.place(x=100, y=400)

entry_3 = Entry(root, textvar=Contact)
entry_3.place(x=250, y=400)

label_4 = Label(root, text="RegNo", bg='white',justify=LEFT, width=20, font=("bold", 10))
label_4.place(x=100, y=450)

entry_5 = Entry(root, textvar=Un)
entry_5.place(x=250, y=450)

label_5 = Label(root, text="Password",bg='white', justify=LEFT, width=20, font=("bold", 10))
label_5.place(x=100, y=500)

entry_6 = Entry(root, textvar=Pw)
entry_6.place(x=250, y=500)

label_7 = Label(root, text="Age",bg='white', justify=LEFT, width=20, font=("bold", 10))
label_7.place(x=100, y=550)

entry_7 = Entry(root, textvar=Age)
entry_7.place(x=250, y=550)

label_8 = Label(root, text="Course",bg='white', justify=LEFT, width=20, font=("bold", 10))
label_8.place(x=100, y=600)

entry_8 = Entry(root, textvar=Gkey)
entry_8.place(x=250, y=600)

label_7 = Label(root, text="Face Image",bg='white',width=20, font=("bold", 10))
label_7.place(x=100, y=650)

entry_7 = Entry(root, textvar=Faceimg)
entry_7.place(x=250, y=650)


Button(root, text='Submit', width=10, bg='gray', fg='white', command=database).place(x=750, y=650)
Button(root, text='Cancel', width=10, bg='gray', fg='white', command=cancel).place(x=830, y=650)
Button(root, text='Browse Photo', width=20, bg='gray', fg='white', command=open_File).place(x=500, y=650)

root.mainloop()
