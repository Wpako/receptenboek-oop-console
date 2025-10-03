class Stap:
    def __init__(self, beschrijving: str):
        self._beschrijving = beschrijving

    def __str__(self) -> str:
        return self._beschrijving
