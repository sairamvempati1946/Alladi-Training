'''
from tkinter import *
import pymongo
class Workers:
    def __init__(self,window):
        self.window = window
        window.title("New Workers Registration Form")
        window.geometry("600x600")
        window.configure(bg="orange")
        self.idnumber = StringVar()
        self.name = StringVar()
        self.gender = StringVar()
        self.dob = StringVar()
        self.address = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        l1 = Label(window, text="ID Number", width=20, height=3, bg="yellow")
        l1.grid(row=0, column=0)
        e1 = Entry(window, width=10, textvariable=self.idnumber, bg="light pink")
        e1.grid(row=0, column=1)
        l2 = Label(window, text="Name", width=20, height=3, bg="light green")
        l2.grid(row=0, column=3)
        e2 = Entry(window, width=10, textvariable=self.name, bg="light blue")
        e2.grid(row=0, column=4)
        l3 = Label(window, text="Gender", width=20, height=3, bg="yellow")
        l3.grid(row=1, column=0)
        e3 = Entry(window, width=10, textvariable=self.gender, bg="light pink")
        e3.grid(row=1, column=1)
        l4 = Label(window, text="DOB", width=20, height=3, bg="light green")
        l4.grid(row=1, column=3)
        e4 = Entry(window, width=10, textvariable=self.dob, bg="light blue")
        e4.grid(row=1, column=4)
        l5 = Label(window, text="Address", width=20, height=3, bg="yellow")
        l5.grid(row=2, column=0)
        e5 = Entry(window, width=10, textvariable=self.address, bg="light pink")
        e5.grid(row=2, column=1)
        l6 = Label(window, text="Phone", width=20, height=3, bg="light green")
        l6.grid(row=2, column=3)
        e6 = Entry(window, width=10, textvariable=self.phone, bg="light blue")
        e6.grid(row=2, column=4)
        l7 = Label(window, text="Email", width=20, height=3, bg="yellow")
        l7.grid(row=3, column=0)
        e7 = Entry(window, width=10, textvariable=self.email, bg="light pink")
        e7.grid(row=3, column=1)
        b1 = Button(window, text="SUBMIT", command=self.enroll, bg="green")
        b1.grid(row=10, column=0)
        b2 = Button(window, text="UPDATE", command=self.update_info, bg="yellow")
        b2.grid(row=10, column=2)
        b3 = Button(window, text="DELETE", command=self.delete_info, bg="red")
        b3.grid(row=10, column=4)
    def enroll(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["holymary_db"]
        coll = db["employee_details"]
        data = [
            {
                "idnumber": self.idnumber.get(),
                "name": self.name.get(),
                "gender": self.gender.get(),
                "address": self.address.get(),
                "phone": self.phone.get(),
                "email": self.email.get(),
                "dob": self.dob.get(),

            }
        ]

        x = coll.insert_many(data)
        print(
            "data has been inserted into desired collection, respective primary keys:\n",
            x.inserted_ids,
        )
        self.clear()
    def update_info(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["employee_db"]
        coll = db["employee_details"]
        query = {"idnumber": self.idnumber.get()}
        new_values = {"$set": {"name": self.name.get()}}
        coll.update_one(query, new_values)
        for x in coll.find():
            print("ur updated data:\n", x)
        self.clear()
    def delete_info(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["employee_db"]
        coll = db["employee_details"]
        query = {"eposition": self.position.get()}
        coll.delete_one(query)
        print("ur record has been deleted")
        for x in coll.find():
            print("ur desired record deleted successfully:\n", x)

        self.clear()
    def clear(self):
        self.name.set("")
        self.gender.set("")
        self.idnumber.set("")
        self.email.set("")
        self.dob.set("")
        self.address.set("")
        self.phone.set("")

window = Tk()
ob = Workers(window)
window.mainloop()
'''




