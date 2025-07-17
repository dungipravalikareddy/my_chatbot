from openai import OpenAI
from config import cfg

class OpenAIClientSingleton:
    _instance = None  # class-level attribute to store single instance

    def __new__(cls):
        if cls._instance is None:
            # First time initialization with API key from config
            cls._instance = OpenAI(api_key=cfg['OPENAI_API_KEY'])
        return cls._instance  # returns existing instance on subsequent calls
