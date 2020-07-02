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
    (298, 298, '카카오바리 브룬 코팅 다크 초콜릿(파타글라세) 5kg /코팅다크초콜릿', '45800', '카카오바리 브룬 코팅 다크 초콜릿(파타글라세) 5kg /코팅다크초콜릿', '1000', 'e2', 'e2298', 'e2298', 'e2298.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 5kg, 개입량 : 1개입', ''),
    (299, 299, '카카오바리 브룬 코팅 화이트 초콜릿(파타글라세) 5kg /코팅다크초콜릿', '47000', '카카오바리 브룬 코팅 화이트 초콜릿(파타글라세) 5kg /코팅다크초콜릿', '1000', 'e2', 'e2299', 'e2299', 'e2299.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 5kg, 개입량 : 1개입', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
