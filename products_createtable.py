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

mycursor.execute('DROP TABLE IF EXISTS products')
mycursor.execute("CREATE TABLE products (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,pid int(11) NOT NULL,pName varchar(100) NOT NULL,price int(11) NOT NULL,description text NOT NULL,available int(11) NOT NULL,category varchar(100) NOT NULL,item varchar(100) NOT NULL,pCode varchar(20) NOT NULL,picture text NOT NULL,date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,info1 text NOT NULL,info2 text NOT NULL,info3 text NOT NULL,info4 text NOT NULL,info5 text DEFAULT NULL,info6 text DEFAULT NULL)")

mydb.commit()

print(mycursor.rowcount, "record inserted.")
