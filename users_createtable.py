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

mycursor.execute('DROP TABLE IF EXISTS users')
mycursor.execute("CREATE TABLE users (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,uid int(11) DEFAULT NULL,username varchar(50) NOT NULL,ofname varchar(50) DEFAULT NULL,email varchar(50) DEFAULT NULL,password varchar(100) DEFAULT NULL,rmobile1 varchar(20) DEFAULT NULL,rmobile2 varchar(20) DEFAULT NULL,rmobile3 varchar(20) DEFAULT NULL,cnumber int(11) DEFAULT NULL, addnum int(11) DEFAULT NULL, oplace varchar(100) DEFAULT NULL, oplacee varchar(100) DEFAULT NULL, oplaced varchar(100) DEFAULT NULL,reg_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,online varchar(1) NOT NULL DEFAULT '0',activation varchar(3) NOT NULL DEFAULT 'yes',memo varchar(100) DEFAULT NULL,membership varchar(100) DEFAULT '일반회원')")

mydb.commit()

print(mycursor.rowcount, "record inserted.")
