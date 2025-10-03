from typing import List
from ingredient import Ingredient
from stap import Stap

class Recept:
    def __init__(self, naam: str, omschrijving: str, aantal_personen: int = 1):
        self._naam = naam
        self._omschrijving = omschrijving
        self._aantal_personen = int(aantal_personen)
        self._ingredient_list: List[Ingredient] = []
        self._stappen_list: List[Stap] = []

    # ---- mutators ----
    def voeg_ingredient_toe(self, ingredient: Ingredient) -> None:
        self._ingredient_list.append(ingredient)

    def voeg_stap_toe(self, stap: Stap) -> None:
        self._stappen_list.append(stap)

    # ---- Week 2 logica ----
    def set_aantal_personen(self, n: int) -> None:
        """Schaal alle ingredienten van basis (1 persoon) naar n."""
        factor = n / self._aantal_personen
        for ing in self._ingredient_list:
            ing.set_hoeveelheid(factor)
        self._aantal_personen = n

    def totale_kcal(self, plantaardig: bool) -> int:
        totaal = 0.0
        for ing in self._ingredient_list:
            totaal += ing.get_ingredient(plantaardig).get_kcal()
        return int(round(totaal))

    # ---- presentatielaag (console) ----
    def as_text(self, plantaardig: bool) -> str:
        lines = [
            f"{self._naam}",
            f"{self._omschrijving}",
            f"(voor {self._aantal_personen} persoon/personen, {'plantaardig' if plantaardig else 'normaal'})",
            "",
            "Ingrediënten:"
        ]
        for ing in self._ingredient_list:
            lines.append(f"• {ing.get_ingredient(plantaardig)}")
        lines.append("")
        lines.append("Stappen:")
        for i, s in enumerate(self._stappen_list, start=1):
            lines.append(f"{i}. {s}")
        lines.append("")
        lines.append(f"Totaal: {self.totale_kcal(plantaardig)} kcal")
        return "\n".join(lines)

    def get_naam(self) -> str:
        return self._naam
