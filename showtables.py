#!python
import mysql.connector

# MySQL Connection 연결
mydb = mysql.connector.connect(
  host="localhost",
  user="mbu4135",
  passwd="1288zpmqal",
  charset="utf8",
  db="menshut",
  autocommit="True"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM all_orders")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
