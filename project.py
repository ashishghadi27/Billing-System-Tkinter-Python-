import datetime
from tkinter import *
import MySQLdb
import tkinter.messagebox

conn = MySQLdb.connect('localhost', 'root', '27DEC1998', 'billing')
c = conn.cursor()
a = list()
qty = list()
time = datetime.datetime.now()
timer = str(time.hour)+"hrs : "+str(time.minute)+"mins : "+str(time.second)+" secs"
dateset = str(str(time.day) + '/' + str(time.month) + '/' + str(time.year))

def exit():
    tkinter.messagebox.showinfo("Exit", "Thankyou for shopping")
    root.withdraw()

def add_button():
    listcanvas.delete(ALL)
    a.clear()
    qty.clear()
    count = 0
    if var1.get() == 1:
        a.append(101)
        qty.append(spin1.get())
        count = count + 1
    if var2.get() == 1:
        a.append(102)
        qty.append(spin2.get())
        count = count + 1
    if var3.get() == 1:
        a.append(103)
        qty.append(spin3.get())
        count = count + 1
    if var4.get() == 1:
        a.append(104)
        qty.append(spin4.get())
        count = count + 1
    if var5.get() == 1:
        a.append(105)
        qty.append(spin5.get())
        count = count + 1
    if var6.get() == 1:
        a.append(106)
        qty.append(spin6.get())
        count = count + 1
    if var7.get() == 1:
        a.append(107)
        qty.append(spin7.get())
        count = count + 1
    if var8.get() == 1:
        a.append(108)
        qty.append(spin8.get())
        count = count + 1
    if var9.get() == 1:
        a.append(109)
        qty.append(spin9.get())
        count = count + 1
    if var10.get() == 1:
        a.append(110)
        qty.append(spin10.get())
        count = count + 1
    if var11.get() == 1:
        a.append(111)
        qty.append(spin11.get())
        count = count + 1
    if var12.get() == 1:
        a.append(112)
        qty.append(spin12.get())
        count = count + 1
    if var13.get() == 1:
        a.append(113)
        qty.append(spin13.get())
        count = count + 1
    if var14.get() == 1:
        a.append(114)
        qty.append(spin14.get())
        count = count + 1
    if var15.get() == 1:
        a.append(115)
        qty.append(spin15.get())
        count = count + 1

    print(a)
    print(str(tuple(int(i) for i in a)))
    try:
        if (len(a) > 1):
            query = "SELECT code, item FROM billing_table where code IN %s" % str(tuple(int(i) for i in a))
        else:
            query = "SELECT code, item FROM billing_table where code = %s" % str(a[0])
        c.execute(query)
        rows = c.fetchall()
        rows = sorted(rows)
        row1 = Text()
        ay = 0.01

        for k in rows:
            movex = 0.1

            for i in range(0, 2):
                row1 = Text(listcanvas, width=12, bd=0, font=('Calibri', 15), fg="#000000", bg="#FFFFFF", wrap=NONE)
                row1.place(relx=movex, rely=ay)
                row1.insert(END, k[i])
                movex = movex + .3

            ay = ay + 0.07

        ay = 0.01

        for i in qty:
            row1 = Text(listcanvas, width=12, bd=0, font=('Calibri', 15), fg="#000000", bg="#FFFFFF", wrap=NONE)
            row1.place(relx=.7, rely=ay)
            row1.insert(END, i)

            ay = ay + 0.07

        '''scrollbar = Scrollbar(root, orient=VERTICAL, command=row1.yview)
        row1.configure(yscrollcommand=scrollbar.set)
        print("here")
        scrollbar.pack(side=RIGHT, fill=Y)'''

    except:
        tkinter.messagebox.showinfo("Items Selected", "NO ITEMS SELECTED ")

