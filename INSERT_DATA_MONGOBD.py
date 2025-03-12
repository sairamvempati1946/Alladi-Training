import pymongo
#write a code to connect mongodb as client
client=pymongo.MongoClient("mongodb://localhost:27017")
#writa a code to connect desired database over the mangodb
db=client["ACT_DB"]
#Write a code to connect collection tables
coll=db["STUDENT_DETAILS"]
#Create data in the form of dicitinary/key:value pair
data=[{"SID":501,"SNAME":"ANU","SCOURCE":"AIML","SPHONE":"9000950022"},
{"SID":502,"SNAME":"SRINI","SCOURCE":"AIML","SPHONE":"9000650022"},
{"SID":503,"SNAME":"VENKET","SCOURCE":"DATA SCIENCE","SPHONE":"9000750022"},
{"SID":504,"SNAME":"JYOTHI","SCOURCE":"DATA SCIENCE","SPHONE":"9100950022"}]
X=coll.insert_many(data)
print("data has been inserted into desired collection\n")
print("Primary keys:\n",X.inserted_ids)
'''


'''
from tkinter import *
import pymongo
class student:
    def __init__(self,window):
        self.window = window
        window.title("New Student Registration Form")
        window.geometry("500x500")
        window.configure(bg="orange")
        self.idnumber = StringVar()
        self.name = StringVar()
        self.gender = StringVar()
        self.qualification = StringVar()
        self.dob = StringVar()
        self.address = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.course = StringVar()
        self.exp = StringVar()
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
        l4 = Label(window, text="Qualification", width=20, height=3, bg="light green")
        l4.grid(row=1, column=3)
        e4 = Entry(window, width=10, textvariable=self.qualification, bg="light blue")
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
        l8 = Label(window, text="Course", width=20, height=3, bg="light green")
        l8.grid(row=3, column=3)
        e8 = Entry(window, width=10, textvariable=self.course, bg="light blue")
        e8.grid(row=3, column=4)
        l9 = Label(window, text="Experience", width=20, height=3, bg="yellow")
        l9.grid(row=4, column=0)
        e9 = Entry(window, width=10, textvariable=self.exp, bg="light pink")
        e9.grid(row=4, column=1)
        l10 = Label(window, text="DOB", width=20, height=3, bg="light green")
        l10.grid(row=4, column=3)
        e10 = Entry(window, width=10, textvariable=self.dob, bg="light blue")
        e10.grid(row=4, column=4)
        b1 = Button(window, text="SUBMIT", command=self.enroll, bg="green")
        b1.grid(row=10, column=0)
        b2 = Button(window, text="UPDATE", command=self.update_info, bg="yellow")
        b2.grid(row=10, column=2)
        b3 = Button(window, text="DELETE", command=self.delete_info, bg="red")
        b3.grid(row=10, column=4)
    def enroll(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["holymary_db"]
        coll = db["student_details"]
        data = [
            {
                "idnumber": self.idnumber.get(),
                "name": self.name.get(),
                "gender": self.gender.get(),
                "qualification": self.qualification.get(),
                "address": self.address.get(),
                "phone": self.phone.get(),
                "email": self.email.get(),
                "course": self.course.get(),
                "exp": self.exp.get(),
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
        self.qualification.set("")
        self.email.set("")
        self.dob.set("")
        self.address.set("")
        self.phone.set("")
        self.course.set("")
        self.exp.set("")

window = Tk()
ob = student(window)
window.mainloop()
'''




'''
from tkinter import *
import pymongo
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class student:
    def __init__(self,window):
        self.window = window
        window.title("Student Management System Connection to MangoDB Server")
        window.geometry("350x300")
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
        self.t3=Entry()
        self.t3.place(x=200, y=200)

    def enroll(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["STUDENT_DB"]
        collection = db["STUDENT_DETAILS"]
        a = {"Student ID": self.sid.get(), "Student Name": self.sname.get(), "Student Phone Number": self.sphone.get()}

        x = collection.insert_one(a)
        print("Data is inserted Successfully into MongoDB")
        self.clear()

    def update_info(self):
        client = pymongo.MongoClient("mongodb://localhost:27017")
        db = client["STUDENT_DB"]
        collection1 = db["STUDENT_DETAILS"]
        b = {"Student ID": self.sid.get()}
        # c={"$set":{"Student Name":self.sname.get()}}
        c = {"$set": {"Student Phone Number": self.sphone.get()}}
        collection1.update_one(b, c)
        self.clear()
        print("Updation Done Check in Database")

    def show_info(self):
        self.t3.delete(0,END='')
        c = pymongo.MongoClient("mongodb://localhost:27017")
        db = c["STUDENT_DB"]
        col = db["STUDENT_DETAILS"]
        uid = {"Student ID": self.sid.get()}
        d=col.find(uid)
        x = d.find({}, {'_id': 0, 'self.sname': 1})
        self.t3.insert(END, str(x))



    def clear(self):
        self.sid.set("")
        self.sname.set("")
        self.sphone.set("")


window = Tk()
ob = student(window)
window.mainloop()
'''






















