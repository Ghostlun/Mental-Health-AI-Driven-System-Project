from datetime import datetime

LOG_FILE = "chat_log.txt"

def log_message(role, message):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {role}: {message}\n")


def get_preset_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How are you doing today?"
    elif "bad" in user_input or "not good" in user_input:
        return "I'm sorry to hear that. Want to talk about what's bothering you?"
    elif "good" in user_input:
        return "That's great to hear! What's making you feel good today?"
    elif "fight" in user_input or "argument" in user_input:
        return "Arguments can be really tough. Do you want to share what happened?"
    return None


def main():
    print("🤖 Mental Health Chatbot (testing mode)\nType 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        log_message("User", user_input)

        if user_input.lower() == "exit":
            print("Chatbot: Take care! 👋")
            log_message("Chatbot", "Take care! 👋")w
            break

        preset_response = get_preset_response(user_input)
        if preset_response:
            print(f"Chatbot (preset): {preset_response}")
            log_message("Chatbot (preset)", preset_response)
        else:
            gpt_response = "[This is where GPT would generate a response]"
            print(f"Chatbot (GPT): {gpt_response}")
            log_message("Chatbot (GPT)", gpt_response)


if __name__ == "__main__":
    main()
