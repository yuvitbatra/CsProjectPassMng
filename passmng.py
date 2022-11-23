from tkinter import PhotoImage, Radiobutton, Tk, CENTER, Button, Label, Frame,Entry, IntVar,Text,INSERT,ttk
import pymysql
import random
import pyperclip
import smtplib


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("adityapassmng25346@gmail.com","cgntqxsrsbzsxdcq")

bgcol = "#282c34"
fgcol = "#f5fffa"
btncol = "#59626f"

window = Tk()
window.title("Password Manager")
icon = PhotoImage(file="lock.png")
window.iconphoto(False, icon)
window.geometry("400x400")
window.configure(bg="black")


#c.execute("create table passlog(sno int not null,softname varchar(100),password varchar(512),emailId varchar(200))")
# ALL FUNCTIONS
#global entry1

def showpass():
    conn = pymysql.connect(host="localhost",user="root",password="amity",port=3306,database="adityagautampassmng25346")
    c = conn.cursor()
    c.execute("select * from passlog where emailId = %s",(emailid))
    conn.commit()
    c.close()
    l=[]

    for i in c.fetchall():
        l.append(list(i))

    for i in l:
        decPass=""
        for k in i[2]:
            a = (chr(ord(k)-i[4]))
            decPass += a

        if i[1]==softwarename:
            entry.delete("1.0","end")
            entry.insert(INSERT,str(decPass))
    global softwarename1
    softwarename1=softwarename
    global entryy
    entryy=entry

def copypassz():
    conn = pymysql.connect(host="localhost",user="root",password="amity",port=3306,database="adityagautampassmng25346")
    c = conn.cursor()
    c.execute("select * from passlog where emailId = %s",(emailid))
    conn.commit()
    c.close()
    l=[]

    for i in c.fetchall():
        l.append(list(i))

    for i in l:
        decPass=""
        for k in i[2]:
            a = (chr(ord(k)-i[4]))
            decPass += a
        if i[1]==softwarename1:
            pyperclip.copy(decPass)
            entryy.delete("1.0","end")
            entryy.insert(INSERT,"Successfully Copied!")

def verified(e):
    global softwarename
    softwarename = combobox.get()
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = Frame(
        window,
        relief="raised",
        height=400,
        width=400,
        borderwidth=18,
        bg = bgcol,
        )
    labelframe.pack()
    label = Label (
        labelframe,
        text = "Display Password",
        font = ("High Tower Text",27),
        bg = bgcol,
        fg = fgcol
        )
    label.pack(padx=46,pady=17)

    showBtn = Button(labelframe,command = showpass,font=("Bahnschrift",12),text="Show Password",bg = bgcol,fg = fgcol,width=20,relief="raised",activebackground=bgcol)
    showBtn.pack(padx=10,pady=0)
    copypassBtn = Button(labelframe,font=("Bahnschrift",12),text="Copy Password",command=copypassz,bg = bgcol,fg = fgcol,width=20,relief="raised",activebackground=bgcol)
    copypassBtn.pack(padx=10,pady=0)
    global entry
    entry = Text(labelframe,font=("Bahnschrift",12),bg = btncol,relief="raised",borderwidth=4,width = 25)

    button = Button(labelframe, font = ("Bahnschrift",12), text= "Another password",bg=bgcol,width=20,fg=fgcol,relief="raised",command=display,activebackground=bgcol)
    button.pack(padx=10,pady=0)
    button = Button(labelframe, font = ("Bahnschrift",12), text= "Return To Main Menu",bg=bgcol,width=20,fg=fgcol,relief="raised",command=mainwin,activebackground=bgcol)
    button.pack(padx=10,pady=0)
    entry.pack(pady=20)
def display():
    conn = pymysql.connect(host="localhost",user="root",password="amity",port=3306,database="adityagautampassmng25346")
    c = conn.cursor()
    c.execute("select * from passlog where emailId = %s",(emailid))
    conn.commit()
    c.close()
    l=[]
    for i in c.fetchall():
        l.append(list(i))

    for widget in window.winfo_children():
        widget.destroy()

    labelframe = Frame(
                window,
                relief="raised",
                height=400,
                width=400,
                borderwidth=18,
                bg = bgcol,
                )
    labelframe.pack()
    label= Label(
                labelframe,
                font = ("Bahnschrift",20),
                text = "Choose The Software",
                bg = bgcol,
                fg = fgcol,
                wraplength=320
                )
    label.pack(padx=50,pady=60)


    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",fielbackground = btncol, background = btncol)
    global combobox
    combobox = ttk.Combobox(labelframe,value=[i[1] for i in l],background=btncol,justify=CENTER,font=("Bahnschrift",20),width=20)
    combobox.bind("<<ComboboxSelected>>",verified)
    combobox['state'] = 'readonly'
    combobox.pack(padx=20,pady=90,ipadx=3,ipady=3)

