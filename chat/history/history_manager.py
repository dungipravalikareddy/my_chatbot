from typing import List, Dict

class HistoryManager:
    """Manages the conversation history including the system prompt."""
    def __init__(self, system_prompt: str):
        self._history: List[Dict[str, str]] = [
            {'role': 'system', 'content': system_prompt}
        ]

    def add_user_message(self, content: str):
        self._history.append({'role': 'user', 'content': content})

    def add_assistant_message(self, content: str):
        self._history.append({'role': 'assistant', 'content': content})

    def get_history(self) -> List[Dict[str, str]]:
        return list(self._history)

    def clear(self):
        self._history.clear()
