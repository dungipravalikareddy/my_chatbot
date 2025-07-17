from chat.client.openai_client import OpenAIClientSingleton
from chat.history.history_manager import HistoryManager
from config import cfg

class ChatService:
    """Handles sending prompts to OpenAI and managing history."""

    def __init__(self):
        # Initialize HistoryManager with system prompt
        self.history = HistoryManager(cfg['SYSTEM_PROMPT'])
        # Create singleton OpenAI client instance
        self.client = OpenAIClientSingleton()
        # Model to use from config
        self.model = cfg['MODEL_NAME']

    def send_prompt(self, prompt: str) -> str:
        # Add user's input to history
        self.history.add_user_message(prompt)

        # Call OpenAI ChatCompletion API with entire conversation history
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.history.get_history()
        )

        # Extract assistant's response text from API output
        answer = response.choices[0].message.content

        # Add assistant's reply to history
        self.history.add_assistant_message(answer)

        return answer  # Return the assistant's reply to caller
