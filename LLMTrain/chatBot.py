import random
import requests

# 설정
WIT_API_TOKEN = "Bearer SNCPHOJLZKI2CNIKQUJVBJCBDJGC6RSQ"
HEADERS = {
    "Authorization": WIT_API_TOKEN
}

def call_wit(text):
    url = f"https://api.wit.ai/message?v=20200513&q={text}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        top_intent = data.get("intents", [{}])[0]
        return top_intent.get("name", ""), top_intent.get("confidence", 0.0)
    else:
        print("Wit.ai API error:", response.status_code)
        return "", 0.0

def call_gpt(user_input):

    
    return f"It’s completely understandable to feel overwhelmed when '{user_input}'. You might find it helpful to take a break or talk to someone. You’re not alone!"

def chatbot():
    greetings = [
        "🙋‍♀️ Hello there!",
        "👋 Hi! Nice to see you.",
        "🌞 Hey! How’s your day so far?",
        "💬 Welcome! I'm here to check in with you.",
        "😊 Hello! Let’s talk about how you're feeling."
    ]

    print(random.choice(greetings))
    print("😊 How are you feeling today? Just describe it in your own words.")
    user_feeling = input("✏️ Your answer: ")

    intent, confidence = call_wit(user_feeling)

    print(f"🔍 Detected intent: {intent} (confidence: {confidence:.2f})")

    if intent == "feel_happy":
        print("✨ That's wonderful to hear! What made you feel happy today?")
        good_thing = input("✏️ Your answer: ")
        print(f"😊 That sounds lovely — '{good_thing}' must have been a really special moment for you.")
        
        print("Would you like to share what kind of conversation you had during that time?")
        convo = input("✏️ Your answer: ")
        print(f"💬 Conversations like '{convo}' are truly meaningful. I'm so glad you experienced that. 🙌")
        
        print("🧠 I’ll remember this happy moment for you — so whenever you need a little sunshine, we can look back on it together.")


    elif intent == "feel_sad":
        print("😟 I'm sorry to hear that. Would you like to share what happened?")
        problem = input("✏️ Your answer: ")
        print("🤖 Sending your concern to GPT for thoughtful support...")
        gpt_response = call_gpt(problem)
        print(f"🧠 GPT: {gpt_response}")

    else:
        print("⚠️ Sorry, I couldn't understand your mood clearly. Could you try describing it again in a different way?")

if __name__ == "__main__":
    chatbot()
