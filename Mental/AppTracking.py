import requests
from datetime import datetime
import json

# ▶️ Step 1: 인증 키 세팅
API_KEY = ""

# ▶️ Step 2: 인증 및 설정
category_id = "100029"  # Health and Fitness
country = "US"
device = "iphone"
feeds = "free"
date = datetime.today().strftime('%Y-%m-%d')  # 또는 datetime.today().strftime('%Y-%m-%d')
ranks = 100

# ▶️ Step 2: API 호출 설정

url = "https://api.data.ai/v1.3/apps/ios/app/1403455040/ranks?start_date=2018-07-22&end_date=2018-08-01&interval=daily&countries=US&category=Overall&feed=free"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}

params = {
    "countries": country,
    "categories": category_id,
    "feeds": feeds,
    "date": date,
    "device": device,
    "ranks": ranks
}

# ▶️ Step 3: 요청 실행
response = requests.get(url, headers=headers, params=params)

# ▶️ 전체 응답을 그대로 저장
if response.status_code == 200:
    data = response.json()
    file_name = "ranking_full_2024_12_31.json"
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ 전체 데이터가 '{file_name}'에 저장되었습니다.")
else:
    print("❌ 오류 발생:", response.status_code)
    print(response.text)



# {'category_path': 'Overall > Health and Fitness', 'category_id': 100029, 'category_name': 'Health and Fitness
# # ▶️ Step 2: API Endpoint & 파라미터 세팅
# url = "https://api.data.ai/v1.3/apps/ios/ranking"

# market = "ios"  # 또는 "google-play"
# url = f"https://api.data.ai/v1.3/meta/apps/{market}/categories"