def verifyagain1():
    if str(entryz.get())==str(code):
        display()
    else:
        for widget in window.winfo_children():
            widget.destroy()
        labelframe = Frame(
        window,
        relief="raised",
        height=400,
        width=400,
        borderwidth=18,
        bg = bgcol,
        )
        labelframe.pack()
        label = Label (
        labelframe,
        text = "Error! Invalid Code!",
        wraplength=320,
        font = ("High Tower Text",20),
        bg = bgcol,
        fg = fgcol
        )
        label.pack(padx=75,pady=77)
        button = Button(labelframe, font=("Bahnschrift",12),text="Try Again",command=selected,bg=btncol)
        button.pack(padx=10,pady=70)
def deltxt1a(e):
    entryz.delete(0,"end")
def verifymaila():
    global code
    code=random.randint(10000,99999)
    server.sendmail("adityapassmng25346",emailid,"The code for verifying your email address for the Password Manager is "+str(code)+"\nDo not share this code with anyone\n\nAditya Gautam\n12D")
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = Frame(
        window,
        relief="raised",
        height=400,
        width=400,
        borderwidth=18,
        bg = bgcol,
        )
    labelframe.pack()
    label = Label (
        labelframe,
        text = "Enter the code sent to your mail",
        wraplength=320,
        font = ("High Tower Text",20),
        bg = bgcol,
        fg = fgcol
        )
    label.pack(padx=30,pady=37)

    global entryz
    entryz = Entry(
            labelframe,
            font = ("Bahnschrift",14),
            bg = btncol,
            borderwidth=4,
            width = 25,
            justify=CENTER,
            )
    entryz.pack(padx = 10,ipady=1,ipadx=1,pady=30)
    entryz.insert(0,"Enter the code...")
    entryz.bind("<FocusIn>",deltxt1a)
    btn = Button(labelframe,font=("Bahnschrift",12),bg=btncol,text = "Submit",justify=CENTER,activebackground=btncol,width=7,command = verifyagain1)
    btn.pack(padx=20,pady=46)
def deltxta(e):
    entry.delete(0,"end")
def selected():
        for widget in window.winfo_children():
            widget.destroy()
        labelframe = Frame(
        window,
        relief="raised",
        height=400,
        width=400,
        borderwidth=18,
        bg = bgcol,
        )
        labelframe.pack()
        label = Label (
        labelframe,
        text = "Verify Yourself",
        font = ("High Tower Text",30),
        bg = bgcol,
        fg = fgcol
        )
        label.pack(padx=53,pady=47)

        loginBtn = Button(
        labelframe,
        font = ("Bahnschrift",14),
        text = "Login",
        bg = btncol,
        width = 20,
        activebackground= btncol,
        command = verifymaila
        )
        label = Label(
        labelframe,
        bg = bgcol
        )
        label.pack(pady=20)
        label = Label(
        labelframe,
        bg = bgcol
        )
        loginBtn.pack(padx=10,pady=50)
        label.pack(pady=15)




