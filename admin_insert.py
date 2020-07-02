#!python
import mysql.connector

# MySQL Connection 연결
mydb = mysql.connector.connect(
  host="localhost",
  user="mbu4135",
  passwd="1288zpmqal",
  charset="utf8",
  database="menshut"
)

mycursor = mydb.cursor()

sql = "insert into admin(id, firstName, lastName, email, mobile, address, password, type, confirmCode)"
val = [
    (4, 'Min', 'Byeongun', 'mbu4135@gmail.com', '01030655770', 'Dhaka', '1288zpmqal', 'manager', '0');
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