'''
from tkinter import *
import pymongo
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class student:
    def __init__(self, window):
        self.window = window
        window.title("Student Management System Connection to MangoDB Server")
        window.geometry("350x300")
        window.config(bg="pink")
        self.sid = StringVar()
        self.sname = StringVar()
        self.sphone = StringVar()

        l1 = Label(window, text="Student ID", width=20, height=3)
        l1.grid(row=0, column=0)
        e1 = Entry(window, width=10, textvariable=self.sid)
        e1.grid(row=0, column=1)
        l2 = Label(window, text="Student Name", width=20, height=3)
        l2.grid(row=1, column=0)
        e2 = Entry(window, width=10, textvariable=self.sname)
        e2.grid(row=1, column=1)
        l3 = Label(window, text="Student Phone Number", width=20, height=3)
        l3.grid(row=2, column=0)
        e3 = Entry(window, width=10, textvariable=self.sphone)
        e3.grid(row=2, column=1)
        b1 = Button(window, text="Enroll", command=self.enroll)
        b1.grid(row=6, column=2)
        b2 = Button(window, text="Update", command=self.update_info)
        b2.grid(row=6, column=3)
        b3 = Button(window, text="Show Data", command=self.show_info)
        b3.grid(row=6, column=4)
        self.t3=Text(window,height=5,width=70,bg="pink")
        self.t3.place(x=300, y=500)

    def enroll(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["ACT_DB"]
        collection = db["STUDENT_DETAILS_TKINTER"]
        a = {"Student ID": self.sid.get(), "Student Name": self.sname.get(), "Student Phone Number": self.sphone.get()}

        x = collection.insert_one(a)
        print("Data is inserted Successfully into MongoDB")
        self.clear()

    def update_info(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["ACT_DB"]
        collection1 = db["STUDENT_DETAILS_TKINTER"]
        b = {"Student ID": self.sid.get()}
        # c={"$set":{"Student Name":self.sname.get()}}
        c = {"$set": {"Student Phone Number": self.sphone.get()}}
        collection1.update_one(b, c)
        self.clear()
        print("Updation Done Check in Database")

    def show_info(self):
        #self.t3.delete(0,END='')
        c = pymongo.MongoClient("mongodb://localhost:27017")
        db = c["ACT_DB"]
        col = db["STUDENT_DETAILS_TKINTER"]
        uid = {"Student ID": self.sid.get()}
        d=col.find(uid)
        for i in d:
            print(i)
        #x = d.find({}, {'_id': 0, 'self.sname': 1})
        self.t3.insert(END, str(i))



    def clear(self):
        self.sid.set("")
        self.sname.set("")
        self.sphone.set("")


window = Tk()
ob = student(window)
window.mainloop()
'''


