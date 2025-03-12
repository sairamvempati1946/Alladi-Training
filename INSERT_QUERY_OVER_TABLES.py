'''
import pymysql
query="insert into AMAZON values('104','Veekshitha','CSE','9876543213')"

con=pymysql.connect(host="localhost",user="root",password="20WH1A05G5",database="act_student_db")
#cursor creation
cur=con.cursor()#enable the access data globally or concurrently
#query execution
cur.execute(query)
con.commit()
print("DATA has been inserted student details successfully over table")
#connection close
con.close()
'''

#-----------------------------------------------------------------------------------------------------------------------

'''
import pymysql
query="insert into PERSONS values('105','SRAVANI','9786846612')"

con=pymysql.connect(host="localhost",user="root",password="20WH1A05G5",database="AMAZON")
#cursor creation
cur=con.cursor()#enable the access data globally or concurrently
#query execution
cur.execute(query)
con.commit()
print("DATA has been inserted student details successfully over table")
#connection close
con.close()
'''

'''
import pymysql
query ="INSERT INTO ORDERS VALUES(12188,7095,105)"

con=pymysql.connect(host="localhost",user="root",password="20WH1A05G5",database="AMAZON")
cur=con.cursor()
cur.execute(query)
con.commit()
print("DATA HAS BEEN INSERTED SUCCESSFULLY OVER TABLE")
con.close()
'''