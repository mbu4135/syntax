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

mycursor.execute('DROP TABLE IF EXISTS imp_uid')
mycursor.execute("CREATE TABLE imp_uid (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,imp_uid varchar(100) DEFAULT NULL)")

mydb.commit()

print(mycursor.rowcount, "record inserted.")
