import mysql.connector
from mysql.connector.errors import DatabaseError

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FREDLY2505",
    database="python"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM demo ORDER BY name DESC")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)