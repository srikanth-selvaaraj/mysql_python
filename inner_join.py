import mysql.connector
from mysql.connector.errors import DatabaseError

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FREDLY2505",
    database="python"
)

mycursor = mydb.cursor()

sql = "SELECT users.name AS name, products.fav AS favorite FROM users RIGHT JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)