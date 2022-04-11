from tkinter import *
from tkinter import messagebox
root=Tk()
s=0
vay=0
#input
def calc():
    try:
        global vay
        global s
        if vay == 0:
            s = float(e.get())
        elif vay == 1:
            s = s + float(e.get())
        elif vay == 2:
            s = s - float(e.get())
        elif vay == 3:
            s = s / float(e.get())
        elif vay == 4:
            s = s % float(e.get())
        elif vay==5:
            s=s*float(e.get())
        elif vay==6:
            s = s
    except:
        messagebox.showerror('ERROR','Enter a number')
def printval():
    global vay
    global s
    calc()
    e.delete(0, END)
    e.insert(0,str(s))
    vay=6
    s=float(s)
def click(a):
    c=e.get()
    if a<10:
        e.delete(0,END)
        e.insert(0,str(c)+str(a))
    else:
        e.insert(len(c),'.')

#clear screen
def dela():
    global vay
    global s
    e.delete(0,END)
    s=0
    vay=0

#backspace
def delb():
    c=e.get()
    c=str(c)
    e.delete(len(c)-1,len(c))

#add
def add():
    global vay
    global s
    calc()
    e.delete(0,END)
    vay=1

def sub():
    global vay
    global s
    calc()
    e.delete(0, END)
    vay = 2
def mul():
    global vay
    global s
    calc()
    e.delete(0, END)
    vay = 5
def div():
    global vay
    global s
    calc()
    e.delete(0, END)
    vay = 3
def mod():
    global vay
    global s
    calc()
    e.delete(0, END)
    vay = 4
#root window
root.title('Calculator')
root.config(background='black')
root.geometry('600x800')
root.resizable(False,False)
root.iconbitmap('icon.ico')

#text window
e=Entry(root,width=22,fg='white',bg='black',justify='left',font=('Times New Roman',40,"bold"),borderwidth=0)
e.config(state=NORMAL)
e.grid(row=1,rowspan=2,column=1,columnspan=4)

#buttons
button_1=Button(text='1',padx=40,pady=40,fg='white',bg='black',activebackground='grey',font=('Times New Roman',30),borderwidth=0,command=lambda: click(1)).grid(row=3,column=1)
button_2=Button(text='2',padx=40,pady=40,fg='white',bg='black',activebackground='grey',font=('Times New Roman',30),borderwidth=0,command=lambda: click(2)).grid(row=3,column=2)
button_3=Button(text='3',padx=40,pady=40,fg='white',bg='black',activebackground='grey',font=('Times New Roman',30),borderwidth=0,command=lambda: click(3)).grid(row=3,column=3)

button_4=Button(text='4',padx=40,pady=40,fg='white',bg='black',activebackground='grey',font=('Times New Roman',30),borderwidth=0,command=lambda: click(4)).grid(row=4,column=1)
button_5=Button(text='5',padx=40,pady=40,fg='white',bg='black',activebackground='grey',font=('Times New Roman',30),borderwidth=0,command=lambda: click(5)).grid(row=4,column=2)
button_6=Button(text='6',padx=40,pady=40,fg='white',bg='black',activebackground='grey',font=('Times New Roman',30),borderwidth=0,command=lambda: click(6)).grid(row=4,column=3)

button_7=Button(text='7',padx=40,pady=40,fg='white',bg='black',activebackground='grey',font=('Times New Roman',30),borderwidth=0,command=lambda: click(7)).grid(row=5,column=1)
button_8=Button(text='8',padx=40,pady=40,fg='white',bg='black',activebackground='grey',font=('Times New Roman',30),borderwidth=0,command=lambda: click(8)).grid(row=5,column=2)
button_9=Button(text='9',padx=40,pady=40,fg='white',bg='black',activebackground='grey',font=('Times New Roman',30),borderwidth=0,command=lambda: click(9)).grid(row=5,column=3)

button_0=Button(text='0',padx=40,pady=40,fg='white',bg='black',activebackground='grey',font=('Times New Roman',30),borderwidth=0,command=lambda: click(0)).grid(row=6,column=2)
button_dot=Button(text='.',padx=40,pady=40,fg='white',bg='black',activebackground='grey',font=('Times New Roman',30),borderwidth=0,command=lambda: click(10)).grid(row=6,column=1)

button_clear=Button(text='Clear',padx=40,pady=20,fg='red',bg='black',activebackground='grey',activeforeground='red',font=('Times New Roman',30),borderwidth=0,command=dela).grid(row=3,column=4)
button_enter=Button(text='Enter',padx=85,pady=20,fg='white',bg='green',activebackground='green',activeforeground='white',font=('Times New Roman',30),borderwidth=0,command=printval).grid(row=7,column=1,columnspan=2)
button_backspace=Button(text='\<',padx=40,pady=40,fg='red',bg='black',activebackground='grey',font=('Times New Roman',30),borderwidth=0,command=delb).grid(row=6,column=3)

#arithmetic buttons
button_add=Button(text='+',padx=40,pady=40,fg='green',bg='black',activebackground='grey',activeforeground='green',font=('Times New Roman',30),borderwidth=0,command=add).grid(row=7,column=3)
button_sub=Button(text='-',padx=40,pady=40,fg='green',bg='black',activebackground='grey',activeforeground='green',font=('Times New Roman',30),borderwidth=0,command=sub).grid(row=4,column=4)
button_div=Button(text='/',padx=40,pady=40,fg='green',bg='black',activebackground='grey',activeforeground='green',font=('Times New Roman',30),borderwidth=0,command=div).grid(row=5,column=4)
button_mul=Button(text='X',padx=40,pady=40,fg='green',bg='black',activebackground='grey',activeforeground='green',font=('Ariel',30),borderwidth=0,command=mul).grid(row=6,column=4)
button_mod=Button(text='%',padx=40,pady=40,fg='green',bg='black',activebackground='grey',activeforeground='green',font=('Times New Roman',30),borderwidth=0,command=mod).grid(row=7,column=4)

root.mainloop()
