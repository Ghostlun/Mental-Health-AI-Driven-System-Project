import requests

WIT_API_TOKEN = "Bearer SNCPHOJLZKI2CNIKQUJVBJCBDJGC6RSQ"
HEADERS = {
    "Authorization": WIT_API_TOKEN
}

def get_prediction(user_input):
    url = f"https://api.wit.ai/message?v=20200513&q={user_input}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        print("Raw Response:", data)

        intent = data.get('intents', [{}])[0].get('name', 'No intent found')
        confidence = data.get('intents', [{}])[0].get('confidence', 0.0)

        print(intent)
        print(f"Predicted Intent: {intent} (confidence: {confidence})")
    else:
        print("Failed to get prediction:", response.status_code, response.text)

# 예시 호출
get_prediction("I am fine thank you")
get_prediction("Today was too tired.")