'''
import time
import datetime
from tkinter import *
import tkinter.messagebox

window = Tk()
window.title("NTH: Employee Payroll System")
window.geometry('100x200')
window.configure(background="white")

Tops = Frame(window, width=1350, height=50, bd=8, bg="lavender")
Tops.pack()
# ---------------------------------------------------------------------------------------
f1 = Frame(window, width=600, height=600, bd=8, bg="red")
f1.pack(side=LEFT)
# -------------------------------------------------------------------------------------
f2 = Frame(window, width=300, height=700, bd=8, bg="yellow")
f2.pack(side=RIGHT)
# -------------------------------------------------------------------------------------
fla = Frame(f1, width=600, height=200, bd=8, bg="green")
fla.pack(side=TOP)
# -----------------------------------------------------------------------------------
flb = Frame(f1, width=300, height=600, bd=8, bg="blue")
flb.pack(side=BOTTOM)
# ------------------------------------------------------------------------------------

lblinfo = Label(Tops, font=('arial', 30, 'bold'), text="EMPLOYEE PAYROLL SYSTEM ", bd=10, fg="blue")
lblinfo.grid(row=0, column=0)


def exit():
    exit = tkinter.messagebox.askyesno("Employee system", "Do you want to exit the system")
    if exit > 0:
        window.destroy()
        return


def reset():
    Name.set("")
    Address.set("")
    HoursWorked.set("")
    wageshour.set("")
    Payable.set("")
    Taxable.set("")
    NetPayable.set("")
    GrossPayable.set("")
    OverTimeBonus.set("")
    Employer.set("")
    NINumber.set("")
    txtpayslip.delete("1.0", END)


def enterinfo():
    txtpayslip.delete("1.0", END)
    txtpayslip.insert(END, "\t\tPay Slip\n\n")
    txtpayslip.insert(END, "Name :\t\t" + Name.get() + "\n\n")
    txtpayslip.insert(END, "Address :\t\t" + Address.get() + "\n\n")
    txtpayslip.insert(END, "Employer :\t\t" + Employer.get() + "\n\n")
    txtpayslip.insert(END, "NI Number :\t\t" + NINumber.get() + "\n\n")
    txtpayslip.insert(END, "Hours Worked :\t\t" + HoursWorked.get() + "\n\n")
    txtpayslip.insert(END, "Net Payable :\t\t" + NetPayable.get() + "\n\n")
    txtpayslip.insert(END, "Wages per hour :\t\t" + wageshour.get() + "\n\n")
    txtpayslip.insert(END, "Tax Paid :\t\t" + Taxable.get() + "\n\n")
    txtpayslip.insert(END, "Payable :\t\t" + Payable.get() + "\n\n")


def weeklywages():
    txtpayslip.delete("1.0", END)
    hoursworkedperweek = float(HoursWorked.get())
    wagesperhours = float(wageshour.get())

    paydue = wagesperhours * hoursworkedperweek
    paymentdue = "INR", str('%.2f' % (paydue))
    Payable.set(paymentdue)

    tax = paydue * 0.2
    taxable = "INR", str('%.2f' % (tax))
    Taxable.set(taxable)

    netpay = paydue - tax
    netpays = "INR", str('%.2f' % (netpay))
    NetPayable.set(netpays)

    if hoursworkedperweek > 40:
        overtimehours = (hoursworkedperweek - 40) + wagesperhours * 1.5
        overtime = "INR", str('%.2f' % (overtimehours))
        OverTimeBonus.set(overtime)
    elif hoursworkedperweek <= 40:
        overtimepay = (hoursworkedperweek - 40) + wagesperhours * 1.5
        overtimehrs = "INR", str('%.2f' % (overtimepay))
        OverTimeBonus.set(overtimehrs)
    return


# =============================== Variables ========================================================
Name = StringVar()
Address = StringVar()
HoursWorked = StringVar()
wageshour = StringVar()
Payable = StringVar()
Taxable = StringVar()
NetPayable = StringVar()
GrossPayable = StringVar()
OverTimeBonus = StringVar()
Employer = StringVar()
NINumber = StringVar()
TimeOfOrder = StringVar()
DateOfOrder = StringVar()

DateOfOrder.set(time.strftime("%d/%m/%Y"))

#================================ Label Widget =================================================

lblName = Label(fla, text="Name", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=0, column=0)
lblAddress = Label(fla, text="Address", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=0,
                                                                                                            column=2)
lblEmployer = Label(fla, text="Employer", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=1,
                                                                                                              column=0)
lblNINumber = Label(fla, text="NI Number", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=1,
                                                                                                               column=2)
lblHoursWorked = Label(fla, text="Hours Worked", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(
    row=2, column=0)
lblHourlyRate = Label(fla, text="Hourly Rate", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(
    row=2, column=2)
lblTax = Label(fla, text="Tax", font=('arial', 16, 'bold'), bd=20, anchor='w', fg="red", bg="powder blue").grid(row=3,
                                                                                                                column=0)
lblOverTime = Label(fla, text="OverTime", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=3,
                                                                                                              column=2)
lblGrossPay = Label(fla, text="GrossPay", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=4,
                                                                                                              column=0)
lblNetPay = Label(fla, text="Net Pay", font=('arial', 16, 'bold'), bd=20, fg="red", bg="powder blue").grid(row=4,
                                                                                                           column=2)

# =============================== Entry Widget =================================================

etxname = Entry(fla, textvariable=Name, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
etxname.grid(row=0, column=1)

etxaddress = Entry(fla, textvariable=Address, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
etxaddress.grid(row=0, column=3)

etxemployer = Entry(fla, textvariable=Employer, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
etxemployer.grid(row=1, column=1)

etxhoursworked = Entry(fla, textvariable=HoursWorked, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
etxhoursworked.grid(row=2, column=1)

etxwagesperhours = Entry(fla, textvariable=wageshour, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
etxwagesperhours.grid(row=2, column=3)

etxnin = Entry(fla, textvariable=NINumber, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
etxnin.grid(row=1, column=3)

etxgrosspay = Entry(fla, textvariable=Payable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
etxgrosspay.grid(row=4, column=1)

etxnetpay = Entry(fla, textvariable=NetPayable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
etxnetpay.grid(row=4, column=3)

etxtax = Entry(fla, textvariable=Taxable, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
etxtax.grid(row=3, column=1)

etxovertime = Entry(fla, textvariable=OverTimeBonus, font=('arial', 16, 'bold'), bd=16, width=22, justify='left')
etxovertime.grid(row=3, column=3)

# =============================== Text Widget ============================================================

payslip = Label(f2, textvariable=DateOfOrder, font=('arial', 21, 'bold'), fg="red", bg="powder blue").grid(row=0,
                                                                                                           column=0)

txtpayslip = Text(f2, height=22, width=34, bd=16, font=('arial', 13, 'bold'), fg="green", bg="powder blue")
txtpayslip.grid(row=1, column=0)

# =============================== buttons ===============================================================

btnsalary = Button(flb, text='Weekly Salary', padx=10, pady=10, bd=8, font=('arial', 7, 'bold'), width=6, fg="red",
                   bg="powder blue", command=weeklywages).grid(row=0, column=0)

btnreset = Button(flb, text='Reset', padx=10, pady=10, bd=8, font=('arial', 7, 'bold'), width=6, command=reset,
                  fg="red", bg="powder blue").grid(row=0, column=1)

btnpayslip = Button(flb, text='View Payslip', padx=10, pady=10, bd=8, font=('arial', 7, 'bold'), width=6,
                    command=enterinfo, fg="red", bg="powder blue").grid(row=0, column=2)

btnexit = Button(flb, text='Exit System', padx=10, pady=10, bd=8, font=('arial', 7, 'bold'), width=6, command=exit,
                 fg="red", bg="powder blue").grid(row=0, column=3)
# btnquit=Button(flb,text='Quit System',padx=10,pady=10,bd=8,font=('arial',7,'bold'),width=6,command=exit,fg="red",bg="powder blue").grid(row=0,column=4)

window.mainloop()
'''


