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
    (121, 121, '칼리바우트 다크커버춰 초콜릿 2.5kg (카카오 57.7%)', '31000', '칼리바우트 다크커버춰 초콜릿 2.5kg (카카오 57.7%)', '1000', 'e1', 'e1121', 'e1121', 'e1121.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 2.5kg, 개입량 : 1개입', ''),
    (122, 122, '칼리바우트 화이트커버춰 초콜릿 2.5kg', '34500', '칼리바우트 화이트커버춰 초콜릿 2.5kg', '1000', 'e1', 'e1122', 'e1122', 'e1122.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 2.5kg, 개입량 : 1개입', ''),
    (292, 292, '칼리바우트 다크커버춰 초콜릿 10kg', '119000', '칼리바우트 다크커버춰 초콜릿 10kg', '1000', 'e1', 'e1292', 'e1292', 'e1292.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 10kg, 개입량 : 1개입', ''),
    (293, 293, '칼리바우트 골드커버춰 초콜릿 2.5kg', '46000', '칼리바우트 골드커버춰 초콜릿 2.5kg', '1000', 'e1', 'e1293', 'e1293', 'e1293.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 2.5kg, 개입량 : 1개입', ''),
    (294, 294, '칼리바우트 밀크커버춰 초콜릿 2.5kg', '32500', '칼리바우트 밀크커버춰 초콜릿 2.5kg', '1000', 'e1', 'e1294', 'e1294', 'e1294.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 2.5kg, 개입량 : 1개입', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
