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
    (42, 42, '서울식품 블루베리머핀반죽(1kg)', '7800', '서울식품 블루베리머핀반죽(1kg)', '1000', 'a3', 'a342', 'a342', 'a342.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 1kg, 개입량 : 1개입, 1개당 크기 : 약 21 × 38 × 3 cm, 원산지 : 국내산', '상온에서 약 40분간 해동,175~180도 오븐에서 약 30~35분간 구워줍니다.'),
    (43, 43, '서울식품 초코머핀반죽(1kg)', '7800', '서울식품 초코머핀반죽(1kg)', '1000', 'a3', 'a343', 'a343', 'a343.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 1kg, 개입량 : 1개입, 1개당 크기 : 약 21 × 38 × 3 cm, 원산지 : 국내산', '상온에서 약 40분간 해동,175~180도 오븐에서 약 30~35분간 구워줍니다.'),
    (44, 44, '서울식품 플레인머핀반죽(1kg)', '7800', '서울식품 플레인머핀반죽(1kg)', '1000', 'a3', 'a344', 'a344', 'a344.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 1kg, 개입량 : 1개입, 1개당 크기 : 약 21 × 38 × 3 cm, 원산지 : 국내산', '상온에서 약 40분간 해동,175~180도 오븐에서 약 30~35분간 구워줍니다.'),
    (45, 45, '서울식품 치즈머핀반죽(1kg)', '7800', '서울식품 치즈머핀반죽(1kg)', '1000', 'a3', 'a345', 'a345', 'a345.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 1kg, 개입량 : 1개입, 1개당 크기 : 약 21 × 38 × 3 cm, 원산지 : 국내산', '상온에서 약 40분간 해동,175~180도 오븐에서 약 30~35분간 구워줍니다.'),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
