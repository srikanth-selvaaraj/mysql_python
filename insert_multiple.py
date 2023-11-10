import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FREDLY2505",
    database="python"
)

mycursor = mydb.cursor()

sql = "INSERT INTO products (id, fav) VALUES (%s,%s)"
val = [
    ('154','Chocolate'),
    ('155','Tasty Lemons'),
    ('156','vanilla Dreams')
]

mycursor.executemany(sql,val)

mydb.commit() #required

print(mycursor.rowcount, "record was inserted.")