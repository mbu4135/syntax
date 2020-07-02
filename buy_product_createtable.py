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

mycursor.execute('DROP TABLE IF EXISTS buy_product1')
mycursor.execute("CREATE TABLE buy_product1 (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,uid int(11) DEFAULT NULL,ofname text DEFAULT NULL,pid int(11) NOT NULL,quantity int(11) NOT NULL,dstatus varchar(10) NOT NULL DEFAULT 'no',odate timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,ddate date DEFAULT NULL,pName varchar(100) DEFAULT NULL,price int(11) DEFAULT NULL,condi varchar(100) DEFAULT '배송준비',total_price int(11) DEFAULT NULL)")

mydb.commit()

print(mycursor.rowcount, "record inserted.")