def view():
    rootdev = Tk()
    rootdev.config(bg="white")
    rootdev.geometry("1000x800+0+0")
    bill_number = text3.get()
    if bill_number == "":
        bill_number = "Please Enter Bill No"
    bill_label = Label(rootdev, text='Bill No: '+bill_number,font=('arial',14,'bold'), bg='#FFFFFF')
    bill_label.place(relx=.05, rely = 0.02)

    date_label = Label(rootdev, text='Date : ' + dateset, font=('arial', 14, 'bold'), bg='#FFFFFF')
    date_label.place(relx=.45, rely=0.02)

    time_label = Label(rootdev, text='Time:   ' + timer, font=('arial', 14, 'bold'), bg='#FFFFFF')
    time_label.place(relx=.7, rely=0.02)

    top_label = Label(rootdev,font=('arial',14,'bold'),text='CODE',bg='white')
    top_label.place(relx=0.02, rely=.1)

    top_label1 = Label(rootdev, font=('arial', 14, 'bold'),
                      text='ITEMS',
                      bg='white')
    top_label1.place(relx=0.27, rely=.1)

    top_label2 = Label(rootdev, font=('arial', 14, 'bold'),
                      text='COST',
                      bg='white')
    top_label2.place(relx=0.52, rely=.1)

    top_label3 = Label(rootdev, font=('arial', 14, 'bold'),
                      text='QTY',
                      bg='white')
    top_label3.place(relx=0.77, rely=.1)

    bottom_canvas = Canvas(rootdev, height=700,width=1000, bg="#FFFFFF")
    bottom_canvas.place(relx=0, rely=.15)


    if len(a) > 1:
        query = "SELECT * FROM billing_table where code IN %s" % str(tuple(int(i) for i in a))
    else:
        query = "SELECT * FROM billing_table where code = %s" % str(a[0])
    c.execute(query)
    rows = c.fetchall()
    rows = sorted(rows)

    ay = 0.0
    q = 0
    total = 0
    for k in rows:
        movex = 0.02

        for i in range(0, 3):
            row1 = Text(bottom_canvas, width=12, bd=0, font=('Calibri', 15), fg="#000000", bg="#FFFFFF")
            row1.place(relx=movex, rely=ay)
            if i == 2:
                row1.insert(END, str(int(k[i])*int(qty[q])))
                total = total + int(k[i])*int(qty[q])
            else:
                row1.insert(END, k[i])
            movex = movex + .25

        ay = ay + 0.07
        q = q + 1

    ay = .0
    for i in qty:
        row1 = Text(bottom_canvas, width=12, bd=0, font=('Calibri', 15), fg="#000000", bg="#FFFFFF")
        row1.place(relx=.8, rely=ay)
        row1.insert(END, i)

        ay = ay + 0.07

    label_total = Label(bottom_canvas, font=('arial',15,'bold'), text="TOTAL = "+str(total), bg="white")
    label_total.place(relx=.2, rely=ay+0.07)

    def print():
        tkinter.messagebox.showinfo("Bill Status","Bill Printed")

    print_button = Button(rootdev, text="Print", font=('arial', 14, 'bold'), command=print)
    print_button.place(relx=.9, rely = .1)

    rootdev.mainloop()

def reset():
    listcanvas.delete(ALL)
    ay = 0.01

    for k in range(0,2):
        movex = 0.1

        for i in range(0, 2):
            row1 = Text(listcanvas, width=12, bd=0, font=('Calibri', 15), fg="#ffffff", bg="#FFFFFF")
            row1.place(relx=movex, rely=ay)
            row1.insert(END, "root")
            movex = movex + .3

        ay = ay + 0.07

    ay = 0.01

    for i in range(0,2):
        row1 = Text(listcanvas, width=12, bd=0, font=('Calibri', 15), fg="#ffffff", bg="#FFFFFF")
        row1.place(relx=.7, rely=ay)
        row1.insert(END, "1")

        ay = ay + 0.07
    '''text = Text(listcanvas,  width=10, height=10)
    text.insert(END, "Root")
    text.place(relx=0, rely=0)'''

    a.clear()
    qty.clear()
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    spin1.delete(0,"end")
    spin2.delete(0, "end")
    spin3.delete(0, "end")
    spin4.delete(0, "end")
    spin5.delete(0, "end")
    spin6.delete(0, "end")
    spin7.delete(0, "end")
    spin8.delete(0, "end")
    spin9.delete(0, "end")
    spin10.delete(0, "end")
    spin11.delete(0, "end")
    spin12.delete(0, "end")
    spin13.delete(0, "end")
    spin14.delete(0, "end")
    spin15.delete(0, "end")


root = Tk()
root.geometry("1250x650+0+0")
root.title("Billing System")

Top1 = Frame(root,width=1250,height=60,bd=8,relief="raise")
Top1.pack(side=TOP)
Label1=Label(Top1,font=('arial',20,'bold'),text='   BILLING SYSTEM   ',fg='black')
Label1.place(x=500,y=5)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()

Label1=Label(font=('arial',15,'bold'),text='TIME:')
Label1.place(x=950,y=80)
text1=Entry(font=('arial',10,'bold'))
text1.place(x=1015,y=82,height=25,width=175)
text1.insert(END,timer)
Label2=Label(font=('arial',15,'bold'),text='BILL DATE:')
Label2.place(x=500,y=80)
text2=Entry(font=('arial',15,'bold'))
text2.place(x=620,y=82)
text2.insert(END,dateset)
Label3=Label(font=('arial',15,'bold'),text='BILL NUMBER:')
Label3.place(x=10,y=80)
text3=Entry()
text3.place(x=165,y=82,height=25,width=175)

Button_add=Button(root,font=('arial',15,'bold'),text='ADD',height=1,width=7, command=add_button)
Button_add.place(x=1100,y=175)

Button2=Button(root,font=('arial',15,'bold'),text='RESET',height=1,width=7, command=reset)
Button2.place(x=1100,y=275)

Button3=Button(root,font=('arial',15,'bold'),text='VIEW',height=1,width=7, command=view)
Button3.place(x=1100,y=375)

Button4=Button(root,font=('arial',15,'bold'),text='EXIT',height=1,width=7, command=exit)
Button4.place(x=1100,y=475)

#Button5=Button(root,font=('arial',15,'bold'),text='CANCEL',height=1,width=7)
#Button5.place(x=1100,y=575)