def delpass():
    conn = pymysql.connect(host="localhost",user="root",password="amity",port=3306,database="adityagautampassmng25346")
    c = conn.cursor()
    c.execute("select * from passlog where emailId = %s",(emailid))
    conn.commit()
    c.close()
    l=[]
    for i in c.fetchall():
        l.append(list(i))
    global curpass1
    curpass1 = entryb1.get()
    decpassL=[]
    for i in l:
        decPass=""
        for k in i[2]:
            a = (chr(ord(k)-i[4]))
            decPass += a
        decpassL.append(decPass)
    #softnameconf1 is the name of the software for del Button
    #curpass1 is the current password for del button
    if softnameconf1 not in [i[1] for i in l] or curpass1 not in decpassL:
        for widget in window.winfo_children():
            widget.destroy()
        labelframe = Frame(
        window,
        relief="raised",
        height=400,
        width=400,
        borderwidth=18,
        bg = bgcol,
        )
        labelframe.pack()

        label=Label(
            labelframe,
            font = ("Bahnschrift",15),
            text= "Invalid Operation, Try again!",
            bg=bgcol,
            fg=fgcol
            )
        label.pack(padx=10,pady=50)
        label = Label(
                labelframe,
                text="",
                bg = bgcol
                )
        label.pack(pady=20)
        tryBtn = Button(
            labelframe,
            font = ("Bahnschrift",14),
            text = "Try Again",
            relief="raised",
            bg = bgcol,
            fg=fgcol,
            command = update1,
            width = 50
            )
        tryBtn.pack(padx=10,pady=10)
        mainmenuBtn = Button(
            labelframe,
            font = ("Bahnschrift",14),
            relief="raised",
            bg = bgcol,
            fg=fgcol,
            text = "Main Menu",
            width = 50,
            command = mainwin
            )
        mainmenuBtn.pack(padx=10,pady=15)
        label.pack(padx=10,pady=30)
        label = Label(labelframe,bg=bgcol)
        label.pack(pady=20)
    else:
        conn = pymysql.connect(host="localhost",user="root",password="amity",port=3306,database="adityagautampassmng25346")
        c = conn.cursor()
        c.execute("delete from passlog where softname = %s and emailId = %s",(softnameconf1,emailid))
        conn.commit()
        c.close()
        for widget in window.winfo_children():
            widget.destroy()
        labelframe = Frame(
                window,
                relief="raised",
                height=400,
                width=400,
                borderwidth=18,
                bg = bgcol,
                )
        labelframe.pack()
        label= Label(
                labelframe,
                font = ("Bahnschrift",20),
                text = "Password Deleted Successfully!",
                bg = bgcol,
                fg = fgcol,
                wraplength=320
                )
        label.pack(padx=65,pady=60)
        mainmenuBtn = Button(
        labelframe,
        font = ("Bahnschrift",12),
        relief="raised",
        bg = btncol,
        text = "Return To Main Menu",
        width = 50,
        command = mainwin
        )
        mainmenuBtn.pack(padx=10,pady=70)

def confpass1():
        global softnameconf1
        softnameconf1 = entrya1.get()
        for widget in window.winfo_children():
            widget.destroy()
        labelframe = Frame(
                window,
                relief="raised",
                height=400,
                width=400,
                borderwidth=18,
                bg = bgcol,
                )
        labelframe.pack()
        label = Label(
                labelframe,
                font = ("Bahnschrift",18),
                text = "Enter the current password for the software",
                wraplength = 350,
                bg = bgcol,
                fg = fgcol
                )
        label.pack(padx=15,pady=45)
        global entryb1
        entryb1 = Entry(
                labelframe,
                font = ("Bahnschrift",15),
                bg = btncol,
                width=20,
                justify=CENTER,
                show="*"
                )
        entryb1.pack(padx=10,pady=41,ipady=3)
        sbmtBtn = Button(
                labelframe,
                font = ("Bahnschrift",12),
                text = "Submit",
                bg = btncol,
                command = delpass
                )
        sbmtBtn.pack(padx=10,pady=30,ipadx=1,ipady=1)
def update1():
        for widget in window.winfo_children():
            widget.destroy()
        labelframe = Frame(
                window,
                relief="raised",
                height=400,
                width=400,
                borderwidth=18,
                bg = bgcol,
                )
        labelframe.pack()
        label = Label(
                labelframe,
                font = ("Bahnschrift",18),
                text = "Enter the name of the software for which the password needs to be deleted",
                wraplength = 350,
                bg = bgcol,
                fg = fgcol
                )
        label.pack(padx=15,pady=30)
        global entrya1
        entrya1 = Entry(
                labelframe,
                font = ("Bahnschrift",15),
                bg = btncol,
                width=20,
                justify=CENTER
                )
        entrya1.pack(padx=10,pady=41,ipady=3)
        sbmtBtn = Button(
                labelframe,
                font = ("Bahnschrift",12),
                text = "Submit",
                bg = btncol,
                command = confpass1
                )
        sbmtBtn.pack(padx=10,pady=30,ipadx=1,ipady=1)

