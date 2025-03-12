'''
import pymysql
#query
query="CREATE DATABASE deekshitha"
#mysql connection string
con=pymysql.connect(host="localhost",user="root",password="20WH1A05G5")
#cursor creation
cur=con.cursor()#enable the access data globally or concurrently
#query execution
cur.execute(query)
con.commit()
print("Database created successfully")
#connection close
con.close()
'''


'''
import pymysql
#query
query="CREATE DATABASE AMAZON"
#mysql connection string
con=pymysql.connect(host="localhost",user="root",password="20WH1A05G5")
#cursor creation
cur=con.cursor()#enable the access data globally or concurrently
#query execution
cur.execute(query)
con.commit()
print("Database created successfully")
#connection close
con.close()
'''


