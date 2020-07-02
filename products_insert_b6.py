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
    (88, 88, '대두 화과방 우리통팥 2kg - 국산팥', '13000', '대두 화과방 우리통팥 2kg - 국산팥', '1000', 'b7', 'b788', 'b788', 'b788.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 2kg, 개입량 : 1개입', ''),
    (148, 148, '제원 데코젤 미로와 5kg', '28000', '제원 데코젤 미로와 5kg', '1000', 'b6', 'b6148', 'b6148', 'b6148.jpg', '2020-04-15 18:33:40', '불필요', '서늘한곳에 보관', '내용량 : 5kg, 개입량 : 1개입', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
