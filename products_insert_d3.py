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
    (140, 140, '햇 호박씨 1kg', '6200', '햇 호박씨 1kg', '1000', 'd3', 'd3140', 'd3140', 'd3140.jpg', '2020-04-15 18:33:40', '불필요', '서늘한곳에 보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (141, 141, '해바라기씨 1kg (미국산)', '4900', '해바라기씨 1kg (미국산)', '1000', 'd3', 'd3141', 'd3141', 'd3141.jpg', '2020-04-15 18:33:40', '불필요', '서늘한곳에 보관', '내용량 : 1kg, 개입량 : 1개입', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
