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
    (17, 17, '대두 고운앙금 5kg 55M', '12700', '고운앙금 55M 5kg', '1000', 'b3', 'b317', 'b317', 'b317.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '당도 : 55±2 Bx, 점도 : 170~200, 중량 : 5kg, 유통기한 : 5개월', '고운앙금은 팥과 적강낭콩을 1:1비율로 섞어 껍질을 제거하여 만든 제품으로 입자가 고와 떡이나 빵을 만들때 많이 사용합니다.'),
    (18, 18, '대두 고운앙금 5kg S35M 저당', '13500', '고운앙금 S35M 5kg 저당', '1000', 'b3', 'b318', 'b318', 'b318.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '당도 : 57±2 Bx, 점도 : 170~250, 중량 : 5kg, 유통기한 : 3개월', '고운앙금은 팥과 적강낭콩을 1:1비율로 섞어 껍질을 제거하여 만든 제품으로 입자가 고와 떡이나 빵을 만들때 많이 사용합니다.'),
    (19, 19, '대두 백옥앙금 5kg 52H', '12200', '백옥앙금 52H 5kg', '1000', 'b3', 'b319', 'b319', 'b319.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '당도 : 55±2 Bx, 점도 : 180~230, 중량 : 5kg, 유통기한 : 3개월', '백옥앙금은 흰 강낭콩을 사용한 식염이 투입된 제품이며, 주로 앙금빵, 떡류 등의 원료로 사용합니다.'),
    (20, 20, '대두 백옥앙금 5kg S35M 저당', '12500', '백옥앙금 S35M 5kg 저당', '1000', 'b3', 'b320', 'b320', 'b320.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '당도 : 57±2 Bx, 점도 : 140~240, 중량 : 5kg, 유통기한 : 3개월', '백옥앙금은 흰 강낭콩을 사용한 식염이 투입된 제품이며, 주로 앙금빵, 떡류 등의 원료로 사용합니다.'),
    (21, 21, '대두 춘설앙금 5kg 57H', '12500', '춘설앙금 57H 5kg', '1000', 'b3', 'b321', 'b321', 'b321.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '당도 : 57±2 Bx, 점도 : 270~340, 중량 : 5kg, 유통기한 : 3개월', '춘설앙금은 흰강낭콩을 사용한 식염이 투입되지 않은 제품으로 색이 밝고 물성이 되서 주로 화과자나 구운과자류를 만들떄 사용합니다.'),
    (22, 22, '대두 완두앙금 5kg 57M', '12500', '완두앙금 57M 5kg', '1000', 'b3', 'b322', 'b322', 'b322.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '당도 : 57±2 Bx, 점도 : 120~160, 중량 : 5kg, 유통기한 : 3개월', '완두앙금은 완두콩 거피 후 조린 제품으로 완두의 색상과 풍미를 살린 제품입니다.'),
    (23, 23, '대두 통팥앙금 5kg 57M', '13000', '통팥앙금 57M 5kg', '1000', 'b3', 'b323', 'b323', 'b323.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '당도 : 57±2 Bx, 점도 : 140~180, 중량 : 5kg, 유통기한 : 5개월', '통팥앙금은 거피하지 않고 조림한 제품으로 껍질에 당침투가 적어 고운앙금에 비해 당도가 약합니다.'),
    (24, 24, '대두 통팥앙금 5kg 55M', '13000', '통팥앙금 55M 5kg', '1000', 'b3', 'b324', 'b324', 'b324.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '당도 : 57±2 Bx, 점도 : 140~180, 중량 : 5kg, 유통기한 : 5개월', '통팥앙금은 거피하지 않고 조림한 제품으로 껍질에 당침투가 적어 고운앙금에 비해 당도가 약합니다.'),
    (25, 25, '대두 통팥앙금 5kg S35M 저당', '13000', '통팥앙금 S35M 5kg 저당', '1000', 'b3', 'b325', 'b325', 'b325.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '당도 : 56±1 Bx, 점도 : 140~180, 중량 : 5kg, 유통기한 : 5개월', '통팥앙금S35M은 저감미 제품으로 정백당의 사용량을 줄이고, 저감미 당류(말티톨시럽)을 사용한 제품으로 먹을때 느끼는 당도가 상대적으로 약한 제품입니다. 기존 당도가 낮은 앙금제품의 단점인 냉장유통에 따른 불편을 해소하였습니다.'),
    (26, 26, '대두 호박앙금 5kg 57M', '16500', '호박앙금 57M 5kg', '1000', 'b3', 'b326', 'b326', 'b326.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '당도 : 57±2 Bx, 점도 : 155~185, 중량 : 5kg, 유통기한 : 3개월', '밤호박 페이스트를 이용하여 호박의 풍미가 좋고 색상 또한 진하여 제품 응용시 색과 맛이 뛰어납니다.'),
    (27, 27, '대두 황등앙금 5kg 57M', '16500', '황등앙금 57M 5kg', '1000', 'b3', 'b327', 'b327', 'b327.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '당도 : 57±2 Bx, 점도 : 150~180, 중량 : 5kg, 유통기한 : 3개월', '황등앙금은 백물앙금에 고구마를 혼합하여 조림된 제품입니다.'),
    (28, 28, '대두 강낭콩배기 2kg', '7200', '대두 강낭콩배기 2kg', '1000', 'b3', 'b328', 'b328', 'b328.jpg', '2020-04-17 18:33:40', '불필요', '실온보관', '중량 : 2kg, 유통기한 : 12개월', '콩 고유의 색상과 맛을 그대로 살려 곡물의 형태가 변형되지 않게 당절임한 제품입니다. 삶은 후 당침을 하여 살균처리한 제품으로 상온에서 장기유통이 가능합니다.(미개봉시) 배기 내부까지 당침이 균일합니다. 껍질이 부드러워 떡 제조시 쉽게 활용 가능합니다.'),
    (29, 29, '대두 팥배기 2kg', '7200', '대두 팥배기 2kg', '1000', 'b3', 'b329', 'b329', 'b329.jpg', '2020-04-17 18:33:40', '불필요', '실온보관', '당도 : 57~60 Brix, 중량 : 2kg, 유통기한 : 6개월', '콩 고유의 색상과 맛을 그대로 살려 곡물의 형태가 변형되지 않게 당절임한 제품입니다. 삶은 후 당침을 하여 살균처리한 제품으로 실온에서 장기유통이 가능합니다.(미개봉시) 배기 내부까지 당침이 균일합니다. 껍질이 부드러워 떡,빵 제조 시 쉽게 활용 가능합니다.'),
    (30, 30, '대두 완두배기 2kg', '7200', '대두 완두배기 2kg', '1000', 'b3', 'b330', 'b330', 'b330.jpg', '2020-04-17 18:33:40', '불필요', '실온보관', '당도 : 66~68 Brix, 중량 : 2kg, 유통기한 : 3개월', '콩 고유의 색상과 맛을 그대로 살려 곡물의 형태가 변형되지 않게 당절임한 제품입니다. 배기 내부까지 당침이 균일합니다. 껍질이 부드러워 떡,빵 제조 시 쉽게 활용 가능합니다.'),
    (31, 31, '대두 검정배기 2kg', '7400', '대두 검정배기 2kg', '1000', 'b3', 'b331', 'b331', 'b331.jpg', '2020-04-17 18:33:40', '불필요', '실온보관', '당도 : 58~60 Brix, 중량 : 2kg, 유통기한 : 6개월', '배기는 삶은후 당침을 하여 만든 제품으로 껍질이 부드러워 떡이나 빵에 다양한 활용이 가능합니다.'),
    (32, 32, '대두 강력쌀가루 (수입) 15kg', '35800', '대두 강력쌀가루 (수입) 15kg', '1000', 'b1', 'b132', 'b132', 'b132.jpg', '2020-04-17 18:33:40', '불필요', '실온보관', '중량 : 15kg, 유통기한 : 1년', '햇쌀마루 쌀가루는 전통 방식 그대로 만들어져 다양하고 맛있는 제품을 만들 수 있습니다. 부드럽고 담백하여 쫄깃합니다. 수분함량이 높아 동일 중량 반죽시 실제 원료의 투입량이 줄어듭니다. 1차발효 및 휴지 공정이 없어 제조시간이 단축됩니다. (발효시간:1시간, 휴지시간:10분 단축)'),
    (33, 33, '대두 강력쌀가루 (국산) 15kg', '44000', '대두 강력쌀가루 (국산) 15kg', '1000', 'b1', 'b133', 'b133', 'b133.jpg', '2020-04-17 18:33:40', '불필요', '실온보관', '중량 : 15kg, 유통기한 : 1년', '햇쌀마루 쌀가루는 전통 방식 그대로 만들어져 다양하고 맛있는 제품을 만들 수 있습니다. 부드럽고 담백하여 쫄깃합니다. 수분함량이 높아 동일 중량 반죽시 실제 원료의 투입량이 줄어듭니다. 1차발효 및 휴지 공정이 없어 제조시간이 단축됩니다. (발효시간:1시간, 휴지시간:10분 단축)'),
    (34, 34, '대두 박력쌀가루 15kg', '29500', '대두 박력쌀가루 15kg', '1000', 'b1', 'b134', 'b134', 'b134.jpg', '2020-04-17 18:33:40', '불필요', '실온보관', '중량 : 15kg, 유통기한 : 1년', '햇쌀마루 쌀가루는 전통방식 그대로 만들어져 다양하고 맛있는 제품을 만들 수 있습니다. 쌀가루의 입자가 균일하여 밀가루의 가공적성과 유사합니다. 쌀함량 100%로써 쌀의 풍미가 좋습니다. 과자류 외에 롤케익, 쉬폰케익, 카스텔라, 찜카스테라 등 다양하게 응용할 수 있습니다. 촉촉하고 부드러운 식감을 느낄 수 있습니다. 볼륨성이 좋아집니다.'),
    (35, 35, '대두 박력쌀가루 (국산) 15kg', '34800', '대두 박력쌀가루 (국산) 15kg', '1000', 'b1', 'b135', 'b135', 'b135.jpg', '2020-04-17 18:33:40', '불필요', '실온보관', '중량 : 15kg, 유통기한 : 1년', '햇쌀마루 쌀가루는 전통방식 그대로 만들어져 다양하고 맛있는 제품을 만들 수 있습니다. 쌀가루의 입자가 균일하여 밀가루의 가공적성과 유사합니다. 쌀함량 100%로써 쌀의 풍미가 좋습니다. 과자류 외에 롤케익, 쉬폰케익, 카스텔라, 찜카스테라 등 다양하게 응용할 수 있습니다. 촉촉하고 부드러운 식감을 느낄 수 있습니다. 볼륨성이 좋아집니다.'),
    (36, 36, '대두 골드강력쌀가루 (국산) 3kg', '12500', '대두 골드강력쌀가루 (국산) 3kg', '1000', 'b1', 'b136', 'b136', 'b136.jpg', '2020-04-17 18:33:40', '불필요', '실온보관', '중량 : 3kg, 유통기한 : 1년', '쌀빵의 품질유지기한이 말가루빵과 동일한 수준으로 유지 가능합니다. 쌀빵의 풍미가 향상되었습니다. 최고의 품질을 가진 쌀빵을 만들 수 있습니다. 빵의 조직이 부드럽고 볼륨감이 좋아집니다. 빵의 조직이 균일하여, 촉촉한 식감을 느낄 수 있습니다.'),
    (37, 37, '대두 흑미강력쌀가루 (국산) 15kg', '12500', '대두 흑미강력쌀가루 (국산) 15kg', '1000', 'b1', 'b137', 'b137', 'b137.jpg', '2020-04-17 18:33:40', '불필요', '실온보관', '중량 : 15kg, 유통기한 : 1년', '햇쌀마루 쌀가루는 전통 방식 그대로 만들어져 다양하고 맛있는 제품을 만들 수 있습니다. 흑미빵 전용쌀가루로 기존 밀가루로 만든 모든 쌀빵을 만들 수 있습니다. 내상이 적고 조직이 균일하여, 촉촉한 식감이 특징입니다.'),
    (38, 38, '대두 대두소프트 5kg', '20700', '대두 대두소프트 5kg', '1000', 'b1', 'b138', 'b138', 'b138.jpg', '2020-04-17 18:33:40', '불필요', '실온보관', '중량 : 5kg, 유통기한 : 1년', '대두 PINE SOFT와 202를 혼합된 프리믹스입니다. 부드럽고 쫄깃한 식감이 오래 유지 되도록 도움을 주는 첨가제입니다. 제품의 보수보형 유지가 뛰어납니다.'),
    (39, 39, '대두 파인소프트 T 10kg', '31300', '대두 파인소프트 T 10kg', '1000', 'b1', 'b139', 'b139', 'b139.jpg', '2020-04-17 18:33:40', '불필요', '실온보관', '중량 : 10kg, 유통기한 : 년', '빵, 케익 등 과자류의 식감을 한층 더 부드럽고 쫄깃하게 해주며, 수분이탈, 노화등을 막아줍니다.'),
    (40, 40, '대두 파인소프트 202 2kg', '12500', '대두 파인소프트 202 2kg', '1000', 'b1', 'b140', 'b140', 'b140.jpg', '2020-04-17 18:33:40', '불필요', '실온보관', '중량 : 15kg, 유통기한 : 년', ''),
    (41, 41, '대두 파인소프트 C 2kg', '27000', '대두 파인소프트 C 2kg', '1000', 'b1', 'b141', 'b141', 'b141.jpg', '2020-04-17 18:33:40', '불필요', '실온보관', '중량 : 15kg, 유통기한 : 년', ''),
    (76, 76, '아이엠에그 난황 국산 1kg', '7800', '아이엠에그 난황 국산 1kg', '1000', 'c4', 'c476', 'c476', 'c476.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 1kg, 개입량 : 1개입, 원산지 : 국내산', '드레싱류, 마요네즈, 아이스크림류, 머스타드, 제과, 제빵 등 사용.'),
    (77, 77, '아이엠에그 난백 국산 1kg', '4700', '아이엠에그 난백 국산 1kg', '1000', 'c4', 'c477', 'c477', 'c477.jpg', '2020-04-17 18:33:40', '필요', '냉동보관', '내용량 : 1kg, 개입량 : 1개입, 원산지 : 국내산', '드레싱류, 마요네즈, 아이스크림류, 머스타드, 제과, 제빵 등 사용.'),
    (83, 83, '대두 햇쌀마루 골드중력쌀가루 (국산) 3kg', '12200', '대두 골드중력쌀가루 (국산) 3kg', '1000', 'b1', 'b183', 'b183', 'b183.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 3kg, 개입량 : 1개입, 용도 : 쿠키, 케익시트, 롤케익등의 소프트 계열의 빵', '밀가루에 비해 보습력이 뛰어나 빵의 촉촉함이 오래 지속되며, 부드러운 롤케익, 케익시트, 카스텔라, 단과자류등의 소프트 계열의 빵에 적합합니다. '),
    (84, 84, '대두 햇쌀마루 가루멥쌀 (국산) 1kg', '2500', '대두 햇쌀마루 가루멥쌀 1kg', '1000', 'b1', 'b184', 'b184', 'b184.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입, 용도 : 설기, 송편, 시루떡, 절편 등', '고운 멥쌀가루로 부드러운 식감을 주며, 떡의 볼륨감이 올라가며, 노화시간이 연장됩니다.'),
    (85, 85, '대두 햇쌀마루 가루찹쌀 (국산) 1kg', '5500', '대두 햇쌀마루 가루찹쌀 (국산) 1kg', '1000', 'b1', 'b185', 'b185', 'b185.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입, 용도 : 찰떡, 인절미, 경단 등', '찰떡 고유의 쫄깃하고 부드러운 풍미와 식감을 느낄수 있습니다.'),
    (86, 86, '대두 햇쌀마루 빵이되는 현미가루 (국산) 3kg', '13000', '대두 햇쌀마루 빵이되는 현미가루 (국산) 3kg', '1000', 'b1', 'b186', 'b186', 'b186.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 3kg, 개입량 : 1개입, 용도 : 찰떡, 인절미, 경단 등', '찰떡 고유의 쫄깃하고 부드러운 풍미와 식감을 느낄수 있습니다.'),
    (87, 87, '대두 햇쌀마루 도너츠파인찹쌀 3kg', '14500', '대두 햇쌀마루 도너츠파인찹쌀 3kg', '1000', 'b1', 'b187', 'b187', 'b187.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 3kg, 개입량 : 1개입, 용도 : 찹쌀도너츠 등', '기름 흡수가 적고 쫄깃하면서 부드러운 식감이 납니다.'),
    (88, 88, '대두 화과방 우리통팥 2kg - 국산팥', '13000', '대두 화과방 우리통팥 2kg - 국산팥', '1000', 'b7', 'b788', 'b788', 'b788.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 2kg, 개입량 : 1개입', ''),
    (89, 89, '오뚜기 콤비 쇼팅 4.5kg - 쇼트닝', '8200', '오뚜기 콤비 쇼팅 4.5kg - 쇼트닝', '1000', 'c1', 'c189', 'c189', 'c189.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 4/5kg, 개입량 : 1개입', ''),
    (90, 90, '대두 햇쌀마루 홍국쌀가루 (국산) 1kg', '36900', '대두 햇쌀마루 홍국쌀가루 (국산) 1kg', '1000', 'b1', 'b190', 'b190', 'b190.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (91, 91, '메디락 골드 1kg', '3200', '메디락 골드 1kg', '1000', 'b4', 'b491', 'b491', 'b491.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (92, 92, '이든타운 단호박분말 1kg', '7900', '이든타운 단호박분말 1kg', '1000', 'b1', 'b192', 'b192', 'b192.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (93, 93, '코알라 하이얀 빵가루 1kg', '2880', '코알라 하이얀 빵가루 1kg', '1000', 'b1', 'b193', 'b193', 'b193.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (94, 94, '선인 딸기레진 1kg', '12900', '선인 딸기레진 1kg', '1000', 'b5', 'b594', 'b594', 'b594.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (95, 95, '선인 녹차레진 1kg', '12900', '선인 녹차레진 1kg', '1000', 'b5', 'b595', 'b595', 'b595.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (96, 96, '선인 옥수수레진 1kg', '12900', '선인 옥수수레진 1kg', '1000', 'b5', 'b596', 'b596', 'b596.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (97, 97, '선인 메론레진 1kg', '12900', '선인 메론레진 1kg', '1000', 'b5', 'b597', 'b597', 'b597.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (98, 98, '선인 바나나레진 1kg', '12900', '선인 바나나레진 1kg', '1000', 'b5', 'b598', 'b598', 'b598.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (99, 99, '선인 블루베리레진 1kg', '12900', '선인 블루베리레진 1kg', '1000', 'b5', 'b599', 'b599', 'b599.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (100, 100, '선인 포도레진 1kg', '12900', '선인 포도레진 1kg', '1000', 'b5', 'b5100', 'b5100', 'b5100.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (101, 101, '맥선 중력1등 밀가루 20kg - 다목적용,미국산', '17500', '맥선 중력1등 밀가루 20kg - 다목적용,미국산', '1000', 'b1', 'b1101', 'b1101', 'b1101.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 20kg, 개입량 : 1개입', ''),
    (102, 102, '맥선 박력1등 밀가루 20kg', '18500', '맥선 박력1등 밀가루 20kg', '1000', 'b1', 'b1102', 'b1102', 'b1102.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 20kg, 개입량 : 1개입', ''),
    (103, 103, '맥선 박력1등 밀가루 20kg - 제빵전용분', '15900', '맥선 박력1등 밀가루 20kg - 제빵전용분', '1000', 'b1', 'b1103', 'b1103', 'b1103.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 20kg, 개입량 : 1개입', ''),
    (104, 104, '맥선 유기농 강력 1등 밀가루 20kg - 제빵전용', '42000', '맥선 유기농 강력 1등급 밀가루 20kg - 제빵전용', '1000', 'b1', 'b1104', 'b1104', 'b1104.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 20kg, 개입량 : 1개입', ''),
    (105, 105, '맥선 유기농 중력 1등 밀가루 20kg', '40500', '맥선 유기농 중력 1등 밀가루 20kg', '1000', 'b1', 'b1105', 'b1105', 'b1105.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 20kg, 개입량 : 1개입', ''),
    (106, 106, '맥선 유기농 박력 1등 밀가루 20kg', '40500', '맥선 유기농 박력 1등 밀가루 20kg', '1000', 'b1', 'b1106', 'b1106', 'b1106.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 20kg, 개입량 : 1개입', ''),
    (107, 107, '대한제분 암소 박력 밀가루 다목적용 20kg 1등급', '19800', '대한제분 암소 박력 밀가루 다목적용 20kg 1등급', '1000', 'b1', 'b1107', 'b1107', 'b1107.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 20kg, 개입량 : 1개입', ''),
    (108, 108, '대한제분 코끼리 강력 밀가루 제과제빵용 20kg 1등급', '20800', '대한제분 코끼리 강력 밀가루 제과제빵용 20kg 1등급', '1000', 'b1', 'b1108', 'b1108', 'b1108.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 20kg, 개입량 : 1개입', ''),
    (109, 109, '큐원 강력밀가루 20kg', '23500', '큐원 강력밀가루 20kg', '1000', 'b1', 'b1109', 'b1109', 'b1109.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 20kg, 개입량 : 1개입', ''),
    (110, 110, '큐원 박력밀가루 20kg', '21100', '큐원 박력밀가루 20kg', '1000', 'b1', 'b1110', 'b1110', 'b1110.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 20kg, 개입량 : 1개입', ''),
    (111, 111, '큐원 중력밀가루 20kg - 다목적용', '14900', '큐원 중력밀가루 20kg - 다목적용', '1000', 'b1', 'b1111', 'b1111', 'b1111.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 20kg, 개입량 : 1개입', ''),
    (112, 112, '큐원 갈색설탕 15kg', '24400', '큐원 갈색설탕 15kg', '1000', 'b2', 'b2112', 'b2112', 'b2112.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 15kg, 개입량 : 1개입', ''),
    (113, 113, '큐원 흑설탕 15kg', '25500', '큐원 흑설탕 15kg', '1000', 'b2', 'b2113', 'b2113', 'b2113.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 15kg, 개입량 : 1개입', ''),
    (114, 114, '큐원 하얀설탕 15kg', '15500', '큐원 하얀설탕 15kg', '1000', 'b2', 'b2114', 'b2114', 'b2114.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 15kg, 개입량 : 1개입', ''),
    (115, 115, '큐원 분당 20kg', '32800', '큐원 분당 20kg', '1000', 'b2', 'b2115', 'b2115', 'b2115.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 20kg, 개입량 : 1개입', ''),
    (116, 116, '자라메 설탕 1kg', '8000', '자라메 설탕 1kg', '1000', 'b2', 'b2116', 'b2116', 'b2116.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (117, 117, '큐원 하얀설탕 3kg', '4000', '큐원 분당 20kg', '1000', 'b2', 'b2117', 'b2117', 'b2117.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 3kg, 개입량 : 1개입', ''),
    (118, 118, '큐원 갈색설탕 1kg', '1950', '큐원 갈색설탕 1kg', '1000', 'b2', 'b2118', 'b2118', 'b2118.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (119, 119, '큐원 흑설탕 1kg', '1950', '큐원 흑설탕 1kg', '1000', 'b2', 'b2119', 'b2119', 'b2119.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (120, 120, '꼬미다 슈가파우더 3kg', '4580', '꼬미다 슈가파우더 3kg', '1000', 'b2', 'b2120', 'b2120', 'b2120.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 3kg, 개입량 : 1개입', ''),
    (121, 121, '칼리바우트 다크커버춰 초콜릿 2.5kg (카카오 57.7%)', '31000', '칼리바우트 다크커버춰 초콜릿 2.5kg (카카오 57.7%)', '1000', 'e1', 'e1121', 'e1121', 'e1121.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 2.5kg, 개입량 : 1개입', ''),
    (122, 122, '칼리바우트 화이트커버춰 초콜릿 2.5kg', '34500', '칼리바우트 화이트커버춰 초콜릿 2.5kg', '1000', 'e1', 'e1122', 'e1122', 'e1122.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 2.5kg, 개입량 : 1개입', ''),
    (123, 123, '아몬드슬라이스 1kg (미국/캘리포니아)', '12500', '아몬드슬라이스 1kg (미국/캘리포니아)', '1000', 'd1', 'd1123', 'd1123', 'd1123.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (124, 124, '백아몬드슬라이스 1kg (미국/캘리포니아) / 아몬드슬라이스', '13100', '꼬미다 슈가파우더 3kg', '1000', 'd1', 'd1124', 'd1124', 'd1124.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (125, 125, '햇 호두분태 1kg (미국/캘리포니아)', '12400', '햇 호두분태 1kg (미국) / 호두 햇호두 캘리포니아호두분태', '1000', 'd1', 'd1125', 'd1125', 'd1125.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (126, 126, '다이아몬드 호두분태 벌크 캘리포니아 (13.61kg)', '180000', '다이아몬드 캘리포니아 호두분태 벌크 (13.61kg)', '1000', 'd1', 'd1126', 'd1126', 'd1126.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 13.61kg, 개입량 : 1개입', ''),
    (127, 127, '블루다이아몬드 아몬드슬라이스 벌크 캘리포니아 (11.34kg)', '138000', '블루다이아몬드 아몬드슬라이스 벌크 (11.34kg)', '1000', 'd1', 'd1127', 'd1127', 'd1127.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 11.34kg, 개입량 : 1개입', ''),
    (128, 128, '햇 호두 1/4태 1kg (미국/캘리포니아)', '10800', '캘리포니아 햇 호두 1/4태 1kg (미국)', '1000', 'd1', 'd1128', 'd1128', 'd1128.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (129, 129, '햇 아몬드분태 1kg (미국/캘리포니아)', '13600', '햇 아몬드분태 1kg (캘리포니아 미국) 아몬드 분태', '1000', 'd1', 'd1129', 'd1129', 'd1129.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (130, 130, '햇 호두반태 1kg (미국/캘리포니아)', '12700', '캘리포니아 햇 호두반태 1kg (미국)', '1000', 'd1', 'd1130', 'd1130', 'd1130.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (131, 131, '햇 통아몬드 1kg (미국/캘리포니아)', '11300', '햇 통아몬드 1kg (미국.캘리포니아)', '1000', 'd1', 'd1131', 'd1131', 'd1131.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (132, 132, '아몬드분태 10kg (캘리포니아.미국)', '110400', '아몬드분태 10kg (캘리포니아.미국)', '1000', 'd1', 'd1132', 'd1132', 'd1132.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 10kg, 개입량 : 1개입', ''),
    (133, 133, '풀그린아몬드가루 1kg (아몬드95%+소맥분5%)', '9300', '풀그린아몬드가루 1kg (아몬드95%+소맥분5%)', '1000', 'd1', 'd1133', 'd1133', 'd1133.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (134, 134, '풀그린 아몬드분말 벌크 11.34kg (아몬드95%,소맥분5%)', '97500', '풀그린 아몬드분말 벌크 11.34kg (아몬드95%,소맥분5%)', '1000', 'd1', 'd1134', 'd1134', 'd1134.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 11.34kg, 개입량 : 1개입', ''),
    (135, 135, '냉동 크랜베리 500g', '3600', '냉동 크랜베리 500g', '1000', 'd2', 'd2136', 'd2136', 'd2136.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 500g, 개입량 : 1개입', ''),
    (136, 136, '반건조무화과 2kg (터키)', '21400', '반건조무화과 2kg (터키)', '1000', 'd2', 'd2136', 'd2136', 'd2136.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 2kg, 개입량 : 1개입', ''),
    (137, 137, '선인 건조크랜베리 1kg', '7600', '선인 건조크랜베리 1kg', '1000', 'd2', 'd2137', 'd2137', 'd2137.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (138, 138, '설정식품 사과다이스 3kg (고형량1.6kg/국내산)', '11000', '설정식품 사과다이스 3kg (고형량1.6kg/국내산)', '1000', 'd2', 'd2138', 'd2138', 'd2138.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 3kg, 개입량 : 1개입', ''),
    (139, 139, '설정식품 웰스피아 고구마다이스 3kg', '11000', '설정식품 웰스피아 고구마다이스 3kg', '1000', 'd2', 'd2139', 'd2139', 'd2139.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 3kg, 개입량 : 1개입', ''),
    (140, 140, '햇 호박씨 1kg', '6200', '햇 호박씨 1kg', '1000', 'd3', 'd3140', 'd3140', 'd3140.jpg', '2020-04-15 18:33:40', '불필요', '서늘한곳에 보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (141, 141, '해바라기씨 1kg (미국산)', '4900', '해바라기씨 1kg (미국산)', '1000', 'd3', 'd3141', 'd3141', 'd3141.jpg', '2020-04-15 18:33:40', '불필요', '서늘한곳에 보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (142, 142, '사프 드라이이스트 레드 500g (저당용)', '4450', '사프 드라이이스트 레드 500g (저당용)', '1000', 'b3', 'b3142', 'b3142', 'b3142.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 500g, 개입량 : 1개입', ''),
    (143, 143, '사프 드라이이스트 골드 500g (고당용)', '4450', '사프 드라이이스트 골드 500g (고당용)', '1000', 'b3', 'b3143', 'b3143', 'b3143.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 500g, 개입량 : 1개입', ''),
    (144, 144, '제니코 생이스트 500g (국산)', '2100', '제니코 생이스트 500g (국산)', '1000', 'b3', 'b3144', 'b3144', 'b3144.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 500g, 개입량 : 1개입', ''),
    (145, 145, '제니코 베이킹파우더 블루(포뮬러2) 300g', '1150', '제니코 베이킹파우더 블루(포뮬러2) 300g', '1000', 'b3', 'b3145', 'b3145', 'b3145.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 300g, 개입량 : 1개입', ''),
    (146, 146, '선인 사프 비비제이 500g (BBJ)', '8400', '선인 사프 비비제이 500g (BBJ)', '1000', 'b3', 'b3146', 'b3146', 'b3146.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 500g, 개입량 : 1개입', ''),
    (147, 147, '신광 베이킹소다 1kg', '1500', '신광 베이킹소다 1kg', '1000', 'b3', 'b3147', 'b3147', 'b3147.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (148, 148, '제원 데코젤 미로와 5kg', '28000', '제원 데코젤 미로와 5kg', '1000', 'b3', 'b3148', 'b3148', 'b3148.jpg', '2020-04-15 18:33:40', '불필요', '서늘한곳에 보관', '내용량 : 5kg, 개입량 : 1개입', ''),
    (149, 149, '퓨라토스 S-500 제빵계량제 500g', '3400', '퓨라토스 S-500 제빵계량제 500g', '1000', 'b3', 'b3149', 'b3149', 'b3149.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 500g, 개입량 : 1개입', ''),
    (150, 150, '분말젤라틴 450g', '10500', '분말젤라틴 450g', '1000', 'b3', 'b3150', 'b3150', 'b3150.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 450g, 개입량 : 1개입', ''),
    (151, 151, '큐원 물엿 5kg', '10500', '큐원 물엿 5kg', '1000', 'b4', 'b4151', 'b4151', 'b4151.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 5kg, 개입량 : 1개입', ''),
    (152, 152, '후버옐로우머스터드/머스타드 680g', '2650', '후버옐로우머스터드/머스타드 680g', '1000', 'b5', 'b5152', 'b5152', 'b5152.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 450g, 개입량 : 1개입', ''),
    (153, 153, '리치스 슬라이스 오이피클 3kg', '5630', '리치스 슬라이스 오이피클 3kg', '1000', 'b7', 'b7153', 'b7153', 'b7153.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 3kg, 개입량 : 1개입', ''),
    (154, 154, 'ANCHOR 앵커버터 454g (무염/유크림100%)', '5500', 'ANCHOR 앵커버터 454g (무염/유크림100%)', '1000', 'c1', 'c1154', 'c1154', 'c1154.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 454g, 개입량 : 1개입', ''),
    (155, 155, '엘르앤비르고메버터 500g 무염버터 발효버터 최상급버터', '9900', '엘르앤비르고메버터 500g 무염버터 발효버터 최상급버터', '1000', 'c1', 'c1155', 'c1155', 'c1155.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 500g, 개입량 : 1개입', ''),
    (156, 156, '[무료배송] 앵커버터1박스 9.08kg (454gx20개)', '106000', '[무료배송] 앵커버터1박스 9.08kg (454gx20개)', '1000', 'c1', 'c1156', 'c1156', 'c1156.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 9.08kg, 개입량 : 20개입', ''),
    (157, 157, '엘르앤비르 엑스트라드라이버터 1kg (프랑스산 버터시트 판버터)', '18500', '엘르앤비르 엑스트라드라이버터 1kg (프랑스산 버터시트 판버터)', '1000', 'c1', 'c1157', 'c1157', 'c1157.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (158, 158, '엘르앤비르 엑스트라 드라이버터 1박스 (1kg *10개입) (프랑스버터 고메버터시트 판버터)', '184900', '엘르앤비르 엑스트라 드라이버터 1박스 (1k *10개입) (프랑스버터 고메버터시트 판버터)', '1000', 'c1', 'c1158', 'c1158', 'c1158.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 10kg, 개입량 : 10개입', ''),
    (159, 159, '오뚜기 브레드5000 마가린 4.5kg', '7790', '오뚜기 브레드5000 마가린 4.5kg', '1000', 'c1', 'c1159', 'c1159', 'c1159.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 4.5kg, 개입량 : 1개입', ''),
    (160, 160, '그랜드500 FREE _4.5kg (중급다목적)', '17300', '그랜드500 FREE _4.5kg (중급다목적)', '1000', 'c1', 'c1160', 'c1160', 'c1160.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 4.5kg, 개입량 : 1개입', ''),
    (161, 161, '선인 에버휩 1030g (식물성,가당 휘핑크림,생크림)', '2800', '선인 에버휩 1030g (식물성,가당 휘핑크림,생크림)', '1000', 'c2', 'c2161', 'c2161', 'c2161.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 1030g, 개입량 : 1개입', ''),
    (162, 162, '뉴 골드라벨 1박스 (1030g*12개입) / 식물성 가당 생크림', '36240', '뉴 골드라벨 1박스 (1030g*12개입) / 식물성 가당 생크림', '1000', 'c2', 'c2162', 'c2162', 'c2162.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 12.36kg, 개입량 : 12개입', ''),
    (163, 163, '뉴 골드라벨 1030g / 식물성 가당 생크림', '17300', '뉴 골드라벨 1030g / 식물성 가당 생크림', '1000', 'c2', 'c2163', 'c2163', 'c2163.jpg', '2020-04-15 18:33:40', '필요', '냉동보관', '내용량 : 1030g, 개입량 : 1개입', ''),
    (164, 164, '알라 동물성 휘핑크림 1L (무가당) / 코스트코 생크림,덴마크산', '6950', '알라 동물성 휘핑크림 1L (무가당) / 코스트코 생크림,덴마크산', '1000', 'c2', 'c2164', 'c2164', 'c2164.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (165, 165, '선인 가나슈 필링 1kg / 초콜릿크림, 와플잼', '3700', '선인 가나슈 필링 1kg / 초콜릿크림, 와플잼', '1000', 'c2', 'c2165', 'c2165', 'c2165.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (166, 166, '선인 크림치즈무스 1kg / 스위트치즈스프레드,크림치즈,치즈필링', '8040', '선인 크림치즈무스 1kg / 스위트치즈스프레드,크림치즈,치즈필링', '1000', 'c2', 'c2166', 'c2166', 'c2166.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (167, 167, '매일휘핑크림 38% 1L (국산생크림, 매일동물성생크림)', '8200', '매일휘핑크림 38% 1L (국산생크림, 매일동물성생크림)', '1000', 'c2', 'c2167', 'c2167', 'c2167.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (168, 168, '온탑 생크림 340g (식물성) / 아이스박스 필수구매', '3300', '온탑 생크림 340g (식물성) / 아이스박스 필수구매', '1000', 'c2', 'c2168', 'c2168', 'c2168.jpg', '2020-04-15 18:33:40', '필요', '냉ehd보관', '내용량 : 340g, 개입량 : 1개입', ''),
    (169, 169, '사워크림 LP 1L / 샤워크림 사우어크림', '6100', '사워크림 LP 1L / 샤워크림 사우어크림', '1000', 'c2', 'c2169', 'c2169', 'c2169.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (170, 170, '끼리크림치즈 1kg (프랑스크림치즈)', '15200', '끼리크림치즈 1kg (프랑스크림치즈)', '1000', 'c2', 'c2170', 'c2170', 'c2170.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (171, 171, '끼리크림치즈 1박스 (1kg x 12개입)', '182400', '끼리크림치즈 1박스 (1kg x 12개입)', '1000', 'c2', 'c2171', 'c2171', 'c2171.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 12kg, 개입량 : 12개입', ''),
    (172, 172, '끼리크림치즈 1kg (프랑스크림치즈)', '15200', '끼리크림치즈 1kg (프랑스크림치즈)', '1000', 'c3', 'c3172', 'c3172', 'c3172.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (173, 173, '매일 베이커리슬라이스치즈 50 II 100매 1.8kg / 체다치즈', '13900', '매일 베이커리슬라이스치즈 50 II 100매 1.8kg / 체다치즈', '1000', 'c3', 'c3173', 'c3173', 'c3173.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1.8kg, 개입량 : 1개입', ''),
    (174, 174, '매일 고소한 롤치즈 1kg /매일롤치즈', '10500', '매일 고소한 롤치즈 1kg /매일롤치즈', '1000', 'c3', 'c3174', 'c3174', 'c3174.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (175, 175, '선인 크림치즈무스 1kg / 스위트치즈스프레드', '8040', '선인 크림치즈무스 1kg / 스위트치즈스프레드', '1000', 'c3', 'c3175', 'c3175', 'c3175.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (176, 176, '베이커리 롤치즈 1kg /서울롤치즈', '11500', '베이커리 롤치즈 1kg /서울롤치즈', '1000', 'c3', 'c3176', 'c3176', 'c3176.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 1kg, 개입량 : 1개입', ''),
    (177, 177, '매일연유 500g (가당)', '3500', '매일연유 500g (가당)', '1000', 'c5', 'c5177', 'c5177', 'c5177.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 500g, 개입량 : 1개입', ''),
    (178, 178, '서강 크리밀 연유 500g / 튜브연유', '2990', '선인 크림치즈무스 1kg / 스위트치즈스프레드', '1000', 'c5', 'c5178', 'c5178', 'c5178.jpg', '2020-04-15 18:33:40', '필요', '냉장보관', '내용량 : 500g, 개입량 : 1개입', ''),
    (179, 179, '꼬미다슈가파우더 3kg', '4580', '꼬미다슈가파우더 3kg', '1000', 'b2', 'b2179', 'b2179', 'b2179.jpg', '2020-04-15 18:33:40', '불필요', '실온보관', '내용량 : 3kg, 개입량 : 1개입', ''),
]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")