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
    (177, 177, '매일연유 500g (가당)', '3500', '매일연유 500g (가당)', '1000', 'c5', 'c5177', 'c5177', 'c5177.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 500g, 개입량 : 1개입', ''),
    (178, 178, '서강 크리밀 연유 500g / 튜브연유', '2990', '선인 크림치즈무스 1kg / 스위트치즈스프레드', '1000', 'c5', 'c5178', 'c5178', 'c5178.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 500g, 개입량 : 1개입', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
