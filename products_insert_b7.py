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
    (88, 88, '대두 화과방 우리통팥 2kg - 국산팥', '12700', '대두 화과방 우리통팥 2kg - 국산팥', '1000', 'b7', 'b788', 'b788', 'b788.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 2kg, 개입량 : 1개입', ''),
    (153, 153, '리치스 슬라이스 오이피클 3kg', '5630', '리치스 슬라이스 오이피클 3kg', '1000', 'b7', 'b7153', 'b7153', 'b7153.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 3kg, 개입량 : 1개입', ''),
    (255, 255, '설정식품 사과다이스 3kg (고형량1.6kg/국내산)', '11000', '설정식품 사과다이스 3kg (고형량1.6kg/국내산)', '1000', 'b7', 'b7255', 'b7255', 'b7255.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 3kg, 개입량 : 1개입', ''),
    (256, 256, '설정식품 웰스피아 고구마다이스 3kg', '11000', '설정식품 웰스피아 고구마다이스 3kg', '1000', 'b7', 'b7256', 'b7256', 'b7256.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 3kg, 개입량 : 1개입', ''),
    (274, 274, '옥수수캔 425g', '850', '옥수수캔 425g', '1000', 'b7', 'b7274', 'b7274', 'b7274.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 425g, 개입량 : 1개입', ''),
    (309, 309, '파인애플(820g)', '2600', '파인애플(820g)', '1000', 'b7', 'b7309', 'b7309', 'b7309.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 820g, 개입량 : 1개입', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
