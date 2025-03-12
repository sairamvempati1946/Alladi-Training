import pymysql

query="delete from student_details where sid=101"

con=pymysql.connect(host="localhost",user="root",password="20WH1A05G5",database="act_student_db")
#cursor creation
cur=con.cursor()#enable the access data globally or concurrently
#query execution
cur.execute(query)
con.commit()
print("DATA has been deleted successfully over table")
#connection close
con.close()