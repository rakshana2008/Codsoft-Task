print("=== Smart Chat Assistant ===")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif "name" in user:
        print("Bot: I am RuleBot 1.0.")

    elif "college" in user:
        print("Bot: Which department are you studying in?")

    elif "python" in user:
        print("Bot: Python is a beginner-friendly programming language.")

    elif "bye" in user:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
