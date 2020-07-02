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

mycursor.execute('DROP TABLE IF EXISTS orders')
mycursor.execute('DROP TABLE IF EXISTS uorders')
mycursor.execute('DROP TABLE IF EXISTS uorders1')
mycursor.execute('DROP TABLE IF EXISTS uorders2')
mycursor.execute('DROP TABLE IF EXISTS uorders3')
mycursor.execute("CREATE TABLE orders (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,uid int(11) DEFAULT NULL,ofname text DEFAULT NULL,pid int(11) NOT NULL,quantity int(11) NOT NULL,dstatus varchar(10) NOT NULL DEFAULT 'no',odate timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,ddate date DEFAULT NULL,pName varchar(100) DEFAULT NULL,price int(11) DEFAULT NULL,condi varchar(100) DEFAULT '배송준비')")
mycursor.execute("CREATE TABLE uorders (uid int(11) DEFAULT NULL,ofname text DEFAULT NULL,pid int(11) NOT NULL,quantity int(11) NOT NULL,dstatus varchar(10) NOT NULL DEFAULT 'no',odate timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,ddate date DEFAULT NULL,pName varchar(100) DEFAULT NULL,price int(11) DEFAULT NULL,condi varchar(100) DEFAULT '배송준비')")
mycursor.execute('INSERT INTO uorders(uid,pid,quantity) VALUES(%s,%s,%s)', (0,0,0,))
mydb.commit()

print(mycursor.rowcount, "record inserted.")
