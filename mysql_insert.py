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
    (1, 1, 'a11', '150', 'a11', '4', 'a1', 'a11', 'a11', 'a11.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (2, 2, 'a12', '150', 'a12', '4', 'a1', 'a11', 'a11', 'a11.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (3, 3, 'a13', '150', 'a13', '4', 'a1', 'a11', 'a11', 'a11.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (4, 4, 'a14', '150', 'a14', '4', 'a1', 'a11', 'a11', 'a11.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (5, 5, 'a15', '150', 'a15', '4', 'a1', 'a11', 'a11', 'a11.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (6, 6, 'a21', '150', 'a21', '4', 'a2', 'a21', 'a21', 'a21.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (7, 7, 'a22', '150', 'a22', '4', 'a2', 'a21', 'a21', 'a21.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (8, 8, 'a23', '150', 'a23', '4', 'a2', 'a21', 'a21', 'a21.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (9, 9, 'a24', '150', 'a24', '4', 'a2', 'a21', 'a21', 'a21.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (10, 10, 'a25', '150', 'a25', '4', 'a2', 'a21', 'a21', 'a21.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (11, 11, 'a31', '150', 'a31', '4', 'a3', 'a31', 'a31', 'a31.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (12, 12, 'a32', '150', 'a32', '4', 'a3', 'a31', 'a31', 'a31.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (13, 13, 'a33', '150', 'a33', '4', 'a3', 'a31', 'a31', 'a31.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (14, 14, 'a34', '150', 'a34', '4', 'a3', 'a31', 'a31', 'a31.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (15, 15, 'a35', '150', 'a35', '4', 'a3', 'a31', 'a31', 'a31.jpg', '2018-09-20 07:10:40', '필요', '냉동식품', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
    (16, 16, 'icebox', '1500', 'add icebox', '100', 'icebox', 'icebox', 'icebox', 'icebox.jpg', '2018-09-20 07:10:40', '필요', 'aa', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.','Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididuorum.'),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
