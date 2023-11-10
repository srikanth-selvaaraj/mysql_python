# it is used for prevent from sql injection

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='FREDLY2505',
    database='python'
)

mycursor = mydb.cursor()

sql="SELECT * FROM demo WHERE name = %s"
name=("Srikanth",)  # comma(,) is must

mycursor.execute(sql,name)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
