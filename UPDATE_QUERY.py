'''
import pymysql

query="UPDATE FROM PERSONS WHERE SID=104"

con=pymysql.connect(host="localhost",user="root",password="20WH1A05G5",database="AMAZON")
#cursor creation
cur=con.cursor()#enable the access data globally or concurrently
#query execution
cur.execute(query)
con.commit()
print("DATA has been updated successfully over table")
#connection close
con.close()
'''



