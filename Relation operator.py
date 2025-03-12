from tkinter import*
from tkinter import messagebox

window=Tk()
window.geometry("1000x600")
window.config(bg="white")
window.title("Number")
def Number():
    x=int(e1.get())
    y=int(e2.get())

    if(x==2 and y>5):
        messagebox.showinfo("STATUS:","Number is valid")
    else:
        messagebox.showinfo("STATUS:", "Number is invalid")

#label1
l1=Label(window,text="x",font=40)
l1.grid(row=0,column=0)
#entry box
e1=Entry(window)
e1.grid(row=0,column=1)
#l2
l2=Label(window,text="y",font=40)
l2.grid(row=1,column=0)
#entry box
e2=Entry(window)
e2.grid(row=1,column=1)
#button
b1=Button(window,text="SUBMIT",command=Number)
b1.grid(row=2,column=1)

window.mainloop()