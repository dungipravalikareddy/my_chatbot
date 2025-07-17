from chat.service.chat_service import ChatService

def main():
    print("=== Welcome to Mystic Bot 🤖✨ ===")
    # Fun initial greeting
    print("Bot: Hey there, curious mind! 🌟 What would you like to explore today?")

    bot = ChatService()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ('exit', 'quit', 'bye'):
            print("Bot: Bye! Have a great day 😊")
            break

        reply = bot.send_prompt(user_input)
        print(f"Bot: {reply}\n")

if __name__ == '__main__':
    main()
