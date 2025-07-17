from chat.service.chat_service import ChatService

def main():
    print("=== Welcome to Mystic Bot 🤖✨ ===")
    # Fun initial greeting
    print("Bot: Hey there, curious mind! 🌟 What would you like to explore today?")

    # Initialize chat service
    bot = ChatService()

    # Chat loop
    while True:
        user_input = input("You: ")

        # Check for exit words
        if user_input.lower() in ('exit', 'quit', 'bye'):
            print("Bot: Bye! Have a great day 😊")
            break

        # Get bot's reply using ChatService
        reply = bot.send_prompt(user_input)
        print(f"Bot: {reply}\n")

# Runs main if this script is executed directly
if __name__ == '__main__':
    main()
