import mysql.connector
from mysql.connector.cursor import SQL_COMMENT
from mysql.connector.errors import DatabaseError

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="FREDLY2505",
    database="python"
)

mycursor = mydb.cursor()

sql="DELETE FROM demo WHERE ID>%s"
val=("5",)

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")