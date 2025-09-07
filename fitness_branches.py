# jett_branches.py

# List of all Jett Fitness branches
branch_names = [
    "เกตเวย์ บางซื่อ",
    "เกษร (ชิดลม)",
    "แคนวาส (เพลินจิต)",
    "ดองกี้ มอลล์ (เอกมัย)",
    "เดอะ ยูนิคอร์น (บีทีเอส พญาไท)",
    "เดอะซีน (ทาวน์อินทาวน์)",
    "เดอะพาร์ค (MRT QSNCC)",
    "เดอะฟิล (อ่อนนุช)",
    "เดอะสตรีท (รัชดา)",
    "นวมินทร์ ซิตี้ อเวนิว (เกษตร-นวมินทร์)",
    "บางจาก (ฺBTS บางจาก)",
    "พาร์ค สีลม (BTS ศาลาแดง)",
    "ฟิวเจอร์ซิตี้ รังสิต (รังสิต)",
    "มาร์เก็ต เพลส (ดุสิต)",
    "ยูนิลีเวอร์ (พระรามเก้า)",
    "โรบินสัน (ลาดกระบัง)",
    "วัน แบงค็อก (MRT ลุมพินี)",
    "วิคตอรี่ ฮับ (BTS อนุสาวรีย์ชัยฯ)",
    "สเตเดียมวัน (จุฬา)",
    "สยามสแควร์วัน (BTS สยาม)",
    "สวนเพลิน มาร์เก็ต (พระราม 4)",
    "สายไหม อเวนิว (สายไหม)",
    "สีลม คอนเนค (BTS ช่องนนทรี)",
    "เสนา เฟสท์ (เจริญนคร)",
    "อมอรินี่ (รามอินทรา)",
    "อโศก (BTS อโศก)",
    "อาคาร เอส พี (อารีย์)",
    "อินเด็กซ์ ลิฟวิ่ง มอลล์ (พระราม 2)",
    "เอ็มเอส สยาม (พระราม 3)",
    "เอสเจ อินฟินิท วัน (จตุจักร)",
    "แอมไชน่าทาวน์ (MRT วัดมังกร)",
    "เดอะกลาส บางนา Samut Prakan",
    "เซ็นทรัลสุราษฎร์ธานี Surat Thani",
    "คอสโม บาร์ซาร์ (เมืองทองธานี) Nonthaburi",
    "เซ็นทรัล เวสต์วิลล์ (ราชพฤกษ์) Nonthaburi",
    "โรบินสัน ไลฟ์สไตล์ (ราชพฤกษ์) Nonthaburi",
    "ลิตเติ้ล วอร์ค รัตนาธิเบศร์ (MRT แยกนนทบุรี 1) Nonthaburi",
    "อินเด็กซ์ ลิฟวิ่ง มอลล์ บางใหญ่ (MRT ตลาดบางใหญ่) Nonthaburi",
    "โฮมโปร (ราชพฤกษ์) Nonthaburi",
    "เซ็นทรัล นครปฐม Nakhon Pathom",
    "เดอะ โฟร์ท (พุทธมณฑล สาย4) Nakhon Pathom",
    "เซ็นทรัล นครสวรรค์ Nakhon Sawan",
    "เซฟวัน (โคราช) Nakhon Ratchasima",
    "เทอร์มินอล 21 (โคราช) Nakhon Ratchasima",
    "เซ็นทรัลอยุธยา Phra Nakhon Si Ayutthaya",
    "เซ็นทรัลภูเก็ต เฟสติวัล Phuket",
    "โรบินสัน ถลาง Phuket",
    "วันนิมมาน Chiang Mai",
    "อินเด็กซ์ ลิฟวิ่ง มอลล์ Chiang Mai",
    "เซ็นทรัลศรีราชา Chonburi",
    "ลิตเติ้ล วอร์ค (พัทยากลาง) Chonburi",
    "โรบินสัน ไลฟ์สไตล์ เพชรบุรี Phetchaburi",
    "มาร์เก็ตวิลเลจ หัวหิน Prachuap Khiri Khan",
    "เซ็นทรัลจันทบุรี Chanthaburi"
]

