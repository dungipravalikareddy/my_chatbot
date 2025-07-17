import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    return {
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
        'MODEL_NAME': os.getenv('MODEL_NAME', 'gpt-3.5-turbo'),
        'SYSTEM_PROMPT': os.getenv('SYSTEM_PROMPT', 'You are a helpful assistant.')
    }

cfg = load_config()
