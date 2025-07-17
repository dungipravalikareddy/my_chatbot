import os
from dotenv import load_dotenv

# Load environment variables from .env file
def load_config():
    load_dotenv()  # loads .env into os.environ

    # Return config as a dictionary
    return {
        'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
        'MODEL_NAME': os.getenv('MODEL_NAME', 'gpt-3.5-turbo'),
        'SYSTEM_PROMPT': os.getenv('SYSTEM_PROMPT', 'You are a helpful assistant.')
    }

# Load and expose configuration globally
cfg = load_config()
