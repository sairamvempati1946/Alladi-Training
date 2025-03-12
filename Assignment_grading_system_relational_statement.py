'''
#1Q:GRADE SYSTEM-LOGIC:
score = float(input("Enter ur aggregate score:\n"))
if(score >= 90):
    grade="A"
    print("U HAVE GOT GRADE:",grade)
elif(score>=80 and score <90):
    grade = "B"
    print("U HAVE GOT GRADE:", grade)
elif(score>=70 and score <80):
    grade = "C"
    print("U HAVE GOT GRADE:", grade)
elif(score>=60 and score<70):
    grade = "D"
    print("U HAVE GOT GRADE:", grade)
elif(score>=50 and score<60):
    grade = "E"
    print("U HAVE GOT GRADE:", grade)
elif(score<50 and score>0):
    grade = "F"
    print("U HAVE FAILED:", grade)
else:
    print("wrong input given")


#USING TKINTER:
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("GRADE SYSTEM")
window.geometry("500x450")
window.configure(bg="pink")

def grade_determination():
    score = float(e1.get())
    if(score >= 90):
        grade="A"
        messagebox.showinfo("STATUS",grade)
    elif(score>=80 and score < 90):
        grade = "B"
        messagebox.showinfo("STATUS", grade)
    elif(score>=70 and score <80):
        grade = "C"
        messagebox.showinfo("STATUS", grade)
    elif(score>=60 and score < 70):
        grade = "D"
        messagebox.showinfo("STATUS", grade)
    elif(score>=50 and score<60):
        grade = "E"
        messagebox.showinfo("STATUS", grade)
    elif(score<50 and score>=0):
        grade = "Fail"
        messagebox.showinfo("STATUS", grade)
    else:
        messagebox.showinfo("STATUS", "invalid input")

# label1:
l1 = Label(window,text="Enter Score:",font=30)
l1.grid(row=0, column=0)
#entrybox1
e1 = Entry(window)
e1.grid(row=0, column=1)
#button
b1_sum = Button(window, text="GRADE VALIDITY", command = grade_determination)
b1_sum.grid(row=7, column=5)
window.mainloop()
'''


'''
#2Q:BANK LOAN ELIGIBILITY

1ST METHOD
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Bank Loan Eligibility")
window.geometry("500x450")
window.configure(bg="pink")

def Loan():
    Age = int(e1.get())
    salary=int(e2.get())
    credit_score=int(e3.get())

    if(Age >= 21 and Age < 60):
        if (salary >= 40000):
            if (credit_score >= 650):
                messagebox.showinfo("Eligibility", "You are eligible for the loan.")
            else:
                messagebox.showinfo("Eligibility", "You are not eligible due to low credit score.")
        else:
            messagebox.showinfo("Eligibility", "You are not eligible due to low salary.")
    else:
        messagebox.showinfo("Eligibility", "You are not eligible due to age restrictions.")

# label1:
l1 = Label(window,text="Age:",font=30)
l1.grid(row=0, column=0)
#entrybox1
e1 = Entry(window)
e1.grid(row=0, column=1)

#label2
l2 = Label(window,text="Salary:",font=30)
l2.grid(row=1, column=0)
#entrybox2
e2 = Entry(window)
e2.grid(row=1, column=1)

#label3
l3 = Label(window,text="Credit score:",font=30)
l3.grid(row=2, column=0)
#entrybox3
e3 = Entry(window)
e3.grid(row=2, column=1)

#button
b1 = Button(window, text="Loan Validity", command = Loan)
b1.grid(row=3, column=4)
window.mainloop()


2ND METHOD:
from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("500x450")
window.title("Bank Loan Eligibility")

def loan_eligibility():
    Age=int(e1.get())
    Salary=int(e2.get())
    Credit_Score=int(e3.get())
    if(Age>=21 and Age<60):
        messagebox.showinfo("status","Ur are eligible for a loan")
        if(Salary>=40,000):
            messagebox.showinfo("status","Ur are eligible for loan")
        if(Credit_Score>=650):
            messagebox.showinfo("status","Ur are eligible for loan")
        else:
            messagebox.showinfo("status","Ur not eligible")
#label1:
l1=Label(window,text="Enter Score",font=30)
l1.grid(row=0,column=0)
l2=Label(window,text="Enter Salary",font=30)
l2.grid(row=1,column=0)
l3=Label(window,text="Enter Credit_Score",font=30)
l3.grid(row=2,column=0)
#entrybox1:
e1=Entry(window)
e1.grid(row=0, column=1)
e2=Entry(window)
e2.grid(row=1, column=1)
e3=Entry(window)
e3.grid(row=2, column=1)
# button
b1 = Button(window,text="LOAN ELIGIBILITY",command=loan_eligibility)
b1.grid(row=3, column=4)
window.mainloop()
'''