def tryagain():
        for widget in window.winfo_children():
            widget.destroy()
        labelframe = Frame(
        window,
        relief="raised",
        height=400,
        width=400,
        borderwidth=18,
        bg = bgcol,
        )
        labelframe.pack()

        label=Label(
            labelframe,
            font = ("Bahnschrift",15),
            text= "Invalid Operation, Try again!",
            bg=bgcol,
            fg=fgcol
            )
        label.pack(padx=10,pady=50)
        label = Label(
                labelframe,
                text="",
                bg = bgcol
                )
        label.pack(pady=20)
        tryBtn = Button(
            labelframe,
            font = ("Bahnschrift",14),
            text = "Try Again",
            relief="raised",
            bg = bgcol,
            fg=fgcol,
            command = update,
            width = 50
            )
        tryBtn.pack(padx=10,pady=10)
        mainmenuBtn = Button(
            labelframe,
            font = ("Bahnschrift",14),
            relief="raised",
            bg = bgcol,
            fg=fgcol,
            text = "Main Menu",
            width = 50,
            command = mainwin
            )
        mainmenuBtn.pack(padx=10,pady=15)
        label.pack(padx=10,pady=30)
        label = Label(labelframe,bg=bgcol)
        label.pack(pady=20)
def chkpass():
    global newpassconf2
    newpassconf2 = entryd.get()
    conn = pymysql.connect(host="localhost",user="root",password="amity",port=3306,database="adityagautampassmng25346")
    c = conn.cursor()
    c.execute("select * from passlog where emailId = %s",(emailid))
    conn.commit()
    c.close()
    l=[]
    for i in c.fetchall():
        l.append(list(i))

    decpassL=[]
    for i in l:
        decPass=""
        for k in i[2]:
            a = (chr(ord(k)-i[4]))
            decPass += a
        decpassL.append(decPass)
    #softnameconf is var for the software name for the update mode
    #curpassconf is var for the current password
    #newpassconf is var for the new password
    #newpassconf2 is var for the conformation password
    if softnameconf not in [i[1] for i in l] or softnameconf == "" or curpassconf not in [i for i in decpassL] or curpassconf == "" or newpassconf!=newpassconf2:
        tryagain()
    else:
        for i in l:
            if i[1]==softnameconf:
                decPass=""
                for k in i[2]:
                    a=chr(ord(k)-i[4])
                    decPass+=a
                if decPass==curpassconf:
                    if newpassconf2==newpassconf:
                        deviation = random.randint(50,500)
                        encPass=""
                        for i in newpassconf:
                            j=chr(ord(i)+deviation)
                            encPass +=j
                        conn = pymysql.connect(host="localhost",user="root",password="amity",port=3306,database="adityagautampassmng25346")
                        c = conn.cursor()
                        c.execute("update passlog set password = %s,deviation = %s  where softname = %s and emailId = %s",(encPass,deviation,softnameconf,emailid))
                        conn.commit()
                        c.close()
                        for widget in window.winfo_children():
                            widget.destroy()
                        labelframe = Frame(
                                window,
                                relief="raised",
                                height=400,
                                width=400,
                                borderwidth=18,
                                bg = bgcol,
                                )
                        labelframe.pack()
                        label= Label(
                                labelframe,
                                font = ("Bahnschrift",20),
                                text = "Password Updated Successfully!",
                                bg = bgcol,
                                fg = fgcol,
                                wraplength=320
                                )
                        label.pack(padx=65,pady=60)
                        mainmenuBtn = Button(
                        labelframe,
                        font = ("Bahnschrift",12),
                        relief="raised",
                        bg = btncol,
                        text = "Return To Main Menu",
                        width = 50,
                        command = mainwin
                        )
                        mainmenuBtn.pack(padx=10,pady=70)
                        break

def updpass2():
    global newpassconf
    newpassconf = entryc.get()
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = Frame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            )
    labelframe.pack()
    label = Label(
            labelframe,
            font = ("Bahnschrift",18),
            text = "Confirm the password again",
            wraplength = 350,
            bg = bgcol,
            fg = fgcol
            )
    label.pack(padx=30,pady=62)
    global entryd
    entryd = Entry(
            labelframe,
            font = ("Bahnschrift",15),
            bg = btncol,
            width=20,
            justify=CENTER,
            show="*"
            )
    entryd.pack(padx=10,pady=40,ipady=3)
    sbmtBtn = Button(
            labelframe,
            font = ("Bahnschrift",12),
            text = "Submit",
            bg = btncol,
            command = chkpass
            )
    sbmtBtn.pack(padx=10,pady=30,ipadx=1,ipady=1)

