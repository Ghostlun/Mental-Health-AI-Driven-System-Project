import requests

WIT_API_TOKEN = "Bearer SNCPHOJLZKI2CNIKQUJVBJCBDJGC6RSQ"
HEADERS = {"Authorization": WIT_API_TOKEN, 
           "Content-Type": "application/json"}

def upload_training_data(utterances, intent):
    payload = []
    for text in utterances:
        payload.append({
            "text": text,
            "intent": intent,
            "entities": [],
            "traits": []
        })

    response = requests.post(
        "https://api.wit.ai/utterances?v=20200513",
        headers=HEADERS,
        json=payload
    )

    print(f"{intent} upload status:", response.status_code, response.text)

# Feel happy examples
happy_utterances = [
    "Today was amazing!",
    "I'm feeling great today.",
    "I had a really good day.",
    "Everything went smoothly today.",
    "I’m feeling super happy!",
    "Had a wonderful lunch with my friend.",
]

# Feel sad examples
sad_utterances = [
    "I'm not feeling great today.",
    "Today was really tough.",
    "I feel kind of down.",
    "Nothing seems to be going right.",
    "I had an argument with someone.",
    "I’m emotionally exhausted.",
]

# Upload
upload_training_data(happy_utterances, "feel_happy")
upload_training_data(sad_utterances, "feel_sad")

