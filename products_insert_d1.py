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
    (123, 123, '아몬드슬라이스 1kg (미국/캘리포니아)', '12500', '아몬드슬라이스 1kg (미국/캘리포니아)', '1000', 'd1', 'd1123', 'd1123', 'd1123.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (124, 124, '백아몬드슬라이스 1kg (미국/캘리포니아) / 아몬드슬라이스', '13100', '꼬미다 슈가파우더 3kg', '1000', 'd1', 'd1124', 'd1124', 'd1124.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (125, 125, '햇 호두분태 1kg (미국/캘리포니아)', '12400', '햇 호두분태 1kg (미국) / 호두 햇호두 캘리포니아호두분태', '1000', 'd1', 'd1125', 'd1125', 'd1125.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (126, 126, '다이아몬드 호두분태 벌크 캘리포니아 (13.61kg)', '162800', '다이아몬드 캘리포니아 호두분태 벌크 (13.61kg)', '1000', 'd1', 'd1126', 'd1126', 'd1126.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 13.61kg, 개입량 : 1개입', ''),
    (127, 127, '블루다이아몬드 아몬드슬라이스 벌크 캘리포니아 (11.34kg)', '138000', '블루다이아몬드 아몬드슬라이스 벌크 (11.34kg)', '1000', 'd1', 'd1127', 'd1127', 'd1127.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 11.34kg, 개입량 : 1개입', ''),
    (128, 128, '햇 호두 1/4태 1kg (미국/캘리포니아)', '10800', '캘리포니아 햇 호두 1/4태 1kg (미국)', '1000', 'd1', 'd1128', 'd1128', 'd1128.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (129, 129, '햇 아몬드분태 1kg (미국/캘리포니아)', '13600', '햇 아몬드분태 1kg (캘리포니아 미국) 아몬드 분태', '1000', 'd1', 'd1129', 'd1129', 'd1129.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (130, 130, '햇 호두반태 1kg (미국/캘리포니아)', '12700', '캘리포니아 햇 호두반태 1kg (미국)', '1000', 'd1', 'd1130', 'd1130', 'd1130.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (131, 131, '햇 통아몬드 1kg (미국/캘리포니아)', '11300', '햇 통아몬드 1kg (미국.캘리포니아)', '1000', 'd1', 'd1131', 'd1131', 'd1131.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (132, 132, '아몬드분태 10kg (캘리포니아.미국)', '110400', '아몬드분태 10kg (캘리포니아.미국)', '1000', 'd1', 'd1132', 'd1132', 'd1132.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 10kg, 개입량 : 1개입', ''),
    (134, 134, '풀그린 아몬드분말 벌크 11.34kg (아몬드95%,소맥분5%)', '97500', '풀그린 아몬드분말 벌크 11.34kg (아몬드95%,소맥분5%)', '1000', 'd1', 'd1134', 'd1134', 'd1134.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 11.34kg, 개입량 : 1개입', ''),
    (184, 184, '선인 피스타치오 커넬 100g', '10700', '선인 피스타치오 커넬 100g', '1000', 'd1', 'd1184', 'd1184', 'd1184.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 100g, 개입량 : 1개입', ''),
    (185, 185, '해바라기 씨 1kg 미국산', '3600', '해바라기 씨 1kg 미국산', '1000', 'd1', 'd1185', 'd1185', 'd1185.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (186, 186, '헤이즐넛 1kg 미국산', '16400', '헤이즐넛 1kg 미국산', '1000', 'd1', 'd1186', 'd1186', 'd1186.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    
    (199, 199, '건포도 1kg / 건과일,말린포도', '5000', '건포도 1kg / 건과일,말린포도', '1000', 'd1', 'd1199', 'd1199', 'd1199.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (210, 210, '공주 당적밤 (2.19kg)', '24900', '공주 당적밤 (2.19kg)', '1000', 'd1', 'd1210', 'd1210', 'd1210.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 2.19kg, 개입량 : 1개입', ''),
    (211, 211, '녹차 분말 1kg (보성산)', '47830', '녹차 분말 1kg (보성산)', '1000', 'd1', 'd1211', 'd1211', 'd1211.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (212, 212, '녹차 분말 1kg (일본산 마차)', '92600', '녹차 분말 1kg (보성산)', '1000', 'd1', 'd1212', 'd1212', 'd1212.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (224, 224, '볶은 땅콩 분태 1kg', '6300', '볶은 땅콩 분태 1kg', '1000', 'd1', 'd1224', 'd1224', 'd1224.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
