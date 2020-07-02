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

mycursor.execute('DROP TABLE IF EXISTS product_level')
mycursor.execute("CREATE TABLE product_level (id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,product_id int(11) NOT NULL,v_shape varchar(10) NOT NULL DEFAULT 'no',polo varchar(10) NOT NULL DEFAULT 'no',clean_text varchar(10) NOT NULL DEFAULT 'no',design varchar(10) NOT NULL DEFAULT 'no',chain varchar(10) NOT NULL DEFAULT 'no',leather varchar(10) NOT NULL DEFAULT 'no',hook varchar(10) NOT NULL DEFAULT 'no',color varchar(10) NOT NULL DEFAULT 'no',formal varchar(10) NOT NULL DEFAULT 'no',converse varchar(10) NOT NULL DEFAULT 'no',loafer varchar(10) NOT NULL DEFAULT 'no')")

mydb.commit()

print(mycursor.rowcount, "record inserted.")
