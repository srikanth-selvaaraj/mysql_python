import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FREDLY2505",
    database="python"
)

mycursor = mydb.cursor()

sql = "UPDATE demo SET name = %s WHERE name = %s"
val = ("Ram","Sam")

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")