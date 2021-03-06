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
    (161, 161, '선인 에버휩 1030g (식물성,가당 휘핑크림,생크림)', '2800', '선인 에버휩 1030g (식물성,가당 휘핑크림,생크림)', '1000', 'c2', 'c2161', 'c2161', 'c2161.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 1030g, 개입량 : 1개입', ''),
    
    (163, 163, '뉴 골드라벨 1030g / 식물성 가당 생크림', '3000', '뉴 골드라벨 1030g / 식물성 가당 생크림', '1000', 'c2', 'c2163', 'c2163', 'c2163.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 1030g, 개입량 : 1개입', ''),
    (164, 164, '알라 동물성 휘핑크림 1L (무가당) / 코스트코 생크림,덴마크산', '6900', '알라 동물성 휘핑크림 1L (무가당) / 코스트코 생크림,덴마크산', '1000', 'c2', 'c2164', 'c2164', 'c2164.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (165, 165, '선인 가나슈 필링 1kg / 초콜릿크림, 와플잼', '3700', '선인 가나슈 필링 1kg / 초콜릿크림, 와플잼', '1000', 'c2', 'c2165', 'c2165', 'c2165.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (166, 166, '선인 크림치즈무스 1kg / 스위트치즈스프레드,크림치즈,치즈필링', '7800', '선인 크림치즈무스 1kg / 스위트치즈스프레드,크림치즈,치즈필링', '1000', 'c2', 'c2166', 'c2166', 'c2166.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (167, 167, '매일휘핑크림 38% 1L (국산생크림, 매일동물성생크림)', '8200', '매일휘핑크림 38% 1L (국산생크림, 매일동물성생크림)', '1000', 'c2', 'c2167', 'c2167', 'c2167.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (168, 168, '온탑 생크림 340g (식물성) / 아이스박스 필수구매', '3300', '온탑 생크림 340g (식물성) / 아이스박스 필수구매', '1000', 'c2', 'c2168', 'c2168', 'c2168.jpg', '2020-04-15 18:33:40', '필요', '냉ehd보관', '내용량 : 340g, 개입량 : 1개입', ''),
    (169, 169, '사워크림 LP 1L / 샤워크림 사우어크림', '6100', '사워크림 LP 1L / 샤워크림 사우어크림', '1000', 'c2', 'c2169', 'c2169', 'c2169.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (170, 170, '끼리크림치즈 1kg (프랑스크림치즈)', '15200', '끼리크림치즈 1kg (프랑스크림치즈)', '1000', 'c2', 'c2170', 'c2170', 'c2170.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (171, 171, '끼리크림치즈 1박스 (1kg x 12개입)', '182400', '끼리크림치즈 1박스 (1kg x 12개입)', '1000', 'c2', 'c2171', 'c2171', 'c2171.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 12kg, 개입량 : 12개입', ''),
    (209, 209, '골드라벨 오리지널 907g / 식물성 가당 생크림', '3950', '골드라벨 오리지널 907g / 식물성 가당 생크림', '1000', 'c2', 'c2209', 'c2209', 'c2209.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 907g, 개입량 : 1개입', ''),
    (229, 229, '매일생크림 500ml /매일우유생크림,매일생크림', '3590', '매일생크림 500ml /매일우유생크림,매일생크림', '1000', 'c2', 'c2229', 'c2229', 'c2229.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 500g, 개입량 : 1개입', ''),
    (230, 230, '알라 부코 대니쉬 크림치즈 1.8kg / 덴마크', '21000', '알라 부코 대니쉬 크림치즈 1.8kg / 덴마크', '1000', 'c2', 'c2230', 'c2230', 'c2230.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1.8kg, 개입량 : 1개입', ''),
    (231, 231, '매직토핑 907g (식물성,가당,생크림)', '2550', '매직토핑 907g (식물성,가당,생크림)', '1000', 'c2', 'c2231', 'c2231', 'c2231.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 907g, 개입량 : 1개입', ''),
    (270, 270, '선인 에버휩AS 1030g / 가당,생크림,휘핑크림', '2800', '선인 에버휩AS 1030g / 가당,생크림,휘핑크림', '1000', 'c2', 'c2270', 'c2270', 'c2270.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 1030g, 개입량 : 1개입', ''),
    (271, 271, '선인 에버휩 10kg 벌크 / 생크림,휘핑크림', '27000', '선인 에버휩 10kg 벌크 / 생크림,휘핑크림', '1000', 'c2', 'c2271', 'c2271', 'c2271.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 10kg, 개입량 : 1개입', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
