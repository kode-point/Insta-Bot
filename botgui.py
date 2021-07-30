from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from time import sleep
from backend_login import *


win1 = Tk()
win1.title("Log in")
win1.geometry('1000x600')
win1.maxsize(1000, 600)
win1.minsize(1000, 600)
photo2 = PhotoImage(file="images/logo4.png")
win1.iconphoto(False, photo2)
font1 = ("Times", 25, "bold")
font2 = ("Roboto Mono", 18)

f1 = Frame(win1, height=600, width=1000, bg="Black")
f1.propagate(0)
f1.place(x=0, y=0)


img = Image.open("images/instalogobw.png")
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
    Button(f3, text="Hashtags", cursor="hand2", command=follow_htag, width=37, height=3).place(x=200, y=100)
    Button(f3, text="Username(s)", cursor="hand2", command=follow_uname, width=37, height = 3).place(x=200, y=250)
    Button(f3, text="Auto Follow-back", cursor="hand2", width=37, height=3).place(x=200, y=400)

def follow_htag(): #***
    delall()
    hashtags1 = StringVar()
    fol_heading = Label(f3, text="Follow", font=font1, bg="Black", fg="White")
    fol_heading.place(x=280, y=10)
    l12 = Label(f3, text='Enter hashtags:', font=font2, bg="Black", fg="White")
    l12.place(x=50, y=180)
    e12 = Entry(f3, textvariable=hashtags1, width=70, border=2)
    e12.place(x=240, y=185)
    fol_btn = Button(f3, text="Follow", cursor="hand2", border=4, width=10)
    fol_btn.place(x=390, y=400)
    Button(f3, text="Back", cursor="hand2", border=4, command=follow, width=10).place(x=185, y=400)

def dialogbox1(btn): #***
    #f3.filename contains the path of the csv/txt file along with the file name
    f3.filename = filedialog.askopenfilename(initialdir="C:", title="Select a csv/txt File", filetypes=(("csv files", "*.csv"),("txt files", "*.txt")))
    if len(f3.filename) > 0:
        filename = os.path.basename(f3.filename)
        l15 = Label(f3, text=filename, font=font2, bg="Black", fg="White")
        l15.place(x=280, y=260)
        btn['state'] = NORMAL

def follow_uname(): #***
    delall()
    fol_heading = Label(f3, text="Follow", font=font1, bg="Black", fg="White")
    fol_heading.place(x=280, y=10)
    l13 = Label(f3, text='Choose txt/csv file containing usernames:', font=font2, bg="Black", fg="White")
    l13.place(x=50, y=180)
    Button(f3, text="Browse files..", cursor="hand2", command=lambda: dialogbox1(fol_btn), border=4, width=10).place(x=520, y=182)
    l14 = Label(f3, text='Selected file name: ', font=font2, bg="Black", fg="White")
    l14.place(x=50, y=260)
    fol_btn = Button(f3, text="Follow", cursor="hand2", border=4, width=10, state=DISABLED)
    fol_btn.place(x=390, y=450)
    Button(f3, text="Back", cursor="hand2", border=4, command=follow, width=10).place(x=185, y=450)

def like_comment():
    delall()
    like_button['state'] = DISABLED
    follow_button['state'] = NORMAL
    msg_button['state'] = NORMAL
    l7 = Label(f3, text="Like/Comment based on:-", font=font1, fg="White", bg="Black")
    l7.place(x=170, y=0)
    Button(f3, text="Hashtags", cursor="hand2", command=lc_htags, width=37, height=3).place(x=200, y=150)
    Button(f3, text="Post ID", cursor="hand2", command=lc_postid, width=37, height=3).place(x=200, y=300)

def comment(val, y1): #***
    global l18, e18, comment1
    comment1 = StringVar()
    if val==1:
        l18 = Label(f3, text='Enter Comment:', font=font2, bg="Black", fg="White")
        l18.place(x=50, y=y1)
        e18 = Entry(f3, textvariable=comment1, width=70, border=2)
        e18.place(x=240, y=y1+5)
    elif val==2:
        l18.destroy()
        e18.destroy()

def lc_htags(): #***
    delall()
    hashtags2 = StringVar()
    rvar = IntVar()
    rvar.set(2)
    lc_heading = Label(f3, text="Like/Comment", font=font1, bg="Black", fg="White")
    lc_heading.place(x=240, y=10)
    l16 = Label(f3, text='Enter hashtags:', font=font2, bg="Black", fg="White")
    l16.place(x=50, y=180)
    e16 = Entry(f3, textvariable=hashtags2, width=70, border=2)
    e16.place(x=240, y=185)
    l17 = Label(f3, text='Do you want to comment?', font=font2, bg="Black", fg="White")
    l17.place(x=50, y=260)
    Radiobutton(f3, text="Yes", variable=rvar, value=1, command=lambda: comment(rvar.get(),360), cursor="hand2", fg='#89CFF0', bg='black', font=font2).place(x=350, y=255)
    Radiobutton(f3, text="No", variable=rvar, value=2, command=lambda: comment(rvar.get(),360), cursor="hand2", fg='#89CFF0', bg='black', font=font2).place(x=460, y=255)
    lc_btn = Button(f3, text="Like/Comment", cursor="hand2", border=4, width=14)
    lc_btn.place(x=390, y=450)
    Button(f3, text="Back", cursor="hand2", border=4, command=like_comment, width=10).place(x=185, y=450)

