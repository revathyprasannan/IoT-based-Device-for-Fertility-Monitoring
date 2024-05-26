from Tkinter import *
from newenc import *
from tkinter import messagebox
import sqlite3
top1=""
def logout():
    global top1
    top1.destroy()

def userhome(abd,tmp,usr):
    global top1
    print('Home page loaded',abd,tmp)
    top1=Toplevel()
    top1.geometry("550x150")
    top1.title("FORM")
    top1.minsize(550,460)
    top1.config(bg="#1AA5B5")
    lbl_Ln=Label(top1,text="Welcome "+usr,font="20",bg="white",width=20)
    lbl_Ln.place(x=190,y=50)
    lbl_fn=Label(top1,text="ABDOMEN SIZE",bg="white",width=15)
    lbl_fn.place(x=30,y=170)
    ent_fn=Entry(top1,font="12",width=15,bg="white")
    ent_fn.insert(END, abd)
    ent_fn.place(x=250,y=170)
    lbl_Ln=Label(top1,text="TEMPERATURE",bg="white",width=15)
    lbl_Ln.place(x=30,y=210)
    ent_ln=Entry(top1,font="12",width=15,bg="white")
    ent_ln.insert(END,str(tmp))
    ent_ln.place(x=250,y=210)

      
    top1.mainloop()
    

def sql_fetch(con,uid):

    cursorObj = con.cursor()

    cursorObj.execute('SELECT * FROM users where patientid="'+uid+'";')

    rows = cursorObj.fetchall()
    print(rows,len(rows))

    for row in rows:

        print(row[1])
        

        messagebox.showinfo("Welcome", "Welcome "+str(row[1]))
        userhome(row[3],row[4],row[1])



def checking(con):
    cipher=ent_.get()
    uid=decryptMessage(cipher)
    sql_fetch(con,uid)
con = sqlite3.connect('mydatabase.db')
top=Tk()

top.geometry('550x550')
top.title('Checks')
ent_=Entry(top,font="12",width=24,bg="white")
ent_.place(x=180,y=290)
btn1 = Button(top,bg="light green", text = 'CHECK',height=2,width=30,
             command = lambda:checking(con)) 
btn1.place(x = 180, y = 330)
    

top.mainloop()
