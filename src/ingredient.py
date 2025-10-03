from __future__ import annotations
from typing import Optional

class Ingredient:
    """
    kcal hoort bij de opgegeven hoeveelheid/eenheid (voor 1 pers).
    Bij schalen vermenigvuldigen we hoeveelheid én kcal evenredig.
    """
    def __init__(
        self,
        naam: str,
        hoeveelheid: float,
        eenheid: str,
        kcal: float,
        plantaardig_alternatief: Optional["Ingredient"] = None,
    ):
        self._naam = naam
        self._hoeveelheid = float(hoeveelheid)
        self._eenheid = eenheid
        self._kcal = float(kcal)
        self._plantaardig_alternatief = plantaardig_alternatief

    def set_hoeveelheid(self, factor: float) -> None:
        self._hoeveelheid *= factor
        self._kcal *= factor
        if self._plantaardig_alternatief:
            self._plantaardig_alternatief.set_hoeveelheid(factor)

    def get_ingredient(self, plantaardig: bool) -> "Ingredient":
        return self._plantaardig_alternatief if (plantaardig and self._plantaardig_alternatief) else self

    def get_kcal(self) -> float:
        return self._kcal

    def __str__(self) -> str:
        qty = int(self._hoeveelheid) if self._hoeveelheid.is_integer() else self._hoeveelheid
        spc = "" if self._eenheid in ("stuk", "stuks", "snuf") else " "
        return f"{qty}{spc}{self._eenheid} {self._naam} ({int(self._kcal)} kcal)"
