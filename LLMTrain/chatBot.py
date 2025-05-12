def chatbot():
    print("🙋‍♀️ Hello there!")
    print("😊 How are you feeling today?")
    print("1. I'm feeling happy")
    print("2. I'm not feeling great")

    choice = input("👉 Please select an option (1 or 2): ")

    if choice == "1":
        print("✨ That's wonderful! What made you feel happy today?")
        good_thing = input("✏️ Your answer: ")
        print(f"😊 That sounds lovely! '{good_thing}' must have been a really nice experience.")
        print("Would you like to share what kind of conversation you had during that moment?")
        convo = input("✏️ Your answer: ")
        print(f"💬 Conversations like '{convo}' are really meaningful. Wishing you more joyful moments ahead! 🙌")

    elif choice == "2":
        print("😟 I'm sorry to hear that. Would you like to share what happened?")
        problem = input("✏️ Your answer: ")
        print("🤖 Sending your concern to GPT for thoughtful support...")
        gpt_response = call_gpt(problem)
        print(f"🧠 GPT: {gpt_response}")

    else:
        print("⚠️ Invalid input. Please choose either 1 or 2.")


def call_gpt(user_input):
    # Placeholder for GPT response — replace this with actual OpenAI API call
    # API Call
    return f"It’s completely understandable to feel overwhelmed when '{user_input}'. You might find it helpful to establish a small routine or take short breaks. You’ve got this!"

if __name__ == "__main__":
    chatbot()