def updpass():
    global curpassconf
    curpassconf = entryb.get()
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = Frame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            )
    labelframe.pack()
    label = Label(
            labelframe,
            font = ("Bahnschrift",18),
            text = "Enter the new password",
            wraplength = 350,
            bg = bgcol,
            fg = fgcol
            )
    label.pack(padx=53,pady=55)
    global entryc

    entryc = Entry(
            labelframe,
            font = ("Bahnschrift",15),
            bg = btncol,
            width=20,
            justify=CENTER,
            show="*"
            )
    entryc.pack(padx=10,pady=49,ipady=3)
    sbmtBtn = Button(
            labelframe,
            font = ("Bahnschrift",12),
            text = "Submit",
            bg = btncol,
            command = updpass2
            )
    sbmtBtn.pack(padx=10,pady=26,ipadx=1,ipady=1)




def confpass():
    global softnameconf
    softnameconf = entrya.get()
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = Frame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            )
    labelframe.pack()
    label = Label(
            labelframe,
            font = ("Bahnschrift",18),
            text = "Enter the current password for the software",
            wraplength = 350,
            bg = bgcol,
            fg = fgcol
            )
    label.pack(padx=15,pady=45)
    global entryb
    entryb = Entry(
            labelframe,
            font = ("Bahnschrift",15),
            bg = btncol,
            width=20,
            justify=CENTER,
            show="*"
            )
    entryb.pack(padx=10,pady=41,ipady=3)
    sbmtBtn = Button(
            labelframe,
            font = ("Bahnschrift",12),
            text = "Submit",
            bg = btncol,
            command = updpass
            )
    sbmtBtn.pack(padx=10,pady=30,ipadx=1,ipady=1)


def update():
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = Frame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            )
    labelframe.pack()
    label = Label(
            labelframe,
            font = ("Bahnschrift",18),
            text = "Enter the name of the software for which the password needs to be updated",
            wraplength = 350,
            bg = bgcol,
            fg = fgcol
            )
    label.pack(padx=15,pady=30)
    global entrya
    entrya = Entry(
            labelframe,
            font = ("Bahnschrift",15),
            bg = btncol,
            width=20,
            justify=CENTER
            )
    entrya.pack(padx=10,pady=41,ipady=3)
    sbmtBtn = Button(
            labelframe,
            font = ("Bahnschrift",12),
            text = "Submit",
            bg = btncol,
            command = confpass
            )
    sbmtBtn.pack(padx=10,pady=30,ipadx=1,ipady=1)

def mainwin():
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = Frame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            )
    labelframe.pack()
    label = Label (
        labelframe,
        text = "PASSWORD MANAGER",
        font = ("High Tower Text",20),
        bg = bgcol,
        fg = fgcol
        )
    label.pack(padx=22,pady=15)

    createBtn = Button(
        labelframe,
        text = "Create",
        font = ("Bahnschrift",12),
        relief="raised",
        command = createbtn,
        bg = btncol,
        activebackground=btncol,
        width = 20,
        height = 1
        )
    updateBtn = Button(
        labelframe,
        text = "Update",
        font = ("Bahnschrift",12),
        relief="raised",
        bg = btncol,
        activebackground=btncol,
        width = 20,
        command = update
        )
    deleteBtn = Button(
        labelframe,
        text = "Delete",
        font = ("Bahnschrift",12),
        relief="raised",
        bg = btncol,
        activebackground=btncol,
        width = 20,
        command = update1
        )
    displayBtn = Button(
        labelframe,
        text = "Display",
        font = ("Bahnschrift",12),
        relief="raised",
        bg = btncol,
        activebackground=btncol,
        width = 20,
        command = selected
        )
    exitBtn = Button(
        labelframe,
        text = "  Exit  ",
        font = ("Bahnschrift",10),
        relief="raised",
        bg = bgcol,
        activebackground=bgcol,
        fg = fgcol,
        activeforeground= fgcol,
        command = exitfunc,
        width = 5,
        )
    createBtn.pack(padx=10,pady=10)
    updateBtn.pack(padx=10,pady=10)
    deleteBtn.pack(padx=10,pady=10)
    displayBtn.pack(padx=10,pady=10)
    exitBtn.pack(padx=10,pady=15)

    label = Label(
            labelframe,
            text="",
            bg = bgcol
            )
    label.pack(padx=5,pady=5)

