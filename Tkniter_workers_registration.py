from tkinter import *
import pymongo

window = Tk()
window.geometry("600x600")
window.title("Workers Registration")
window.configure(bg="purple")

#l1
l1=Label(window, text="ID NUMBER",font=30,bg="yellow",width=20, height=3)
l1.grid(row=0,column=0)
#e1
e1=Entry(window)
e1.grid(row=0,column=1)

l2=Label(window, text="Name",font=30,bg="green",width=20, height=3)
l2.grid(row=0,column=3)
#e1
e2=Entry(window)
e2.grid(row=0,column=4)

l3=Label(window, text="GENDER",font=30,bg="yellow",width=20, height=3)
l3.grid(row=2,column=0)
#e1
e3=Entry(window)
e3.grid(row=2,column=1)

l4=Label(window, text="DOB",font=30,bg="green",width=20, height=3)
l4.grid(row=2,column=3)
#e1
e4=Entry(window)
e4.grid(row=2,column=4)

l5=Label(window, text="ADDRESS",font=30,bg="yellow",width=20, height=3)
l5.grid(row=3,column=0)
#e1
e5=Entry(window)
e5.grid(row=3,column=1)

l6=Label(window, text="PHONE NUMBER",font=30,bg="green",width=20, height=3)
l6.grid(row=3,column=3)
#e1
e6=Entry(window)
e6.grid(row=3,column=4)

l7=Label(window, text="EMAIL",font=30,bg="yellow",width=20, height=3)
l7.grid(row=6,column=0)
#e1
e7=Entry(window)
e7.grid(row=6,column=1)

#B1
b1 = Button(window, text="SUBMIT",bg="green")
b1.grid(row=11, column=1)

b1 = Button(window, text="UPDATE",bg="green")
b1.grid(row=11, column=3)

b1 = Button(window, text="DELETE",bg="green")
b1.grid(row=11, column=4)


window.mainloop()
