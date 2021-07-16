from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os

win1 = Tk()
win1.title("Log in")
win1.geometry('1000x600')
win1.maxsize(1000, 600)
win1.minsize(1000, 600)
photo2 = PhotoImage(file="logo4.png")
win1.iconphoto(False, photo2)
font1 = ("Times", 25, "bold")
font2 = ("Roboto Mono", 18)

f1 = Frame(win1, height=600, width=1000, bg="Black")
f1.propagate(0)
f1.place(x=0, y=0)


img = Image.open("instalogobw.png")
img = img.resize((300,90))

photo = ImageTk.PhotoImage(img)
Label(win1, image=photo, borderwidth=0).place(x=400,y=45)

uname = StringVar()
password = StringVar()


l1 = Label(f1, text='User Name:', font=font2, bg="Black", fg="White")
l1.place(x=250, y=180)
e1 = Entry(f1, textvariable=uname, width=50, border=2)
e1.place(x=450, y=185)

l2 = Label(f1, text='Password:', font=font2,  bg="Black", fg="White")
l2.place(x=250, y=260)
e2 = Entry(f1, textvariable=password, show = '*', width=50, border=2)
e2.place(x=450, y=265)


def clear():
    uname.set("")
    password.set("")

def delall():
    for widgets in f3.winfo_children():
        widgets.destroy()

def follow():
    delall()
    follow_button['state'] = DISABLED
    like_button['state'] = NORMAL
    msg_button['state'] = NORMAL
    l6 = Label(f3, text="Follow based on:-", font=font1, fg="White", bg="Black")
    l6.place(x=210, y=0)
    Button(f3, text="Hashtags", cursor="hand2", width=37, height=3).place(x=200, y=100)
    Button(f3, text="Username(s)", cursor="hand2", width=37, height = 3).place(x=200, y=250)
    Button(f3, text="Auto Follow-back", cursor="hand2", width=37, height=3).place(x=200, y=400)


def like_comment():
    delall()
    like_button['state'] = DISABLED
    follow_button['state'] = NORMAL
    msg_button['state'] = NORMAL
    l7 = Label(f3, text="Like/Comment based on:-", font=font1, fg="White", bg="Black")
    l7.place(x=170, y=0)
    Button(f3, text="Hashtags", cursor="hand2", width=37, height=3).place(x=200, y=150)
    Button(f3, text="Post ID", cursor="hand2", width=37, height=3).place(x=200, y=300)

def dialogbox():
    #f3.filename contains the path of the csv/txt file along with the file name
    f3.filename = filedialog.askopenfilename(initialdir="C:", title="Select a csv/txt File", filetypes=(("csv files", "*.csv"),("txt files", "*.txt")))
    if (len(f3.filename) > 0) and (len(msg.get()) > 0):
        filename = os.path.basename(f3.filename)
        l11 = Label(f3, text=filename, font=font2, bg="Black", fg="White")
        l11.place(x=280, y=330)
        send_btn['state'] = NORMAL

def message():
    delall()
    global msg, send_btn
    msg_button['state'] = DISABLED
    like_button['state'] = NORMAL
    follow_button['state'] = NORMAL
    msg = StringVar()
    l8 = Label(f3, text='Enter the message:', font=font2, bg="Black", fg="White")
    l8.place(x=50, y=180)
    e8 = Entry(f3, textvariable=msg, width=60, border=2)
    e8.place(x=280, y=185)
    l9 = Label(f3, text='Choose the csv file:', font=font2, bg="Black", fg="White")
    l9.place(x=50, y=260)
    Button(f3, text="Browse files..", cursor="hand2", command=dialogbox, border=4, width=10).place(x=280, y=260)
    l10 = Label(f3, text='Selected file name: ', font=font2, bg="Black", fg="White")
    l10.place(x=50, y=330)
    send_btn = Button(f3, text="Send", cursor="hand2", border=4, width=10, state=DISABLED)
    send_btn.place(x=300, y=390)

def secwin():
    if len(uname.get())==0 or len(password.get())==0:
        messagebox.showerror("Error", "Please enter details in all the fields.")
    else:
        global f3, follow_button, like_button, msg_button
        win2 = Toplevel()
        win2.title("Menu")
        win2.geometry('1000x600')
        win2.maxsize(1000, 600)
        win2.minsize(1000, 600)
        win2.iconphoto(False, photo2)
        f2 = Frame(win2, height=600, width=300, borderwidth = 5, relief = SUNKEN, bg="#FFFAFA")
        f2.propagate(0)
        f2.place(x=0, y=0)
        l4 = Label(f2, text="Menu", font=font1, bg="#FFFAFA")
        l4.place(x=100, y=0)
        follow_button = Button(f2, text="Follow", cursor="hand2", command=follow, border=4, width=37, height=3)
        follow_button.place(x=10, y=100)
        like_button = Button(f2, text="Like/Comment", cursor="hand2", command=like_comment, border=4, width=37, height = 3)
        like_button.place(x=10, y=250)
        msg_button = Button(f2, text="Send a message", cursor="hand2", command=message, border=4, width=37, height = 3)
        msg_button.place(x=10, y=400)
        f3 = Frame(win2, height=600, width=700, borderwidth = 5, relief = SUNKEN, bg="Black")
        f3.propagate(0)
        f3.place(x=300, y=0)
        inst = "Please select the desired option from the Menu."
        l5 = Label(f3, text=inst, font=font2, fg="White", bg="Black")
        l5.place(x=80, y=0)

Button(f1, text="Login", cursor="hand2", command=secwin, border=4, width=10).place(x=480, y=350)
Button(f1, text="Reset", cursor="hand2", command=clear, border=4, width=10).place(x=620, y=350)

win1.mainloop()