def copy():
    pyperclip.copy(passw)

def finalLogCopy():
    deviation = random.randint(50,500)
    encPass=""
    for i in passw:
        j=chr(ord(i)+deviation)
        encPass +=j
    l=[]
    conn = pymysql.connect(host="localhost",user="root",password="amity",port=3306,database="adityagautampassmng25346")
    c = conn.cursor()
    c.execute("select * from passlog where emailId = %s",(emailid))
    conn.commit()
    for i in c.fetchall():
        l.append(list(i))
    c.execute("insert into passlog(sno, softname,password,emailId,deviation) values(%s,%s,%s,%s,%s)",(len(l)+1,softname,encPass,emailid,deviation))
    conn.commit()
    c.close()
    r1['state']='disabled'

def logOrCopy():
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = Frame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            )
    labelframe.pack()
    label = Label(
            labelframe,
            text = "Choose",
            font = ("Bahnschrift",18),
            bg = bgcol,
            fg = fgcol
            )
    label.pack(padx=140,pady=40)
    label = Label(
            labelframe,
            text="\n",
            bg=bgcol
            )
    label.pack(pady=10)
    global r1
    r1 = Button(
            labelframe,
            bg = bgcol,
            fg = fgcol,
            activebackground=bgcol,
            activeforeground=fgcol,
            font = ("Bahnschrift",12),
            text = "Log password",
            width = 20,
            command = finalLogCopy
            )
    r2 = Button(
            labelframe,
            bg = bgcol,
            fg = fgcol,
            activeforeground=fgcol,
            activebackground=bgcol,
            text = "Copy Password",
            font = ("Bahnschrift",12),
            width = 20,
            command = copy
            )
    r1.pack(padx=20,pady=10)
    r2.pack(padx=20,pady=10)
    mainmenu = Button(
            labelframe,
            font=("Bahnschrift",10),
            text = "Return to main menu",
            bg = btncol,
            command = mainwin
            )
    mainmenu.pack(padx=10,pady=30,ipadx=1,ipady=1)

def notrandpass():
    global passw
    passw = entry1.get()
    logOrCopy()
def randompass():
    global passw
    passw=""
    for i in range(int(entry.get())):
        passw+=chr(random.randint(33,126))
    logOrCopy()


def genpass_radio():
    if var.get()==1:
        for widget in window.winfo_children():
            widget.destroy()
        labelframe = Frame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            )
        labelframe.pack()
        label = Label(
            labelframe,
            text = "Enter the length of password",
            font = ("Bahnschrift",17),
            bg = bgcol,
            fg = fgcol,
            wraplength=350
            )
        label.pack(padx=30,pady=40)
        global entry
        entry = Entry(
            labelframe,
            font = ("Bahnschrift",15),
            bg = btncol,
            width = 20,
            justify=CENTER
            )
        submitBtnRand = Button(
                labelframe,
                text="Submit",
                font= ("Bahnschrift",13),
                bg = btncol,
                activebackground = btncol,
                command = randompass,
                width = 7
                )
        entry.pack(padx=10,pady=50,ipady=3)
        submitBtnRand.pack(padx=10,pady=40,ipadx=1,ipady=1)

    elif var.get()==2:
        for widget in window.winfo_children():
            widget.destroy()
        labelframe = Frame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            )
        labelframe.pack()
        label = Label(
            labelframe,
            text = "Enter your password",
            font = ("Bahnschrift",17),
            bg = bgcol,
            fg = fgcol
            )
        label.pack(padx=70,pady=50)

        global entry1
        entry1 = Entry(
                labelframe,
                font = ("Bahnschrift",15),
                bg = btncol,
                show="*",
                width = 20,
                justify=CENTER
                )
        entry1.pack(padx=10,pady=50,ipadx=1,ipady=3)
        submitBtnUr = Button(
                labelframe,
                font = ("Bahnschrift",13),
                text = "Submit",
                bg = btncol,
                activebackground= btncol,
                command = notrandpass
                )
        submitBtnUr.pack(padx=10,pady=30,ipadx=1,ipady=1)


