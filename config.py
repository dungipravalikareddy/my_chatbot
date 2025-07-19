import os
from dotenv import load_dotenv

# Load environment variables from .env file
def load_config():
    # Load .env if exists, else fallback to .env.development
    if os.path.exists('.env'):
        load_dotenv('.env')
    else:
        load_dotenv('.env.development')

    # Return config as a dictionary
    return {
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
        'MODEL_NAME': os.getenv('MODEL_NAME', 'gpt-3.5-turbo'),
        'PROMPT_NORMAL': os.getenv('PROMPT_NORMAL', 'You are a helpful assistant.'),
        'PROMPT_SARCASTIC': os.getenv('PROMPT_SARCASTIC', 'You are a sarcastic assistant.'),
        'PROMPT_PIRATE': os.getenv('PROMPT_PIRATE', 'You are a pirate.'),
        'TEMPERATURE': float(os.getenv('TEMPERATURE', 0.8)),
        'TOP_P': float(os.getenv('TOP_P', 0.95))
    }

# Load and expose configuration globally
cfg = load_config()
