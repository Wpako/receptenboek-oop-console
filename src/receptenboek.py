from typing import List, Optional
from recept import Recept

class Receptenboek:
    def __init__(self):
        self._recepten: List[Recept] = []

    def toevoegen(self, recept: Recept) -> None:
        self._recepten.append(recept)

    def lijst(self) -> List[Recept]:
        return list(self._recepten)

    def get_by_index(self, index: int) -> Optional[Recept]:
        if 0 <= index < len(self._recepten):
            return self._recepten[index]
        return None

    def verwijder_index(self, index: int) -> bool:
        if 0 <= index < len(self._recepten):
            del self._recepten[index]
            return True
        return False

    def aantal(self) -> int:
        return len(self._recepten)