'''
from tkinter import *
window=Tk()

window.geometry("450x350")
window.title("CHECK BOX DEMO")
def event():
    if var.get()==1:
        print("check box is selected")
    else:
        print("check box deselected")
#CREATE a variable to hold status of the check box
#when checkbox selected variable is hold 1 as value , deselect as 0
var=IntVar()
ch_box1=Checkbutton(window,text="Python",variable=var,onvalue=1,offvalue=0,command=event)

#specify properties or configurations related checkbutton
ch_box1.config(bg="lightgrey",fg="red",selectcolor="black",relief="raised",padx=10,pady=5)

#write a code to align check button
ch_box1.pack(padx=40,pady=40)
ch_box1.flash()

window.mainloop()
'''


'''
from tkinter import*
window=Tk()
window.geometry("350x450")
window.config(bg="pink")
#to maintain status of radio button we need one variable
v=StringVar(window,"3")
values={"Python":"1","AIML":"2","DS":"3","JAVA":"4"}
#APPLY FOR Loop create multiple radio buttons
for (text,value) in values.items():
    Radiobutton(window,text=text,variable=v,value=value).pack(side=TOP,ipady=5)

window.mainloop()
'''



from tkinter import*
window=Tk()
window.geometry("350x450")
window.config(bg="pink")
list_box=Listbox(window,height=10,width=15,bg="red",font="Helvetica",fg="blue")
l1=Label(window,text="SOFTWARE COURSES")
#INSERT VALUES INTO LIST BOX
list_box.insert(1,"PYTHON")
list_box.insert(2,"JAVA")
list_box.insert(3,"AI&ML")
list_box.insert(4,"SELENIUM")
l1.pack()
list_box.pack(side=LEFT)
window.mainloop()


















