from chat.client.openai_client import OpenAIClientSingleton
from chat.history.history_manager import HistoryManager
from config import cfg

class ChatService:
    """Handles sending prompts to OpenAI and updating history."""
    def __init__(self):
        self.history = HistoryManager(cfg['SYSTEM_PROMPT'])
        self.client = OpenAIClientSingleton()
        self.model = cfg['MODEL_NAME']

    def send_prompt(self, prompt: str) -> str:
        self.history.add_user_message(prompt)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.history.get_history()
        )
        answer = response.choices[0].message.content
        self.history.add_assistant_message(answer)
        return answer
