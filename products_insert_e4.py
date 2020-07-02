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
    (196, 196, '선인 가나슈 필링 1kg / 초콜릿크림, 와플잼', '3700', '선인 가나슈 필링 1kg / 초콜릿크림, 와플잼', '1000', 'e4', 'e4196', 'e4196', 'e4196.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (222, 222, '제원 데코젤 미로와 5kg (광택제)', '27000', '제원 데코젤 미로와 5kg (광택제)', '1000', 'e4', 'e4222', 'e4222', 'e4222.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 5kg, 개입량 : 1개입', ''),
    (223, 223, '데코화이트(데코스노우) 1kg (쉽게 녹지 않는 슈가파우더)', '3800', '데코화이트(데코스노우) 1kg (쉽게 녹지 않는 슈가파우더)', '1000', 'e4', 'e4223', 'e4223', 'e4223.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
