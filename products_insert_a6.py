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
    (73, 73, '서울식품 케익시트 1호', '3200', '서울식품 케익시트 1호', '1000', 'a6', 'a673', 'a673', 'a673.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 200 g(580 kcal), 개입량 : 1개입, 1개당 크기 : 약 15 × 15 × 6.5 cm, 원산지 : 국내산', '상온에서 약 30~40분 해동 후 사용'),
    (74, 74, '서울식품 케익시트 2호', '4000', '서울식품 케익시트 2호', '1000', 'a6', 'a674', 'a674', 'a674.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 300 g(870 kcal), 개입량 : 1개입, 1개당 크기 : 약 17 × 17 × 6.5 cm, 원산지 : 국내산', '상온에서 약 30~40분 해동 후 사용'),
    (75, 75, '서울식품 케익시트 3호', '5500', '서울식품 케익시트 3호', '1000', 'a6', 'a675', 'a675', 'a675.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 300 g(870 kcal), 개입량 : 1개입, 1개당 크기 : 약 21 × 21 × 6.5 cm, 원산지 : 국내산', '상온에서 약 30~40분 해동 후 사용'),
    (78, 78, '서울식품 플레인머핀 (110gx1개입)', '1250', '서울식품 플레인머핀 (110gx1개입)', '1000', 'a6', 'a678', 'a678', 'a678.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 110 g(475 kcal), 개입량 : 1개입, 1개당 크기 : 약 8.5 × 8.5 × 7.8 cm, 원산지 : 국내산', '상온에서 약 30분 해동 후 섭취'),
    (79, 79, '서울식품 초코머핀 (110gx1개입)', '1250', '서울식품 초코머핀 (110gx1개입)', '1000', 'a6', 'a679', 'a679', 'a679.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 110 g(475 kcal), 개입량 : 1개입, 1개당 크기 : 약 8.5 × 8.5 × 7.8 cm, 원산지 : 국내산', '상온에서 약 30분 해동 후 섭취'),
    (80, 80, '서울식품 블루베리머핀 (110gx1개입)', '1250', '서울식품 블루베리머핀 (110gx1개입)', '1000', 'a6', 'a680', 'a680', 'a680.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 110 g(475 kcal), 개입량 : 1개입, 1개당 크기 : 약 8.5 × 8.5 × 7.8 cm, 원산지 : 국내산', '상온에서 약 30분 해동 후 섭취'),
    (81, 81, '서울식품 치즈머핀 (110gx1개입)', '1250', '서울식품 치즈머핀 (110gx1개입)', '1000', 'a6', 'a681', 'a681', 'a681.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 110 g(475 kcal), 개입량 : 1개입, 1개당 크기 : 약 8.5 × 8.5 × 7.8 cm, 원산지 : 국내산', '상온에서 약 30분 해동 후 섭취'),
    (82, 82, '케익시트 3단 슬라이스', '3300', '케익시트 3단 슬라이스', '1000', 'a6', 'a682', 'a682', 'a682.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : , 개입량 : 1개입, 1개당 크기 : , 원산지 : 국내산', '상온에서 약 30분 해동 후 섭취'),
    (195, 195, '찹쌀떡 (흰모찌떡) 60g*30개입 냉동찹쌀떡', '6400', '찹쌀떡 (흰모찌떡) 60g*30개입 냉동찹쌀떡', '1000', 'a6', 'a682', 'a682', 'a682.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 60gx30개입 , 개입량 : 30개입', ''),
    (261, 261, '서울식품 소보루가루 / 소보로가루 2kg', '14200', '서울식품 소보루가루 / 소보로가루 2kg', '1000', 'a6', 'a6261', 'a6261', 'a6261.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 2kg , 개입량 : 1개입', ''),
    (275, 275, '홈와플(소)(53g×10개입)', '7800', '홈와플(소)(53g×10개입)', '1000', 'a6', 'a6275', 'a6275', 'a6275.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 530g , 개입량 : 10개입', ''),
    (277, 277, '서울식품 맨치트 아몬드쿠키 1BOX 50g 30개 완제품쿠키', '24800', '서울식품 맨치트 아몬드쿠키 1BOX 50g 30개 완제품쿠키', '1000', 'a6', 'a6277', 'a6277', 'a6277.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 1,500g , 개입량 : 30개입', ''),
    (278, 278, '서울식품 맨치트 초코쿠키 1BOX 50g 30개 완제품쿠키', '24800', '서울식품 맨치트 초코쿠키 1BOX 50g 30개 완제품쿠키', '1000', 'a6', 'a6278', 'a6278', 'a6278.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 1,500g , 개입량 : 30개입', ''),
    (279, 279, '서울식품 완) 크로와상골드 (12개입) (완제)', '9400', '서울식품 완) 크로와상골드 (12개입) (완제)', '1000', 'a6', 'a6279', 'a6279', 'a6279.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : , 개입량 : 12개입', ''),
    (314, 314, '플레인 베이글 6개입', '9400', '플레인 베이글 6개입', '1000', 'a6', 'a6314', 'a6314', 'a6314.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : , 개입량 : 6개입', ''),
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
