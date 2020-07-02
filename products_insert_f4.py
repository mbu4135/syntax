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

sql = "insert into products(id, pid, pName, price, description, available, category, item, pCode, picture, date, info1, info2, info3, info4) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val = [
    (283, 283, '유산지(1/4년)', '13500', '유산지(1/4년)', '1000', 'f4', 'f4283', 'f4283', 'f4283.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : , 개입량 : ', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
