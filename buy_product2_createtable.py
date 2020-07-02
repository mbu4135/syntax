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

mycursor.execute('DROP TABLE IF EXISTS buy_product2')
mycursor.execute("CREATE TABLE buy_product2 (uid int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, ofname varchar(100) DEFAULT NULL, username varchar(100) DEFAULT NULL,email varchar(50) DEFAULT NULL, rmobile1 varchar(20) DEFAULT NULL,rmobile2 varchar(20) DEFAULT NULL,rmobile3 varchar(20) DEFAULT NULL,addnum int(11) DEFAULT NULL, oplace varchar(100) DEFAULT NULL, oplacee varchar(100) DEFAULT NULL, oplaced varchar(100) DEFAULT NULL, memo varchar (100) DEFAULT NULL, metho varchar (100) DEFAULT NULL, refun varchar (100) DEFAULT NULL)")

mydb.commit()

print(mycursor.rowcount, "record inserted.")
