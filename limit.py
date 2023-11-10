import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FREDLY2505",
    database="python"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM demo LIMIT 3 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)