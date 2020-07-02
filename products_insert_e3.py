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
    (286, 286, '선인 다크컴파운드 초코칩 1kg / 초콜릿,데코,컴파운드초코칩', '4500', '선인 다크컴파운드 초코칩 1kg / 초콜릿,데코,컴파운드초코칩', '1000', 'e3', 'e3286', 'e3286', 'e3286.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (296, 296, '발로나 코코아 파우더 3kg', '64800', '발로나 코코아 파우더 3kg', '1000', 'e3', 'e3296', 'e3296', 'e3296.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (297, 297, '카카오바리 엑스트라브뤼츠 코코아파우더 1kg (엑스트라브뤼트)', '16850', '카카오바리 엑스트라브뤼츠 코코아파우더 1kg (엑스트라브뤼트)', '1000', 'e3', 'e3297', 'e3297', 'e3297.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
