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

mycursor.execute('DROP TABLE IF EXISTS product_view')
mycursor.execute("CREATE TABLE product_view (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,user_id int(11) NOT NULL,product_id int(11) NOT NULL,date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP)")

mydb.commit()

print(mycursor.rowcount, "record inserted.")
