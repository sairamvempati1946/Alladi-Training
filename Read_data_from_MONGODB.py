import pymongo
#write a code to connect mongodb as client
client=pymongo.MongoClient("mongodb://localhost:27017")
#writa a code to connect desired database over the mangodb
db=client["ACT_DB"]
#Write a code to connect collection tables
coll=db["STUDENT_DETAILS"]
#CREATE DATA IN THE FORM OF DICTINARY/KEY:VALUE PAIR
for i in coll.find():
    print("student details:\n",i)