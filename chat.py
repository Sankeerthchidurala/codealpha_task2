print("🤖 ChatBot: Hi! I'm a simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if 'hello' in user_input or 'hi' in user_input:
        print("🤖 ChatBot: Hello there!")
    elif 'how are you' in user_input:
        print("🤖 ChatBot: I'm just a program, but I'm doing great! How about you?")
    elif 'your name' in user_input:
        print("🤖 ChatBot: I'm ChatBot, your friendly terminal assistant.")
    elif 'bye' in user_input:
        print("🤖 ChatBot: Goodbye! Have a great day!")
        break
    else:
        print("🤖 ChatBot: I'm not sure how to respond to that.")
