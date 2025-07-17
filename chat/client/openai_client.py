from openai import OpenAI
from config import cfg

class OpenAIClientSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = OpenAI(api_key=cfg['OPENAI_API_KEY'])
        return cls._instance
