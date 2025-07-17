from typing import List, Dict

class HistoryManager:
    """Manages conversation history including the system prompt."""

    def __init__(self, system_prompt: str):
        # Initialize history with system prompt as first message
        self._history: List[Dict[str, str]] = [
            {'role': 'system', 'content': system_prompt}
        ]

    def add_user_message(self, content: str):
        # Adds a user's message to history
        self._history.append({'role': 'user', 'content': content})

    def add_assistant_message(self, content: str):
        # Adds the assistant's response to history
        self._history.append({'role': 'assistant', 'content': content})

    def get_history(self) -> List[Dict[str, str]]:
        # Returns entire conversation history as list of dicts
        return list(self._history)

    def clear(self):
        # Clears conversation history
        self._history.clear()