# Generate full search queries with prefix
jett_queries = [f"Jetts 24 Hour Fitness {branch}" for branch in branch_names]

we_branch_names = [
    "สาขาเมเจอร์รัชโยธิน",
    "สาขาเมเจอร์ปิ่นเกล้า",
    "สาขาเมเจอร์สุขุมวิท(เอกมัย)",
    "สาขาเอสพลานาดรัชดา",
    "สาขาเอสพลานาดแคราย",
    "เจ อเวนิว ทองหล่อ",
    "โรงแรม วี ราชเทวี"
]

# Prefix "WE Fitness"
we_queries = [f"WE Fitness {branch}" for branch in we_branch_names]

fitness_first_branches = [
        "Club ICON",
        "Club 39"
        "ZONE CentralWorld"
        "Platinum AIA Capital Center",
        "Platinum Landmark Plaza",
        "Platinum Q-House Lumpini",
        "Platinum Sathorn Square",
        "Platinum Siam Paragon",
        "Platinum Pearl Bangkok",
        "Platinum T-One Building"
        "CentralPlaza Khonkaen",
        "CentralPlaza Grand Rama 9",
        "CentralPlaza Udonthani",
        "CentralPlaza Bangna",
        "CentralPlaza Chonburi",
        "CentralPlaza Rama 2",
        "CentralPlaza Rama 3",
        "CentralPlaza Rattanathibet",
        "CentralPlaza Pinklao",
        "CentralPlaza Chaengwattana",
        "CentralFestival Hatyai",
        "The Mall Bangkhae",
        "The Mall Korat",
        "The Mall Thapra",
        "The Mall Bangkapi",
        "The Mall Ngamwongwan",
        "Home Pro Petchkasem",
        "Terminal 21",
        "Seacon Square",
        "Mega Bangna",
        "The Crystal SB Ratchapruek",
        "The Crystal Ramindra",
        "Future Park Rangsit",
        "The Promenade"
    ]

fitness_first_queries = [f"Fitness First {branch}" for branch in fitness_first_branches]

virgin_branch_names = [
    "Empire Tower",
    "Siam Discovery",
    "Wireless Road",
    "EmQuartier",
    "EastVille",
    "Westgate",
    "True Digital Park"
]

virgin_queries = [f"Virgin Active {branch}" for branch in virgin_branch_names]

Fitness24Seven_branch_names = [
    "นานา",
    "พระราม 9",
    "สะพานใหม่",
    "สาธรธานี",
    "อ่อนนุช",
    "แฮปปี้แลนด์ บางกะปิ",
    "พหลโยธิน",
    "เดอะ เมโทรโพลิส สำโรง"
]
Fitness24Seven_queries = [f"Fitness24Seven {branch}" for branch in Fitness24Seven_branch_names]

Fitness7_branch_names = [
    "Kubon",
    "Town In Town",
    "Srinakarin",
    "Bang Bua Thong",
    "รัชดา",
]
Fitness7_queries = [f"Fitness7 {branch}" for branch in Fitness7_branch_names]

Anytime_branch_names = [
  "Lotus Saraburi",
  "Portobello Mall Chaengwattana (Coming Soon)",
  "The Walk Ratchapruek",
  "Lotus Bangyai",
  "JLK Nana",
  "Exchange Tower",
  "Chamchuri Square",
  "Century Onnut",
  "Oasis Ratchapruek",
  "Nanglinchee Market Place Mall"
]
Anytime_queries = [f"Anytime Fitness {branch}" for branch in Anytime_branch_names]

# Combine both into one list
all_fitness_queries = jett_queries + we_queries + fitness_first_queries + virgin_queries + Fitness24Seven_queries + Fitness7_queries + Anytime_queries