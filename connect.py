import mysql.connector

Dname = 'python'
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FREDLY2505",
    database=Dname
)

print(mydb)
