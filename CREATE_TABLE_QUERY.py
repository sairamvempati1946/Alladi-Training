'''import pymysql
#query
query="CREATE TABLE STUDENT_DETAILS(SID int, SNAME VARCHAR(50),SCOURCE VARCHAR(50), SPHONE VARCHAR(10))"

#mysql connection string
con=pymysql.connect(host="localhost",user="root",password="20WH1A05G5",database="act_student_db")
#cursor creation
cur=con.cursor()#enable the access data globally or concurrently
#query execution
cur.execute(query)
con.commit()
print("Tables created successfully in database")
#connection close
con.close()
'''

'''
import pymysql
#query
query="CREATE TABLE PERSONS(ID INT PRIMARY KEY, PNAME VARCHAR(50),PPHONE VARCHAR(10))"

#mysql connection string
con=pymysql.connect(host="localhost",user="root",password="20WH1A05G5",database="AMAZON")
#cursor creation
cur=con.cursor()#enable the access data globally or concurrently
#query execution
cur.execute(query)
con.commit()
print("Tables created successfully in database")
#connection close
con.close()
'''

'''
import pymysql
#query
query="CREATE TABLE ORDERS(OID INT, DPIN INT UNIQUE, ID INT, FOREIGN KEY(ID) REFERENCES PERSONS(ID))"

#mysql connection string
con=pymysql.connect(host="localhost",user="root",password="20WH1A05G5",database="AMAZON")
#cursor creation
cur=con.cursor()#enable the access data globally or concurrently
#query execution
cur.execute(query)
con.commit()
print("Tables created successfully in database")
#connection close
con.close()
'''

