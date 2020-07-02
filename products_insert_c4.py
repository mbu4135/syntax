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
    (76, 76, '아이엠에그 난황 국산 1kg', '7800', '아이엠에그 난황 국산 1kg', '1000', 'c4', 'c476', 'c476', 'c476.jpg', '2020-04-17 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입, 원산지 : 국내산', '드레싱류, 마요네즈, 아이스크림류, 머스타드, 제과, 제빵 등 사용.'),
    (77, 77, '아이엠에그 난백 국산 1kg', '4700', '아이엠에그 난백 국산 1kg', '1000', 'c4', 'c477', 'c477', 'c477.jpg', '2020-04-17 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입, 원산지 : 국내산', '드레싱류, 마요네즈, 아이스크림류, 머스타드, 제과, 제빵 등 사용.'),
    (182, 182, '냉동 난황 2.268kg', '14700', '냉동 난황 2.268kg', '1000', 'c4', 'c4182', 'c4182', 'c4182.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 1kg, 개입량 : 1개입', '드레싱류, 마요네즈, 아이스크림류, 머스타드, 제과, 제빵 등 사용.'),
    (183, 183, '데어리스타 멸균우유 1L', '1750', '데어리스타 멸균우유 1L', '1000', 'c4', 'c4183', 'c4183', 'c4183.jpg', '2020-04-17 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
