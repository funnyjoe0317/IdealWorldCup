from pymongo import MongoClient

client = MongoClient('mongodb://bum:bum@52.79.133.185', 27017)
db = client.dbjungle_week00


info = {
    'info' : True,
    'title' : '우리 동네 맛집 월드컵',
    'desc' : '전민동의 맛집을 찾아서!',
    'worldcup_id' : 'food'
}

doc = [
    {
        'id_number' : 0,
        'name' : '국영수떡볶이',
        'url' : 'static/images/food/01_국영수떡볶이.jfif',
        'worldcup_id' : 'food'
    },

    {
        'id_number' : 1,
        'name' : '화목한우리집',
        'url' : 'static/images/food/02_화목한우리집.jfif',
        'worldcup_id' : 'food'
    },

    {
        'id_number' : 2,
        'name' : '곱이곱다',
        'url' : 'static/images/food/03_곱이곱다.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 3,
        'name' : '고고짬뽕',
        'url' : 'static/images/food/04_고고짬뽕.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 4,
        'name' : '플레이버거',
        'url' : 'static/images/food/05_플레이버거.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 5,
        'name' : '한우곰탕',
        'url' : 'static/images/food/06_한우곰탕.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 6,
        'name' : '어니언키친',
        'url' : 'static/images/food/07_어니언키친.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 7,
        'name' : '광세족발',
        'url' : 'static/images/food/08_광세족발.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 8,
        'name' : '한방삼계탕',
        'url' : 'static/images/food/09_한방삼계탕.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 9,
        'name' : '심스스모크하우스',
        'url' : 'static/images/food/10_심스스모크하우스.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 10,
        'name' : '스시안',
        'url' : 'static/images/food/11_스시안.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 11,
        'name' : '라멘히로시',
        'url' : 'static/images/food/12_라멘히로시.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 12,
        'name' : '제주진고기국수',
        'url' : 'static/images/food/13_제주진고기국수.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 13,
        'name' : '우촌면옥',
        'url' : 'static/images/food/14_우촌면옥.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 14,
        'name' : '서민대패',
        'url' : 'static/images/food/15_서민대패.jfif',
        'worldcup_id' : 'food'
    },
    {
        'id_number' : 15,
        'name' : '전민한우',
        'url' : 'static/images/food/16_전민한우.jfif',
        'worldcup_id' : 'food'
    }
]

db.worldcup1.insert_one(info)

for i in range(len(doc)):
    db.worldcup1.insert_one(doc[i])

info = {
    'info' : True,
    'title' : '가고싶은 회사 월드컵',
    'desc' : '최고의 회사를 찾아서!',
    'worldcup_id' : 'company'
}

doc = [
    {
        'id_number' : 0,
        'name' : '네이버',
        'url' : 'static/images/company/01_네이버.jpg',
        'worldcup_id' : 'company'
    },

    {
        'id_number' : 1,
        'name' : '라인',
        'url' : 'static/images/company/02_라인.jpg',
        'worldcup_id' : 'company'
    },

    {
        'id_number' : 2,
        'name' : '펍지',
        'url' : 'static/images/company/03_펍지.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 3,
        'name' : '배민',
        'url' : 'static/images/company/04_배민.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 4,
        'name' : '스파르타코딩클럽',
        'url' : 'static/images/company/05_스파르타코딩클럽.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 5,
        'name' : '당근마켓',
        'url' : 'static/images/company/06_당근마켓.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 6,
        'name' : '야놀자',
        'url' : 'static/images/company/07_야놀자.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 7,
        'name' : '업비트',
        'url' : 'static/images/company/08_업비트.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 8,
        'name' : '직방',
        'url' : 'static/images/company/09_직방.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 9,
        'name' : '채널톡',
        'url' : 'static/images/company/10_채널톡.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 10,
        'name' : '카카오',
        'url' : 'static/images/company/11_카카오.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 11,
        'name' : '코드브릭',
        'url' : 'static/images/company/12_코드브릭.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 12,
        'name' : '쿠팡',
        'url' : 'static/images/company/13_쿠팡.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 13,
        'name' : '크래프톤',
        'url' : 'static/images/company/14_크래프톤.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 14,
        'name' : '토스',
        'url' : 'static/images/company/15_토스.jpg',
        'worldcup_id' : 'company'
    },
    {
        'id_number' : 15,
        'name' : '트루밸런스',
        'url' : 'static/images/company/16_트루밸런스.jpg',
        'worldcup_id' : 'company'
    }
]

db.worldcup1.insert_one(info)

for i in range(len(doc)):
    db.worldcup1.insert_one(doc[i])

