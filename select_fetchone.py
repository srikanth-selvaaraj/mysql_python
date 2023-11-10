import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FREDLY2505",
    database="python"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM demo")

myresult = mycursor.fetchone()     #fetch all the rows

print(myresult)
