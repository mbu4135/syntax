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

mycursor.execute('DROP TABLE IF EXISTS help')
mycursor.execute("CREATE TABLE help (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,uid int(11) DEFAULT NULL,selec varchar(20) NOT NULL,name varchar(11) NOT NULL,phone varchar(20) NOT NULL,email varchar(20) NOT NULL,title varchar(20) NOT NULL,contents text NOT NULL)")

mydb.commit()

print(mycursor.rowcount, "record inserted.")
