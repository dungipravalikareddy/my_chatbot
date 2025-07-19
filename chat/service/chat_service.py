from chat.client.openai_client import OpenAIClientSingleton
from chat.history.history_manager import HistoryManager
from config import cfg

class ChatService:
    """Handles sending prompts to OpenAI and managing history."""

    def __init__(self, system_prompt=None):
        # Uses provided system prompt or defaults to PROMPT_NORMAL from config
        if system_prompt is None:
            system_prompt = cfg['PROMPT_NORMAL']
        # Initialize HistoryManager with system prompt
        self.history = HistoryManager(system_prompt)
        # Create singleton OpenAI client instance
        self.client = OpenAIClientSingleton()
        # Model to use from config
        self.model = cfg['MODEL_NAME']

    def send_prompt(self, prompt: str) -> str:
        # Add user's input to history
        self.history.add_user_message(prompt)

        try:

            # Call OpenAI ChatCompletion API with entire conversation history
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.history.get_history()
            )

            # Extract assistant's response text from API output
            answer = response.choices[0].message.content

        except Exception as e:
            # Week 2 Addition: Handles API call errors gracefully
            answer = f"An error occurred: {str(e)}"


        # Add assistant's reply to history
        self.history.add_assistant_message(answer)

        # Week 2 Addition: Logs each conversation turn to log.txt file
        with open('log.txt', 'a') as f:
            f.write(f"User: {prompt}\\nBot: {answer}\\n---\\n")

        return answer  # Return the assistant's reply to caller
