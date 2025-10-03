class Ingredient:
    def __init__(self, naam: str, hoeveelheid: float, eenheid: str):
        self._naam = naam
        self._hoeveelheid = float(hoeveelheid)
        self._eenheid = eenheid

    def __str__(self) -> str:
        # bv. "100 g pasta" of "1 stuk ui"
        qty = int(self._hoeveelheid) if self._hoeveelheid.is_integer() else self._hoeveelheid
        spc = "" if self._eenheid in ("stuk", "stuks", "snuf") else " "
        return f"{qty}{spc}{self._eenheid} {self._naam}"
