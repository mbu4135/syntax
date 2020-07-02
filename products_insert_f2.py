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
    (122, 122, '칼리바우트 화이트커버춰 초콜릿 2.5kg', '34500', '칼리바우트 화이트커버춰 초콜릿 2.5kg', '1000', 'e1', 'e1122', 'e1122', 'e1122.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 2.5kg, 개입량 : 1개입', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