def create_submitBtn():   # this function takes software name as input and asks user if they want to generate a random pass
    global softname
    softname = entry2.get()
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = Frame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            )

    labelframe.pack()
    label = Label(
            labelframe,
            text = "Do you want to generate a random password? ",
            font = ("Bahnschrift",17),
            bg = bgcol,
            fg = fgcol,
            wraplength=350,
            justify=CENTER
            )
    label.pack(padx=45,pady=40)
    label = Label(
        labelframe,
        text="",
        bg = bgcol
        )
    label.pack(padx=5,pady=5)
    global var
    var = IntVar()
    r1 = Radiobutton(
            labelframe,
            text = " Yes ",
            font = ("Bahnschrift",12),
            variable = var,
            value = 1,
            relief="groove",
            command = genpass_radio,
            bg = btncol,
            activebackground=btncol,
            indicatoron=False,
            width = 10
            )
    r2 = Radiobutton(
            labelframe,
            text = " No ",
            font = ("Bahnschrift",12),
            variable = var,
            relief="groove",
            value = 2,
            command = genpass_radio,
            bg = btncol,
            activebackground= btncol,
            indicatoron=False,
            width=10
            )
    r1.pack(padx=10,pady=10)
    r2.pack(padx=10,pady=10)

    label = Label(
        labelframe,
        text="",
        bg = bgcol
        )
    label.pack(padx=5,pady=50)

def createbtn():
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = Frame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            )
    labelframe.pack()
    label = Label(
            labelframe,
            text = "Enter the name of the software",
            font = ("Bahnschrift",17),
            bg = bgcol,
            fg = fgcol,
            wraplength=350
            )
    label.pack(padx=20,pady=40)
    global entry2
    entry2 = Entry(
            labelframe,
            font = ("Bahnschrift",15),
            bg = btncol,
            width = 25,
            justify= CENTER,
            relief="groove"
            )
    entry2.pack(padx=70,pady=60,ipady=3)
    submitBtn = Button(
            labelframe,
            text = "Submit",
            font = ("Bahnschrift",13),
            relief="raised",
            bg = btncol,
            activebackground=btncol,
            command = create_submitBtn,
            width = 7,
            )
    submitBtn.pack(padx=10,pady=30,ipadx=1,ipady=1)

def exitfunc():
    window.destroy()

# FIRST PAGE (MAIN PAGE)

#CREATE PAGE
#login page
def loginpage():
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = Frame(
        window,
        relief="raised",
        height=400,
        width=400,
        borderwidth=18,
        bg = bgcol,
        )
    labelframe.pack()
    label = Label (
        labelframe,
        text = "Account Login",
        font = ("High Tower Text",30),
        bg = bgcol,
        fg = fgcol
        )
    label.pack(padx=53,pady=47)

    loginBtn = Button(
        labelframe,
        font = ("Bahnschrift",14),
        text = "Login",
        bg = btncol,
        width = 20,
        activebackground= btncol,
        command = login
        )
    label = Label(
        labelframe,
        bg = bgcol
        )
    label.pack(pady=20)
    label = Label(
        labelframe,
        bg = bgcol
        )
    loginBtn.pack(padx=10,pady=50)
    label.pack(pady=15)

def verifyagain():
    if str(entryz.get())==str(code):
        mainwin()
    else:
        for widget in window.winfo_children():
            widget.destroy()
        labelframe = Frame(
        window,
        relief="raised",
        height=400,
        width=400,
        borderwidth=18,
        bg = bgcol,
        )
        labelframe.pack()
        label = Label (
        labelframe,
        text = "Error! Invalid Code!",
        wraplength=320,
        font = ("High Tower Text",20),
        bg = bgcol,
        fg = fgcol
        )
        label.pack(padx=75,pady=77)
        button = Button(labelframe, font=("Bahnschrift",12),text="Try Again",command=loginpage,bg=btncol)
        button.pack(padx=10,pady=70)

def exitloop():
    window.destroy()