Label4=Label(font=('arial',15,'bold'),text='SELECT ITEMS :')
Label4.place(x=10,y=150)

Label5=Label(font=('arial',15,'bold'),text='LIST:')
Label5.place(x=550,y=150)

text4=Entry().place(x=10,y=180,height=35,width=500)
Label6:Label(text4,font=('arial',14,'bold'),text='                 CODE                 ITEMS                    QTY.',bg='white').place(x=12,y=182)

listcanvas = Canvas(root, height=376,width=500, bg="#FFFFFF")
listcanvas.place(x=550,y=220)


Lb=Listbox(root,selectmode=EXTENDED,font=('arial',15,'bold'),height=15,width=45)
Lb.insert(1,"                101              Kurkure")
Lb.insert(2,"                102              Lays")
Lb.insert(3,"                103              Maggi")
Lb.insert(4,"                104              Dove")
Lb.insert(5,"                105              Rice")
Lb.insert(6,"                106              Oil")
Lb.insert(7,"                107              Books")
Lb.insert(8,"                108              Hide & Seek")
Lb.insert(9,"                109              Cheese")
Lb.insert(10,"                110              Masala")
Lb.insert(11,"                111              Butter")
Lb.insert(12,"                112              Paneer")
Lb.insert(13,"                113              Parle-G")
Lb.insert(14,"                114              Oreo")
Lb.insert(15,"                115              Chocolates")
Lb.place(x=10,y=220)

check1=Checkbutton(Lb,  variable=var1, onvalue=1, offvalue=0)
check1.place(x=8,y=1)
check2=Checkbutton(Lb,  variable=var2, onvalue=1, offvalue=0).place(x=8,y=25)
check3=Checkbutton(Lb,  variable=var3, onvalue=1, offvalue=0).place(x=8,y=50)
check4=Checkbutton(Lb, variable=var4, onvalue=1, offvalue=0).place(x=8,y=75)
check5=Checkbutton(Lb, variable=var5, onvalue=1, offvalue=0).place(x=8,y=100)
check6=Checkbutton(Lb,  variable=var6, onvalue=1, offvalue=0).place(x=8,y=125)
check7=Checkbutton(Lb, variable=var7, onvalue=1, offvalue=0).place(x=8,y=150)
check8=Checkbutton(Lb, variable=var8, onvalue=1, offvalue=0).place(x=8,y=175)
check9=Checkbutton(Lb, variable=var9, onvalue=1, offvalue=0).place(x=8,y=200)
check10=Checkbutton(Lb, variable=var10, onvalue=1, offvalue=0).place(x=8,y=225)
check11=Checkbutton(Lb, variable=var11, onvalue=1, offvalue=0).place(x=8,y=250)
check12=Checkbutton(Lb, variable=var12, onvalue=1, offvalue=0).place(x=8,y=275)
check13=Checkbutton(Lb, variable=var13, onvalue=1, offvalue=0).place(x=8,y=300)
check14=Checkbutton(Lb, variable=var14, onvalue=1, offvalue=0).place(x=8,y=325)
check15=Checkbutton(Lb, variable=var15, onvalue=1, offvalue=0).place(x=8,y=350)


spin1 = Spinbox(Lb, from_=1, to=10,width=10)
spin1.place(x=375,y=1)
spin2 = Spinbox(Lb, from_=1, to=10,width=10)
spin2.place(x=375,y=25)
spin3 = Spinbox(Lb, from_=1, to=10,width=10)
spin3.place(x=375,y=50)
spin4 = Spinbox(Lb, from_=1, to=10,width=10)
spin4.place(x=375,y=75)
spin5 = Spinbox(Lb, from_=1, to=10,width=10)
spin5.place(x=375,y=100)
spin6 = Spinbox(Lb, from_=1, to=10,width=10)
spin6.place(x=375,y=125)
spin7 = Spinbox(Lb, from_=1, to=10,width=10)
spin7.place(x=375,y=150)
spin8 = Spinbox(Lb, from_=1, to=10,width=10)
spin8.place(x=375,y=175)
spin9 = Spinbox(Lb, from_=1, to=10,width=10)
spin9.place(x=375,y=200)
spin10 = Spinbox(Lb, from_=1, to=10,width=10)
spin10.place(x=375,y=225)
spin11 = Spinbox(Lb, from_=1, to=10,width=10)
spin11.place(x=375,y=250)
spin12 = Spinbox(Lb, from_=1, to=10,width=10)
spin12.place(x=375,y=275)
spin13 = Spinbox(Lb, from_=1, to=10,width=10)
spin13.place(x=375,y=300)
spin14 = Spinbox(Lb, from_=1, to=10,width=10)
spin14.place(x=375,y=325)
spin15 = Spinbox(Lb, from_=1, to=10,width=10)
spin15.place(x=375,y=350)

text5=Entry().place(x=550,y=180,height=35,width=500)
Label7:Label(text5,font=('arial',14,'bold'),text='          CODE                 ITEMS                    QTY.',bg='white').place(x=552,y=182)

root.mainloop()


