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
    (259, 259, '에쓰푸드 세블락 소시지 300g (10人) /세블락소세지,소세지,에스푸드', '3400', '에쓰푸드 세블락 소시지 300g (10人) /세블락소세지,소세지,에스푸드', '1000', 'b8', 'b8259', 'b8259', 'b8259.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 3kg, 개입량 : 10개입', ''),
    (260, 260, '에쓰푸드 세블락 소시지 400g (4人) /세블락소세지,소세지,에스푸드', '4550', '에쓰푸드 세블락 소시지 400g (4人) /세블락소세지,소세지,에스푸드', '1000', 'b8', 'b8260', 'b8260', 'b8260.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 1.6kg, 개입량 : 4개입', ''),
    (312, 312, '에쓰푸드 페퍼맛 스모크 소시지 900g /페퍼맛소세지,소세지,에스푸드', '10800', '에쓰푸드 페퍼맛 스모크 소시지 900g /페퍼맛소세지,소세지,에스푸드', '1000', 'b8', 'b8312', 'b8312', 'b8312.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 900g, 개입량 : 4개입', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
