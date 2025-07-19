import os
from dotenv import load_dotenv

# Load environment variables from .env file
def load_config():
    load_dotenv()  # loads .env into os.environ

    # Return config as a dictionary
    return {
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
        'MODEL_NAME': os.getenv('MODEL_NAME', 'gpt-3.5-turbo'),
        'PROMPT_NORMAL': os.getenv('PROMPT_NORMAL', 'You are a helpful assistant.'),
        'PROMPT_SARCASTIC': os.getenv('PROMPT_SARCASTIC', 'You are a sarcastic assistant.'),
        'PROMPT_PIRATE': os.getenv('PROMPT_PIRATE', 'You are a pirate.')
    }

# Load and expose configuration globally
cfg = load_config()
