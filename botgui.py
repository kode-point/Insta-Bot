from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

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
    l5 = Label(f3, text="Options", font=font1, fg="White", bg="Black")
    l5.place(x=270, y=0)
    Button(f3, text="Based on Hashtags", cursor="hand2", width=37, height=3).place(x=200, y=100)
    Button(f3, text="Based on Username(s)", cursor="hand2", width=37, height = 3).place(x=200, y=200)
    Button(f3, text="Auto Follow-back", cursor="hand2", width=37, height=3).place(x=200, y=300)


def like_comment():
    delall()
    l5 = Label(f3, text="Options", font=font1, fg="White", bg="Black")
    l5.place(x=270, y=0)
    Button(f3, text="Based on Hashtags", cursor="hand2", width=37, height=3).place(x=200, y=150)
    Button(f3, text="Based on Username(s)", cursor="hand2", width=37, height = 3).place(x=200, y=300)

def secwin():
    if len(uname.get())==0 or len(password.get())==0:
        messagebox.showerror("Error", "Please enter details in all the fields.")
    else:
        global f3
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
        Button(f2, text="Follow", cursor="hand2", command=follow, width=37, height=3).place(x=10, y=100)
        Button(f2, text="Like/Comment", cursor="hand2", command=like_comment, width=37, height = 3).place(x=10, y=250)
        f3 = Frame(win2, height=600, width=700, borderwidth = 5, relief = SUNKEN, bg="Black")
        f3.propagate(0)
        f3.place(x=300, y=0)
        l5 = Label(f3, text="Options", font=font1, fg="White", bg="Black")
        l5.place(x=270, y=0)

Button(f1, text="Login", cursor="hand2", command=secwin, border=4, width=10).place(x=480, y=350)
Button(f1, text="Reset", cursor="hand2", command=clear, border=4, width=10).place(x=620, y=350)

win1.mainloop()
