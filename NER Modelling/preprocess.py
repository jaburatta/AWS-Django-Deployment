import spacy
from spacy.tokens import DocBin

nlp = spacy.blank("en")
training_data = [
    ('We ordered 1000 new spicy stock for 583630 naira', {
     'entities': [(11, 15, 'QUANTITY'), (20, 31, 'ITEM'), (36, 42, 'PRICE')]}),
    ('We bought 70 bags for 277370 naira', {'entities': [
     (10, 12, 'QUANTITY'), (13, 17, 'ITEM'), (22, 28, 'PRICE')]}),
    ('school fees 30000 naira', {'entities': [(0, 11, 'ITEM'), (12, 17, 'PRICE')]}),
    ('47 new spicy stock worth 282330 naira were purchased', {
     'entities': [(0, 2, 'QUANTITY'), (7, 18, 'ITEM'), (25, 31, 'PRICE')]}),
    ('We bought 25 cartons of noodles for 482900 naira', {
     'entities': [(10, 12, 'QUANTITY'), (24, 31, 'ITEM'), (36, 42, 'PRICE')]}),
    ('120 litres of kerosene bought for 428120 naira', {
     'entities': [(0, 3, 'QUANTITY'), (14, 22, 'ITEM'), (34, 40, 'PRICE')]}),
    ('95 cartons of noodles were purchased for 234900 naira', {
     'entities': [(0, 2, 'QUANTITY'), (3, 21, 'ITEM'), (41, 47, 'PRICE')]}),
    ('We sold 2 set of cutleries for 314450 naira', {'entities': [
     (8, 9, 'QUANTITY'), (17, 26, 'ITEM'), (31, 37, 'PRICE')]}),
    ('We bought 1 litre of kerosene for 387870 naira', {
     'entities': [(10, 11, 'QUANTITY'), (21, 29, 'ITEM'), (34, 40, 'PRICE')]}),
    ('32 litres of kerosene worth 393360 naira was sold this morning', {
     'entities': [(0, 2, 'QUANTITY'), (13, 21, 'ITEM'), (28, 34, 'PRICE')]}),
    # ('We procured 12 new spicy stock for 282330 naira', {'entities': [(15, 26, 'ITEM'), (31, 37, 'PRICE')]}),
    ('77 new baskets worth 397670 naira was paid for by the customer', {'entities': [(0, 2, 'QUANTITY'), (7, 14, 'ITEM'), (21, 27, 'PRICE')]}),
    ('We sold 1 new basket worth 154900 naira', {'entities': [
     (8, 9, 'QUANTITY'), (14, 20, 'ITEM'), (27, 33, 'PRICE')]}),
    ('12 sets of cooking utensils worth 179620 naira bought', {
     'entities': [(0, 2, 'QUANTITY'), (11, 27, 'ITEM'), (34, 40, 'PRICE')]}),
    ('We bought 5 bags for 427770 naira', {'entities': [
     (10, 11, 'QUANTITY'), (12, 16, 'ITEM'), (21, 27, 'PRICE')]}),
    ('264590 naira was paid for 25 cartons of noodles', {
     'entities': [(26, 28, 'QUANTITY'), (29, 47, 'ITEM'), (0, 6, 'PRICE')]}),
    ('we sold 150 loaves of bread for 117,810 Naira this past holiday', {
     'entities': [(8, 11, 'QUANTITY'), (12, 27, 'ITEM'), (32, 39, 'PRICE')]}),
    ('10 organic product worth 67,000 naira was sold last week', {
     'entities': [(0, 2, 'QUANTITY'), (3, 18, 'ITEM'), (25, 31, 'PRICE')]}),
    ('I bought 4 bags of nitrosol worth 60,000 naira', {
     'entities': [(9, 10, 'QUANTITY'), (11, 27, 'ITEM'), (34, 40, 'PRICE')]}),
    ('Clement paid 292580 naira for 1077 wedding cakes', {
     'entities': [(30, 34, 'QUANTITY'), (35, 48, 'ITEM'), (13, 19, 'PRICE')]}),
    ('393360 naira was paid for 14 cartons of noodles', {
     'entities': [(26, 28, 'QUANTITY'), (40, 47, 'ITEM'), (0, 6, 'PRICE')]}),
    ('15 loaves of bread worth 117,810 Naira was bought last week', {
     'entities': [(0, 2, 'QUANTITY'), (3, 18, 'ITEM'), (25, 32, 'PRICE')]}),
    ('we bought 12 tractors for 12000 naira', {'entities': [
     (10, 12, 'QUANTITY'), (13, 21, 'ITEM'), (26, 31, 'PRICE')]}),
    ('I rented 5 cutlasses for 7500 naira', {'entities': [
     (9, 10, 'QUANTITY'), (11, 20, 'ITEM'), (25, 29, 'PRICE')]}),
    ('we paid 12 labourers 120000 naira ', {'entities': [
     (8, 10, 'QUANTITY'), (11, 20, 'ITEM'), (21, 27, 'PRICE')]}),
    ('The management paid 7 staffs 840000 naira as their salary', {
     'entities': [(20, 21, 'QUANTITY'), (22, 28, 'ITEM'), (29, 35, 'PRICE')]}),
    # ('2 fencing tools worth 100000 naira was purchased last week', {'entities': [(0, 2, 'QUANTITY'), (2, 15, 'ITEM'), (22, 28, 'PRICE')]}),
    # ('5 gardening tools purchased at 750000 naira ', {'entities': [(0, 2, 'QUANTITY'), (2, 17, 'ITEM'), (31, 37, 'PRICE')]}),
    ('we rented 3 trucks for 8500 naira', {'entities': [
     (10, 11, 'QUANTITY'), (12, 18, 'ITEM'), (23, 27, 'PRICE')]}),
    ('we bought 12 baskets worth 1750 naira yesterday', {
     'entities': [(10, 12, 'QUANTITY'), (13, 20, 'ITEM'), (27, 31, 'PRICE')]}),
    ('we bought 12 farming tools for 14359 naira', {'entities': [
     (10, 12, 'QUANTITY'), (13, 26, 'ITEM'), (31, 36, 'PRICE')]}),
    ('1 portland cement cost 25000 naira', {'entities': [
     (0, 1, 'QUANTITY'), (2, 17, 'ITEM'), (23, 28, 'PRICE')]}),
    ('we paid 19800 naira for 12 sacks', {'entities': [
     (24, 26, 'QUANTITY'), (27, 32, 'ITEM'), (8, 13, 'PRICE')]}),
    ('we procured 3 chisel at 3500 naira', {'entities': [
     (12, 13, 'QUANTITY'), (14, 20, 'ITEM'), (24, 28, 'PRICE')]}),
    ('4 shovels cost us 15000 naira', {'entities': [
     (0, 1, 'QUANTITY'), (2, 9, 'ITEM'), (18, 23, 'PRICE')]}),
    ('5 labourers got paid 7500 naira for the works', {
     'entities': [(0, 1, 'QUANTITY'), (2, 11, 'ITEM'), (21, 25, 'PRICE')]}),
    ('we sold 35 shovels for 15000 naira', {'entities': [
     (8, 10, 'QUANTITY'), (11, 18, 'ITEM'), (23, 28, 'PRICE')]}),
    ('the customer bought 12 rams for 750000 naira', {'entities': [
     (20, 22, 'QUANTITY'), (23, 27, 'ITEM'), (32, 38, 'PRICE')]}),
    ('we bought 12 packs of sugar for 12000 naira', {'entities': [
     (10, 12, 'QUANTITY'), (22, 27, 'ITEM'), (32, 37, 'PRICE')]}),
    ('22 packs of pasta sold for 3500 naira', {'entities': [
     (0, 2, 'QUANTITY'), (12, 17, 'ITEM'), (27, 31, 'PRICE')]}),
    ('we sold 2 gallons of red oil for 13200 naira', {
     'entities': [(8, 9, 'QUANTITY'), (21, 28, 'ITEM'), (33, 38, 'PRICE')]}),
    ('we bought 2 sacks of cashew nut worth 12450 naira', {
     'entities': [(10, 11, 'QUANTITY'), (21, 31, 'ITEM'), (38, 43, 'PRICE')]}),
    ('The distributor paid for 25 litres of groundnut oil worth 75403 naira', {
     'entities': [(25, 27, 'QUANTITY'), (38, 51, 'ITEM'), (58, 63, 'PRICE')]}),
    ('23 sacks of yam seedlings purchased at 11300 naira', {
     'entities': [(0, 2, 'QUANTITY'), (12, 25, 'ITEM'), (39, 44, 'PRICE')]}),
    ('The church ordered for 5 kegs of palm wine for 15000 naira', {
     'entities': [(23, 24, 'QUANTITY'), (33, 42, 'ITEM'), (47, 52, 'PRICE')]}),
    ('we sold 1 bag of corn seeds for 5000 naira', {'entities': [
     (8, 9, 'QUANTITY'), (17, 27, 'ITEM'), (32, 36, 'PRICE')]}),

    ('I gave chinedu 5000 naira', {
     'entities': [(7, 14, 'ITEM'), (15, 19, 'PRICE')]}),
    ('i sold rice 1000 naira', {'entities': [
     (7, 11, 'ITEM'), (12, 16, 'PRICE')]}),
    ('we bought kerosene 12000 naira', {
     'entities': [(10, 18, 'ITEM'), (19, 24, 'PRICE')]}),
    ('Emeka paid 1500 naira for wire cable', {
     'entities': [(26, 36, 'ITEM'), (11, 15, 'PRICE')]}),
    ('Mama Rashida collected 15000 naira', {
     'entities': [(0, 12, 'ITEM'), (23, 28, 'PRICE')]}),
    ('I bought recharge card 100 naira', {
     'entities': [(9, 22, 'ITEM'), (23, 26, 'PRICE')]}),
    ('Richard sold elubo 1200 naira', {
     'entities': [(13, 18, 'ITEM'), (19, 23, 'PRICE')]}),
    ('1750 naira from customer for last week rice', {
     'entities': [(39, 43, 'ITEM'), (0, 4, 'PRICE')]}),
    ('4300 naira GOTV Decoder', {
     'entities': [(11, 23, 'ITEM'), (0, 4, 'PRICE')]}),
    ('Fridge Repair 8500 naira', {
     'entities': [(0, 13, 'ITEM'), (14, 18, 'PRICE')]}),
    ('I paid Adamu 2300 naira', {
     'entities': [(7, 12, 'ITEM'), (13, 17, 'PRICE')]}),
    ('Moses 5000 naira clipper repairs', {
     'entities': [(17, 32, 'ITEM'), (6, 10, 'PRICE')]}),
    ('Loveth next shop borrowed 300 naira', {
     'entities': [(0, 6, 'ITEM'), (26, 29, 'PRICE')]}),
    ('DSTV Subscription 7500 naira', {
     'entities': [(0, 17, 'ITEM'), (18, 22, 'PRICE')]}),
    ('150000 naira Shop Rent fee', {
     'entities': [(13, 22, 'ITEM'), (0, 6, 'PRICE')]}),
    ('5500 naira for council', {
     'entities': [(15, 22, 'ITEM'), (0, 4, 'PRICE')]}),
    ('mtn card 200 naira', {'entities': [(0, 8, 'ITEM'), (9, 12, 'PRICE')]}),
    ('1500 naira security fee', {
     'entities': [(11, 23, 'ITEM'), (0, 4, 'PRICE')]}),
    ('i rent shovel 3000 naira', {
     'entities': [(7, 13, 'ITEM'), (14, 18, 'PRICE')]}),

    ('75000 naira was paid by the vendor for distribution', {
     'entities': [(39, 51, 'ITEM'), (0, 5, 'PRICE')]}),
    ('cable distributor 2500000 naira', {
     'entities': [(0, 17, 'ITEM'), (18, 25, 'PRICE')]}),
    ('3500 naira for internet Subscription', {
     'entities': [(15, 36, 'ITEM'), (0, 4, 'PRICE')]}),
    ('NEPA bill 4200 naira', {
     'entities': [(0, 9, 'ITEM'), (10, 14, 'PRICE')]}),
    ('1200 naira for PHCN bill', {
     'entities': [(15, 24, 'ITEM'), (0, 4, 'PRICE')]}),
    ('Ankara 3 yards 124000 naira', {'entities': [
     (7, 8, 'QUANTITY'), (0, 6, 'ITEM'), (15, 21, 'PRICE')]}),
    ('190000 naira for satin lace 3 yards', {'entities': [
     (28, 29, 'QUANTITY'), (17, 27, 'ITEM'), (0, 6, 'PRICE')]}),
    ('LG AX-023 Television for 350200 naira', {
     'entities': [(0, 20, 'ITEM'), (25, 31, 'PRICE')]}),
    ('50100 naira for pansaonic air conditioner', {
     'entities': [(16, 41, 'ITEM'), (0, 5, 'PRICE')]}),
    ('760100 naira for Scanfrost AC 2HP', {
     'entities': [(17, 33, 'ITEM'), (0, 6, 'PRICE')]}),
    ('i bought 2 1 Horse Power AC for 320010 naira', {'entities': [
     (9, 10, 'QUANTITY'), (11, 27, 'ITEM'), (32, 38, 'PRICE')]}),
    ('Apple watch series 2 for 99000 naira', {
     'entities': [(0, 20, 'ITEM'), (25, 30, 'PRICE')]}),
    ('i sold 2 Airpod pro for 179000 naira', {'entities': [
     (7, 8, 'QUANTITY'), (9, 19, 'ITEM'), (24, 30, 'PRICE')]}),
    ('Samsung Galaxy tab repairs for 32000 naira', {
     'entities': [(0, 26, 'ITEM'), (31, 36, 'PRICE')]}),
    ('Samsung s9 screen repairs for 62000 naira', {
     'entities': [(0, 10, 'ITEM'), (30, 35, 'PRICE')]}),
    ('I bought 3 Nokia touch pad 13000 naira', {'entities': [
     (9, 10, 'QUANTITY'), (11, 26, 'ITEM'), (27, 32, 'PRICE')]}),
    ('HP mouse sold for 7500 naira', {
     'entities': [(0, 8, 'ITEM'), (18, 22, 'PRICE')]}),
    ('I bought Dell mouse for 12000 naira', {
     'entities': [(9, 19, 'ITEM'), (24, 29, 'PRICE')]}),
    ('I sold 5 computer keyboards for 54000 naira', {'entities': [
     (7, 8, 'QUANTITY'), (9, 27, 'ITEM'), (32, 37, 'PRICE')]}),
    ('Cable distributor 55000 naira', {
     'entities': [(0, 17, 'ITEM'), (18, 23, 'PRICE')]}),
    ('i paid phone accessories distributor 525000 naira', {
     'entities': [(7, 36, 'ITEM'), (37, 43, 'PRICE')]}),
    ('Huawei charger sold for 1200 naira', {
     'entities': [(0, 14, 'ITEM'), (24, 28, 'PRICE')]}),
    ('Lenovo laptop charger sold for 15000 naira', {
     'entities': [(0, 21, 'ITEM'), (31, 36, 'PRICE')]}),
    ('Panasonic Television X0Y2G bought for 130000 naira', {
     'entities': [(0, 26, 'ITEM'), (38, 44, 'PRICE')]}),
    ('4 Dell Projectors 190000 naira', {'entities': [
     (0, 1, 'QUANTITY'), (2, 17, 'ITEM'), (18, 24, 'PRICE')]}),
    ('3 Toshiba Projector screen for 20000 naira sold', {'entities': [
     (0, 1, 'QUANTITY'), (2, 26, 'ITEM'), (31, 36, 'PRICE')]}),
    ('4 yards of satin lace for 12000 naira sold', {'entities': [
     (0, 1, 'QUANTITY'), (11, 21, 'ITEM'), (26, 31, 'PRICE')]}),
    ('54 yards of Aso-Oke received for 1200000 naira', {'entities': [
     (0, 2, 'QUANTITY'), (12, 19, 'ITEM'), (33, 40, 'PRICE')]}),
    ('Aso Oke 4 yards sold at 3000 naira', {'entities': [
     (8, 9, 'QUANTITY'), (0, 7, 'ITEM'), (24, 28, 'PRICE')]}),
    ('3 Phillips pressing iron sold for 34050 naira', {'entities': [
     (0, 1, 'QUANTITY'), (2, 24, 'ITEM'), (34, 39, 'PRICE')]}),
    ('1 Phillips TV sold for 134050 naira', {'entities': [
     (0, 1, 'QUANTITY'), (2, 13, 'ITEM'), (23, 29, 'PRICE')]}),
    ('i sold 1 pressing iron for 5000 naira', {'entities': [
     (7, 8, 'QUANTITY'), (9, 22, 'ITEM'), (27, 31, 'PRICE')]}),
    ('12 dozens of ergonomic chairs sold for 1304500 naira', {'entities': [
     (0, 2, 'QUANTITY'), (13, 29, 'ITEM'), (39, 46, 'PRICE')]}),
    ('1 dozen chairs sold for 45000 naira', {'entities': [
     (0, 1, 'QUANTITY'), (8, 14, 'ITEM'), (24, 29, 'PRICE')]}),
    ('centre table 54020 naira', {
     'entities': [(0, 12, 'ITEM'), (13, 18, 'PRICE')]}),
    ('Office chairs bought for 132070 naira', {
     'entities': [(0, 13, 'ITEM'), (25, 31, 'PRICE')]}),
    ('4 office cabinets sold for 1378295 naira', {'entities': [
     (0, 1, 'QUANTITY'), (2, 17, 'ITEM'), (27, 34, 'PRICE')]}),
    ('3 conference tables sold for 12054030 naira', {'entities': [
     (0, 1, 'QUANTITY'), (2, 19, 'ITEM'), (29, 37, 'PRICE')]}),
    ('iPhone 12 pro sold for 450000 naira', {
     'entities': [(0, 13, 'ITEM'), (23, 29, 'PRICE')]}),
    ('Tecno P90 bought for 123000 naira', {
     'entities': [(0, 9, 'ITEM'), (21, 27, 'PRICE')]}),
    ('4 units of Tecno P2 bought for 23000 naira', {'entities': [
     (0, 1, 'QUANTITY'), (11, 19, 'ITEM'), (31, 36, 'PRICE')]}),
    ('AC repair 8000 naira', {
     'entities': [(0, 9, 'ITEM'), (10, 14, 'PRICE')]}),
    ('Air Condition repair 8000 naira', {
     'entities': [(0, 20, 'ITEM'), (21, 25, 'PRICE')]}),
    ('Electrician fee 18000 naira', {
     'entities': [(0, 11, 'ITEM'), (16, 21, 'PRICE')]}),
    ('I sold 2 rechargeable lamps for 32000 naira', {'entities': [
     (7, 8, 'QUANTITY'), (9, 27, 'ITEM'), (32, 37, 'PRICE')]}),
    ('4 inverter batteries sold for 340000 naira', {'entities': [
     (0, 1, 'QUANTITY'), (2, 20, 'ITEM'), (30, 36, 'PRICE')]}),
    ('1 inverter sold for 30000 naira', {'entities': [
     (0, 1, 'QUANTITY'), (2, 10, 'ITEM'), (20, 25, 'PRICE')]}),
    ('i sold 4 yards of atiku material for 14500 naira', {'entities': [
     (7, 8, 'QUANTITY'), (18, 32, 'ITEM'), (37, 42, 'PRICE')]}),
    ('we bought 3 senator materials for 75400 naira', {'entities': [
     (10, 11, 'QUANTITY'), (12, 29, 'ITEM'), (34, 39, 'PRICE')]}),
    # ('i sold 7 T-shirt for 72000 naira', {'entities': [(7, 8, 'QUANTITY'), (9, 16, 'ITEM'), (21, 26, 'PRICE')]}),
    # ('i purchased 17 T shirt for 20000 naira', {'entities': [(7, 8, 'QUANTITY'), (9, 16, 'ITEM'), (21, 26, 'PRICE')]}),
    ('i purchased 1 Tee shirt for 2000 naira', {'entities': [
     (12, 13, 'QUANTITY'), (14, 23, 'ITEM'), (28, 32, 'PRICE')]}),
    ('I bought 4 jeans for 35000 naira', {'entities': [
     (9, 10, 'QUANTITY'), (11, 16, 'ITEM'), (21, 26, 'PRICE')]}),
    ('I bought 3 G string pants for 5000 naira', {'entities': [
     (9, 10, 'QUANTITY'), (11, 25, 'ITEM'), (30, 34, 'PRICE')]}),
    ('we sold 13 bras for 15000 naira', {'entities': [
     (8, 10, 'QUANTITY'), (11, 15, 'ITEM'), (20, 25, 'PRICE')]}),
    ('12 singlets for 3000 naira', {'entities': [
     (0, 2, 'QUANTITY'), (3, 11, 'ITEM'), (16, 20, 'PRICE')]}),
    ('2 boxers short 7000 naira', {'entities': [
     (0, 1, 'QUANTITY'), (2, 14, 'ITEM'), (15, 19, 'PRICE')]}),
    ('2 pair of leather shoes 70000 naira', {'entities': [
     (0, 1, 'QUANTITY'), (10, 23, 'ITEM'), (24, 29, 'PRICE')]}),
    ('Esther sold 2 pair of sanders for 170000 naira', {'entities': [
     (12, 13, 'QUANTITY'), (22, 29, 'ITEM'), (34, 40, 'PRICE')]}),
    ('I sold 2 Nike boxers short for 9800 naira', {'entities': [
     (7, 8, 'QUANTITY'), (9, 26, 'ITEM'), (31, 35, 'PRICE')]}),
    ('Agribot sold 2 Adidas cap for 7000 naira', {'entities': [
     (13, 14, 'QUANTITY'), (15, 25, 'ITEM'), (30, 34, 'PRICE')]}),
    # ('I sold 2 Air Jordan for 45000 naira', {'entities': [(7, 8, 'QUANTITY'), (9, 19, 'ITEM'), (24, 29, 'PRICE')]}),
    # ('I purchased 12 sneakers for 40000 naira', {'entities': [(7, 8, 'QUANTITY'), (9, 19, 'ITEM'), (24, 29, 'PRICE')]}),
    ('Amaka sold jeans for 12000 naira', {
     'entities': [(11, 16, 'ITEM'), (21, 26, 'PRICE')]}),
    ('I sold 2 PUMA rigalia for 12000 naira', {'entities': [
     (7, 8, 'QUANTITY'), (9, 21, 'ITEM'), (26, 31, 'PRICE')]}),
    ('Delivery man 1500 naira', {
     'entities': [(0, 12, 'ITEM'), (13, 17, 'PRICE')]}),
    ('Phone delivery 2000 naira', {
     'entities': [(0, 14, 'ITEM'), (15, 19, 'PRICE')]}),
    ('Material delivery 5000 naira', {
     'entities': [(0, 17, 'ITEM'), (18, 22, 'PRICE')]}),
    ('logistics 5200 naira', {
     'entities': [(0, 9, 'ITEM'), (10, 14, 'PRICE')]}),
    ('miscellaneous 12000 naira', {
     'entities': [(0, 13, 'ITEM'), (14, 19, 'PRICE')]}),
    ('phone repair 7300 naira', {
     'entities': [(0, 12, 'ITEM'), (13, 17, 'PRICE')]}),
    ('office chair repairs 12400 naira', {
     'entities': [(0, 20, 'ITEM'), (21, 26, 'PRICE')]}),
    ('2 GOTV Antenna sold 32790 naira', {'entities': [
     (0, 1, 'QUANTITY'), (2, 14, 'ITEM'), (20, 25, 'PRICE')]}),
    ('4 DSTV dish sold for 56400 naira', {'entities': [
     (0, 1, 'QUANTITY'), (2, 11, 'ITEM'), (21, 26, 'PRICE')]}),
    ('12 DVD remote bought for 13000 naira', {'entities': [
     (0, 2, 'QUANTITY'), (3, 13, 'ITEM'), (25, 30, 'PRICE')]}),
    ('3 GOTV remote 19000 naira', {'entities': [
     (0, 1, 'QUANTITY'), (2, 13, 'ITEM'), (14, 19, 'PRICE')]}),
    ('Sharp B29 DVD sold for 32000 naira', {
     'entities': [(0, 13, 'ITEM'), (23, 28, 'PRICE')]}),
    # ('we bought 7 Sony TVs for 1200000 naira', {'entities': [(10, 11, 'QUANTITY'), (12, 20, 'ITEM'), (25, 31, 'PRICE')]}),
    ('i bought 5 Panasonic Standing Fan for 134000 naira', {'entities': [
     (9, 10, 'QUANTITY'), (11, 33, 'ITEM'), (38, 44, 'PRICE')]}),
    ('i bought fan blades for 15000 naira', {
     'entities': [(9, 19, 'ITEM'), (24, 29, 'PRICE')]}),
    ('I paid the distributor 5000000 naira for accessories delivery', {
     'entities': [(41, 61, 'ITEM'), (23, 30, 'PRICE')]}),
    ('The fabrics distributor received 120000 naira', {
     'entities': [(4, 23, 'ITEM'), (33, 39, 'PRICE')]}),
    ('I sold CAT 6 cables for 750000 naira', {
     'entities': [(7, 19, 'ITEM'), (24, 30, 'PRICE')]}),
    ('I sold 30 yards of cable wire for 1200 naira', {'entities': [
     (7, 9, 'QUANTITY'), (19, 29, 'ITEM'), (34, 38, 'PRICE')]}),
    ('Emeka borrowed 10000 naira', {
     'entities': [(0, 14, 'ITEM'), (15, 20, 'PRICE')]}),
    ('100000 naira for children school fees', {
     'entities': [(17, 37, 'ITEM'), (0, 6, 'PRICE')]}),
    ('25000 naira for tithe', {
     'entities': [(16, 21, 'ITEM'), (0, 5, 'PRICE')]}),
    ('50000 naira bank savings', {
     'entities': [(12, 24, 'ITEM'), (0, 5, 'PRICE')]}),
    ('i saved 120000 naira at the bank yesterday', {
     'entities': [(28, 32, 'ITEM'), (8, 14, 'PRICE')]}),
    ('school fees 30000 naira', {
     'entities': [(0, 11, 'ITEM'), (12, 17, 'PRICE')]}),
    ('House rent 130000 naira', {
     'entities': [(0, 10, 'ITEM'), (11, 17, 'PRICE')]}),
    ('i sold LG Microwave oven for 45000 naira', {
     'entities': [(7, 24, 'ITEM'), (29, 34, 'PRICE')]}),
    ('i bought 1 Haier Thermocool Refridgerator 2 doors for 120000 naira', {'entities': [
     (9, 10, 'QUANTITY'), (11, 49, 'ITEM'), (54, 60, 'PRICE')]}),
    ('i sold NEXUS fridge 1 door for 20000 naira', {
     'entities': [(7, 26, 'ITEM'), (31, 36, 'PRICE')]}),
    ('i sold 1 scanfrost deep freezer for 130500 naira', {'entities': [
     (7, 8, 'QUANTITY'), (9, 31, 'ITEM'), (36, 42, 'PRICE')]}),
    ('I bought NEXUS gas cooker for 230000 naira', {
     'entities': [(9, 25, 'ITEM'), (30, 36, 'PRICE')]}),
    ('i sold binatone electric kettle for 12000 naira', {
     'entities': [(7, 31, 'ITEM'), (36, 41, 'PRICE')]}),
    ('i sold kenwood blender for 8300 naira', {
     'entities': [(7, 22, 'ITEM'), (27, 31, 'PRICE')]}),
    ('we bought binatone washing machine for 45000 naira', {
     'entities': [(10, 34, 'ITEM'), (39, 44, 'PRICE')]}),
    ('we bought Kenstar water dispenser for 32000 naira', {
     'entities': [(10, 33, 'ITEM'), (38, 43, 'PRICE')]}),
    ('i sold 1 unit of oraimo airpod for 12000 naira', {'entities': [
     (7, 8, 'QUANTITY'), (17, 30, 'ITEM'), (35, 40, 'PRICE')]}),
    ('i paid 30000000 naira for 10 Macbook pro 2020', {'entities': [
     (26, 28, 'QUANTITY'), (29, 45, 'ITEM'), (7, 15, 'PRICE')]}),
    ('i paid 30000000 naira for 10 Macbook air 2020', {'entities': [
     (26, 28, 'QUANTITY'), (29, 45, 'ITEM'), (7, 15, 'PRICE')]}),

    ('SRT light Bulb 15 5000 naira', {'entities': [
     (15, 17, 'QUANTITY'), (0, 14, 'ITEM'), (18, 22, 'PRICE')]}),
    ('Distributor fee 7500 naira', {
     'entities': [(0, 15, 'ITEM'), (16, 20, 'PRICE')]}),
    ('delivery fee 11000 naira', {
     'entities': [(0, 12, 'ITEM'), (13, 18, 'PRICE')]}),
    ('lace 3 yards 32000 naira', {'entities': [
     (5, 6, 'QUANTITY'), (0, 4, 'ITEM'), (13, 18, 'PRICE')]}),
    ('Toshiba Loudspeaker 3 169000 naira', {'entities': [
     (20, 21, 'QUANTITY'), (0, 19, 'ITEM'), (22, 28, 'PRICE')]}),
    ('45000 naira 2 buckets', {'entities': [
     (12, 13, 'QUANTITY'), (14, 21, 'ITEM'), (0, 5, 'PRICE')]}),
    ('medical fee 87000 naira', {
     'entities': [(0, 11, 'ITEM'), (12, 17, 'PRICE')]}),
    ('11000 naira for delivery', {
     'entities': [(16, 24, 'ITEM'), (0, 5, 'PRICE')]}),
    ('Distribution fee cost 67500 naira', {
     'entities': [(0, 16, 'ITEM'), (22, 27, 'PRICE')]}),
    ('45300 naira 3 Sharp MX-3100N printer', {'entities': [
     (12, 13, 'QUANTITY'), (14, 36, 'ITEM'), (0, 5, 'PRICE')]}),
    ('5 HP printers 13200 naira', {'entities': [
     (0, 1, 'QUANTITY'), (2, 13, 'ITEM'), (14, 19, 'PRICE')]}),
    ('1TB Samsung Harddrive SSD 99000 naira', {
     'entities': [(0, 25, 'ITEM'), (26, 31, 'PRICE')]}),
    ('34500 naira distribution fee', {
     'entities': [(0, 5, 'ITEM'), (12, 28, 'PRICE')]}),
    ('egusi 2 cups 500 naira', {'entities': [
     (6, 7, 'QUANTITY'), (0, 5, 'ITEM'), (13, 16, 'PRICE')]}),
    ('airtel 300 naira', {
     'entities': [(0, 6, 'ITEM'), (7, 10, 'PRICE')]}),
    ('i bought Glo 1000 naira', {
     'entities': [(9, 12, 'ITEM'), (13, 17, 'PRICE')]}),
    ('Key holder 2 5000 naira', {'entities': [
     (11, 12, 'QUANTITY'), (0, 10, 'ITEM'), (13, 17, 'PRICE')]}),
    ('AWS certification 155000 naira', {
     'entities': [(0, 17, 'ITEM'), (18, 24, 'PRICE')]}),
    ('Microsoft certfication 5 120000 naira', {'entities': [
     (23, 24, 'QUANTITY'), (0, 22, 'ITEM'), (25, 31, 'PRICE')]}),
    ('Microsoft office package 3 56000 naira', {'entities': [
     (25, 26, 'QUANTITY'), (0, 16, 'ITEM'), (27, 32, 'PRICE')]}),

    ('6000 naira phcn bill for july', {
     'entities': [(11, 20, 'ITEM'), (0, 4, 'PRICE')]}),
    ('security fee for march 11000 naira', {
     'entities': [(0, 22, 'ITEM'), (23, 28, 'PRICE')]}),
    ('council fee for january 4500 naira', {
     'entities': [(0, 23, 'ITEM'), (24, 28, 'PRICE')]}),
    ('ewa 10 bags 15000 naira', {'entities': [
     (4, 6, 'QUANTITY'), (0, 3, 'ITEM'), (12, 17, 'PRICE')]}),
    ('bed spread 2 packs for 14000 naira', {'entities': [
     (11, 12, 'QUANTITY'), (0, 10, 'ITEM'), (23, 28, 'PRICE')]}),
    ('february electricity bill 3000 naira', {
     'entities': [(0, 25, 'ITEM'), (26, 30, 'PRICE')]}),
    ('i sold 1 Sony PlayStation 5 for 500000 naira', {'entities': [
     (7, 8, 'QUANTITY'), (9, 27, 'ITEM'), (32, 38, 'PRICE')]}),
    ('i sold 2 nokia X 8gb ram for 45000 naira', {'entities': [
     (7, 8, 'QUANTITY'), (9, 24, 'ITEM'), (29, 34, 'PRICE')]}),
    ('i sold HP Elitebook 840 GS 32GB RAM 1TB SSD laptop for 320000 naira', {
     'entities': [(7, 50, 'ITEM'), (55, 61, 'PRICE')]}),
    ('i sold 2 casio fx-991ms calculator for 7000 naira', {'entities': [
     (7, 8, 'QUANTITY'), (9, 34, 'ITEM'), (39, 43, 'PRICE')]}),
    ('i bought 3 bottles of McDowels for 6500 naira', {'entities': [
     (9, 10, 'QUANTITY'), (11, 30, 'ITEM'), (35, 39, 'PRICE')]}),
    ('we bought 3 brand new iWatch SE 40MM for 170000 naira', {'entities': [
     (10, 11, 'QUANTITY'), (22, 36, 'ITEM'), (41, 47, 'PRICE')]}),
    ('i sold 1 hp 1040 G2 touch screen keyboard light 256gb 8gb ram for 205000', {'entities': [
     (7, 8, 'QUANTITY'), (9, 61, 'ITEM'), (66, 72, 'PRICE')]}),
    ('i sold 3 HP Elitebook 840 GS 32GB RAM 1TB SSD laptop for 320000 naira', {'entities': [
     (7, 8, 'QUANTITY'), (9, 52, 'ITEM'), (57, 63, 'PRICE')]}),
    # ('iphone 11 pro max 512gb gold 1 for 445000 naira', {'entities': [(29, 30, 'QUANTITY'), (0, 28, 'ITEM'), (35, 41, 'PRICE')]}),
    (
        'i sold 1 HP spectre X360 core i5 8th gen 8GB RAM 256 SSD hadrive 16GB optane 4k UHD display touch screen backlight keyboard fingerprint facial recognition B&O play sound windows 10 home for 420000 naira', {'entities': [
            (7, 8, 'QUANTITY'), (9, 185, 'ITEM'), (190, 196, 'PRICE')]}
    ),
    ('i bought 500 naira airtel recharge card', {
     'entities': [(19, 39, 'ITEM'), (9, 12, 'PRICE')]}),
    ('i sold 3000 naira nokia charger', {
     'entities': [(18, 31, 'ITEM'), (7, 11, 'PRICE')]}),
    ('i bought 2000 naira bags of pure water', {
     'entities': [(28, 38, 'ITEM'), (9, 13, 'PRICE')]}),
    ('we sold 100 naira mtn recharge card', {
     'entities': [(18, 35, 'ITEM'), (8, 11, 'PRICE')]}),
    ('i sold 1 Sony play station 5 for 500000 naira', {'entities': [
     (7, 8, 'QUANTITY'), (9, 28, 'ITEM'), (33, 39, 'PRICE')]}),

]

val_data = [
    ('i bought 500 naira airtel recharge card', {
     'entities': [(19, 39, 'ITEM'), (9, 12, 'PRICE')]}),
    ('i sold 3000 naira nokia charger', {
     'entities': [(18, 31, 'ITEM'), (7, 11, 'PRICE')]}),
    ('i bought 2000 naira bags of pure water', {
     'entities': [(28, 38, 'ITEM'), (9, 13, 'PRICE')]}),
    ('we sold 100 naira mtn recharge card', {
     'entities': [(18, 35, 'ITEM'), (8, 11, 'PRICE')]}),
    ('i sold 1 Sony play station 5 for 500000 naira', {'entities': [
     (7, 8, 'QUANTITY'), (9, 28, 'ITEM'), (33, 39, 'PRICE')]}),
]
# the DocBin will store the example documents
db = DocBin()
# for text, annotations in training_data:
for text, annotations in val_data:
    
    doc = nlp(text)
    ents = []
    for start, end, label in annotations['entities']:
        print(start, end, label)
        span = doc.char_span(start, end, label=label)
        ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("data/val.spacy")