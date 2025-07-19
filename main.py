from chat.service.chat_service import ChatService
from config import cfg

def main():
    print("=== Welcome to Mystic Bot 🤖✨ ===")
    print("Choose your bot style:")
    print("1. Normal Assistant")
    print("2. Sarcastic Assistant")
    print("3. Pirate Mode")

    # Week 2 Addition: Ask user for desired bot style and choose system prompt accordingly
    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "2":
        system_prompt = cfg['PROMPT_SARCASTIC']
    elif choice == "3":
        system_prompt = cfg['PROMPT_PIRATE']
    else:
        system_prompt = cfg['PROMPT_NORMAL']

    # Fun initial greeting
    print(f"Bot: {system_prompt} Hey there, curious mind! 🌟 What would you like to explore today?")

    # Pass chosen system prompt to ChatService for dynamic behaviour
    bot = ChatService(system_prompt)

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
