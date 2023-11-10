import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FREDLY2505",
    database="python"
)

mycursor = mydb.cursor()

sql = "INSERT INTO demo (name) VALUES (%s)"
val = ("Ram",)

mycursor.execute(sql,val)

mydb.commit() #required

print(mycursor.rowcount, "record inserted., ID:", mycursor.lastrowid)