info = {
    'info' : True,
    'title' : '주류 월드컵',
    'desc' : '최고의 주류를 찾아서!',
    'worldcup_id' : 'alcohol'
}

doc = [
    {
        'id_number' : 0,
        'name' : '기린이치방',
        'url' : 'static/images/Alcohol/01_기린이치방.jpg',
        'worldcup_id' : 'alcohol'
    },

    {
        'id_number' : 1,
        'name' : '대선',
        'url' : 'static/images/Alcohol/02_대선.jfif',
        'worldcup_id' : 'alcohol'
        
    },

    {
        'id_number' : 2,
        'name' : '발렌타인',
        'url' : 'static/images/Alcohol/03_발렌타인.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 3,
        'name' : '버드와이져',
        'url' : 'static/images/Alcohol/04_버드와이져.jfif',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 4,
        'name' : '아사히',
        'url' : 'static/images/Alcohol/05_아사히.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 5,
        'name' : '연태고량주',
        'url' : 'static/images/Alcohol/06_연태고량주.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 6,
        'name' : '조니워커',
        'url' : 'static/images/Alcohol/07_조니워커.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 7,
        'name' : '좋은데이',
        'url' : 'static/images/Alcohol/08_좋은데이.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 8,
        'name' : '진로',
        'url' : 'static/images/Alcohol/09_진로.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 9,
        'name' : '참이슬',
        'url' : 'static/images/Alcohol/10_참이슬.png',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 10,
        'name' : '처음처럼',
        'url' : 'static/images/Alcohol/11_처음처럼.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 11,
        'name' : '청하',
        'url' : 'static/images/Alcohol/12_청하.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 12,
        'name' : '칭다오',
        'url' : 'static/images/Alcohol/13_칭다오.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 13,
        'name' : '카스',
        'url' : 'static/images/Alcohol/14_카스.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 14,
        'name' : '테라',
        'url' : 'static/images/Alcohol/15_테라.jpg',
        'worldcup_id' : 'alcohol'
    },
    {
        'id_number' : 15,
        'name' : '화요',
        'url' : 'static/images/Alcohol/16_화요.jpg',
        'worldcup_id' : 'alcohol'
    }
]

db.worldcup1.insert_one(info)

for i in range(len(doc)):
    db.worldcup1.insert_one(doc[i])

info = {
    'info' : True,
    'title' : '우리 동네 커피집 월드컵',
    'desc' : '최고의 커피를 찾아서!',
    'worldcup_id' : 'coffe'
}

doc = [
    {
        'id_number' : 0,
        'name' : '랩플레이스',
        'url' : 'static/images/coffecup/01_랩플레이스.jfif',
        'worldcup_id' : 'coffe'
    },

    {
        'id_number' : 1,
        'name' : '리본커피',
        'url' : 'static/images/coffecup/02_리본커피.jfif',
        'worldcup_id' : 'coffe'
    },

    {
        'id_number' : 2,
        'name' : '메가커피',
        'url' : 'static/images/coffecup/03_메가커피.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 3,
        'name' : '스타벅스',
        'url' : 'static/images/coffecup/04_스타벅스.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 4,
        'name' : '연하커피',
        'url' : 'static/images/coffecup/05_연하커피.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 5,
        'name' : '온유',
        'url' : 'static/images/coffecup/06_온유.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 6,
        'name' : '이디야',
        'url' : 'static/images/coffecup/07_이디야.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 7,
        'name' : '커피가',
        'url' : 'static/images/coffecup/08_커피가.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 8,
        'name' : '커피디자인',
        'url' : 'static/images/coffecup/09_커피디자인.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 9,
        'name' : '커피라운지',
        'url' : 'static/images/coffecup/10_커피라운지.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 10,
        'name' : '커피커피',
        'url' : 'static/images/coffecup/11_커피커피.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 11,
        'name' : '커피포터',
        'url' : 'static/images/coffecup/12_커피포터.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 12,
        'name' : '크리미스윗',
        'url' : 'static/images/coffecup/13_크리미스윗.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 13,
        'name' : '14_할리스',
        'url' : 'static/images/coffecup/14_할리스.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 14,
        'name' : '모리스커피',
        'url' : 'static/images/coffecup/15_모리스커피.jfif',
        'worldcup_id' : 'coffe'
    },
    {
        'id_number' : 15,
        'name' : '더리터',
        'url' : 'static/images/coffecup/16_더리터.jfif',
        'worldcup_id' : 'coffe'
    }
]

db.worldcup1.insert_one(info)

for i in range(len(doc)):
    db.worldcup1.insert_one(doc[i])



