from typing import Optional

class Stap:
    def __init__(self, beschrijving: str, tip: Optional[str] = None):
        self._beschrijving = beschrijving
        self._tip = tip  # Week 2: optionele tip

    def __str__(self) -> str:
        if self._tip:
            return f"{self._beschrijving}  [Tip: {self._tip}]"
        return self._beschrijving
