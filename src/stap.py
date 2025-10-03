from typing import Optional

class Stap:
    def __init__(self, beschrijving: str, tip: Optional[str] = None):
        self._beschrijving = beschrijving
        self._tip = tip

    def __str__(self) -> str:
        return f"{self._beschrijving}  [Tip: {self._tip}]" if self._tip else self._beschrijving