def lc_postid():
    delall()
    rvar = IntVar()
    rvar.set(2)
    lc_heading = Label(f3, text="Like/Comment", font=font1, bg="Black", fg="White")
    lc_heading.place(x=240, y=10)
    l19 = Label(f3, text='Choose txt/csv file containing PostIDs:', font=font2, bg="Black", fg="White")
    l19.place(x=50, y=180)
    Button(f3, text="Browse files..", cursor="hand2", command=lambda: dialogbox1(lc_btn), border=4, width=10).place(x=520, y=182)
    l20 = Label(f3, text='Selected file name: ', font=font2, bg="Black", fg="White")
    l20.place(x=50, y=260)
    l21 = Label(f3, text='Do you want to comment?', font=font2, bg="Black", fg="White")
    l21.place(x=50, y=340)
    Radiobutton(f3, text="Yes", variable=rvar, value=1, command=lambda: comment(rvar.get(),440), cursor="hand2", fg='#89CFF0', bg='black', font=font2).place(x=350, y=335)
    Radiobutton(f3, text="No", variable=rvar, value=2, command=lambda: comment(rvar.get(),440), cursor="hand2", fg='#89CFF0', bg='black', font=font2).place(x=460, y=335)
    lc_btn = Button(f3, text="Like/Comment", cursor="hand2", border=4, width=14, state=DISABLED)
    lc_btn.place(x=390, y=530)
    Button(f3, text="Back", cursor="hand2", border=4, command=like_comment, width=10).place(x=185, y=530)

def dialogbox2(m, btn):
    #f3.filename contains the path of the csv/txt file along with the file name
    f3.filename = filedialog.askopenfilename(initialdir="C:", title="Select a csv/txt File", filetypes=(("csv files", ".csv"),("txt files", ".txt")))
    if (len(f3.filename) > 0) and (len(m.get()) > 0):
        filename = os.path.basename(f3.filename)
        l11 = Label(f3, text=filename, font=font2, bg="Black", fg="White")
        l11.place(x=280, y=340)
        btn['state'] = NORMAL

def message():
    delall()
    msg_button['state'] = DISABLED
    like_button['state'] = NORMAL
    follow_button['state'] = NORMAL
    msg = StringVar()
    msg_heading = Label(f3, text="Message", font=font1, bg="Black", fg="White")
    msg_heading.place(x=280, y=10)
    inst = Label(f3, text="(First enter the message and then choose the file.)", font=font2, fg='white', bg='Black')
    inst.place(x=80, y=100)
    l8 = Label(f3, text='Enter the message:', font=font2, bg="Black", fg="White")
    l8.place(x=50, y=180)
    e8 = Entry(f3, textvariable=msg, width=60, border=2)
    e8.place(x=280, y=185)
    l9 = Label(f3, text="Choose txt/csv file having receivers' usernames:", font=font2, bg="Black", fg="White")
    l9.place(x=50, y=260)
    Button(f3, text="Browse files..", cursor="hand2", command=lambda:dialogbox2(msg,send_btn), border=4, width=10).place(x=590, y=260)
    l10 = Label(f3, text='Selected file name: ', font=font2, bg="Black", fg="White")
    l10.place(x=50, y=340)
    send_btn = Button(f3, text="Send", cursor="hand2", border=4, width=10, state=DISABLED)
    send_btn.place(x=300, y=450)

def secwin():
    if len(uname.get())==0 or len(password.get())==0:
        messagebox.showerror("Error", "Please enter details in all the fields.")
    else:

        login(uname.get(), password.get())

        if login.valid:

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

        else:
            messagebox.showerror("Error", "Username or password is incorrect.")




login_but = Image.open("images/login.png")
login_but = login_but.resize((100,40))
login_but = ImageTk.PhotoImage(login_but)

reset_but = Image.open("images/reset.png")
reset_but = reset_but.resize((100,40))
reset_but = ImageTk.PhotoImage(reset_but)

Button(f1, cursor="hand2", command=secwin, text="Login", image=login_but, bg="black", borderwidth=0, highlightthickness=0).place(x=430, y=350)
Button(f1, text="Reset", cursor="hand2", command=clear,image=reset_but , bg="black", borderwidth=0, highlightthickness=0).place(x=580, y=350)


win1.mainloop()
