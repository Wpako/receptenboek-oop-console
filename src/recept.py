from typing import List
from ingredient import Ingredient
from stap import Stap

class Recept:
    def __init__(self, naam: str, omschrijving: str):
        self._naam = naam
        self._omschrijving = omschrijving
        self._ingredient_list: List[Ingredient] = []
        self._stappen_list: List[Stap] = []

    # ---- mutators ----
    def voeg_ingredient_toe(self, ingredient: Ingredient) -> None:
        self._ingredient_list.append(ingredient)

    def voeg_stap_toe(self, stap: Stap) -> None:
        self._stappen_list.append(stap)

    # ---- accessors ----
    def get_naam(self) -> str:
        return self._naam

    # ---- presentatielaag (console) ----
    def __str__(self) -> str:
        lines = [
            f"{self._naam}",
            f"{self._omschrijving}",
            "",
            "Ingrediënten (voor 1 persoon):"
        ]
        for ing in self._ingredient_list:
            lines.append(f"• {ing}")
        lines.append("")
        lines.append("Stappen:")
        for i, s in enumerate(self._stappen_list, start=1):
            lines.append(f"{i}. {s}")
        return "\n".join(lines)
