import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FREDLY2505"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE python")
