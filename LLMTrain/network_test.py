import requests
import uuid

# 서버 주소 (로컬 또는 배포된 URL로 바꿔주세요)
BASE_URL = "http://localhost:8000"

# 테스트용 사용자 이메일과 메시지
email = "test@gmail.com"
message = "I'm feeling really anxious today."

# Style User T/F

# ✅ POST 요청: 메시지 저장 전용 API
post_url = f"{BASE_URL}/api/chat/session_messages/"
post_payload = {
    "email": email,
    "message": message,
    "role": "user"  # 선택적으로 "assistant"로도 가능
}

post_response = requests.post(post_url, json=post_payload)

print("🔹 POST 응답 상태코드:", post_response.status_code)
try:
    print("🔹 POST 응답 내용:", post_response.json())
except Exception as e:
    print("❌ JSON 디코딩 실패:", post_response.text)

# ✅ 2. GET 요청: 세션 메시지 조회
# get_url = f"{BASE_URL}/chat/session_messages/?session_id={session_id}"

# get_response = requests.get(get_url)
# print("\n🔹 GET 응답 상태코드:", get_response.status_code)
# print("🔹 GET 응답 내용:", get_response.json())