def mailerror():
    for widget in window.winfo_children():
            widget.destroy()
    labelframe = Frame(
        window,
        relief="raised",
        height=400,
        width=400,
        borderwidth=18,
        bg = bgcol,
        )
    labelframe.pack()
    label = Label (
        labelframe,
        text = "Invalid Mail ID!",
        wraplength=320,
        font = ("High Tower Text",20),
        bg = bgcol,
        fg = fgcol
        )
    label.pack(padx=90,pady=67)
    btn = Button(
        labelframe,
        font=("Bahnschrift",13),
        bg = bgcol,
        fg = fgcol,
        text = "Try Again",
        width=20,
        activebackground=bgcol,
        command=login
        )
    btn.pack(padx=10,pady=10)
    exitbtn2 = Button(
        labelframe,
        font = ("Bahnschrift",13),
        bg = bgcol,
        fg = fgcol,
        text="Exit",
        width=20,
        activebackground=bgcol,
        command=exitloop
        )
    exitbtn2.pack(padx=10,pady=10)
    label=Label(
            labelframe,
            bg=bgcol
            )
    label.pack(pady=100)

def deltxt1(e):
    entryz.delete(0,"end")
def verifymail():
    global emailid
    emailid = entry.get()
    global code
    code=random.randint(10000,99999)
    try:
        server.sendmail("adityapassmng25346",emailid,"The code for verifying your email address for the Password Manager is "+str(code)+"\nDo not share this code with anyone\n\nAditya Gautam\n12D")

        for widget in window.winfo_children():
            widget.destroy()
        labelframe = Frame(
            window,
            relief="raised",
            height=400,
            width=400,
            borderwidth=18,
            bg = bgcol,
            )
        labelframe.pack()
        label = Label (
            labelframe,
            text = "Enter the code sent to your mail",
            wraplength=320,
            font = ("High Tower Text",20),
            bg = bgcol,
            fg = fgcol
            )
        label.pack(padx=30,pady=37)

        global entryz
        entryz = Entry(
                labelframe,
                font = ("Bahnschrift",14),
                bg = btncol,
                borderwidth=4,
                width = 25,
                justify=CENTER,
                )
        entryz.pack(padx = 10,ipady=1,ipadx=1,pady=30)
        entryz.insert(0,"Enter the code...")
        entryz.bind("<FocusIn>",deltxt1)
        btn = Button(labelframe,font=("Bahnschrift",12),bg=btncol,text = "Submit",justify=CENTER,activebackground=btncol,width=7,command = verifyagain)
        btn.pack(padx=20,pady=46)

    except:
        mailerror()

def deltxt(e):
    entry.delete(0,"end")
def login():
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = Frame(
        window,
        relief="raised",
        height=400,
        width=400,
        borderwidth=18,
        bg = bgcol,
        )
    labelframe.pack()
    label = Label (
        labelframe,
        text = "Login",
        font = ("High Tower Text",20),
        bg = bgcol,
        fg = fgcol
        )
    label.pack(padx=150,pady=37)
    global entry
    entry = Entry(
            labelframe,
            font = ("Bahnschrift",14),
            bg = btncol,
            borderwidth=4,
            width = 25,
            justify=CENTER
            )
    entry.pack(padx = 10, pady = 60,ipady=1,ipadx=1)
    entry.insert(0,"Enter Your Email Address...")
    entry.bind("<FocusIn>",deltxt)
    btn = Button(labelframe,font=("Bahnschrift",12),bg=btncol,text = "Submit",justify=CENTER,activebackground=btncol,width=7,command = verifymail)
    btn.pack(padx=20,pady=32)


labelframe = Frame(
        window,
        relief="raised",
        height=400,
        width=400,
        borderwidth=18,
        bg = bgcol,
        )
labelframe.pack()
label = Label (
        labelframe,
        text = "Account Login",
        font = ("High Tower Text",30),
        bg = bgcol,
        fg = fgcol
        )
label.pack(padx=53,pady=47)

loginBtn = Button(
        labelframe,
        font = ("Bahnschrift",14),
        text = "Login",
        bg = btncol,
        width = 20,
        activebackground= btncol,
        command = login
        )
label = Label(
        labelframe,
        bg = bgcol
        )
label.pack(pady=20)
label = Label(
        labelframe,
        bg = bgcol
        )
loginBtn.pack(padx=10,pady=50)
label.pack(pady=15)

window.mainloop()
