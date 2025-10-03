from receptenboek import Receptenboek
from recept import Recept
from ingredient import Ingredient
from stap import Stap

def seed_data(boek: Receptenboek) -> None:
    # Recept 1 — Pasta Pesto (kcal zijn schattingen per 1 pers)
    r1 = Recept("Pasta Pesto", "Snelle pasta met basilicumpesto en cherrytomaat.")
    # alternatieven
    pesto_alt = Ingredient("vegan pesto", 30, "g", 130)
    r1.voeg_ingredient_toe(Ingredient("pasta", 100, "g", 360))  # 100g pasta ~360 kcal
    r1.voeg_ingredient_toe(Ingredient("pesto", 30, "g", 130, plantaardig_alternatief=pesto_alt))
    r1.voeg_ingredient_toe(Ingredient("cherrytomaten", 100, "g", 18))
    r1.voeg_stap_toe(Stap("Kook de pasta beetgaar volgens de verpakking.", tip="Bewaar wat kookvocht voor de saus."))
    r1.voeg_stap_toe(Stap("Halveer de tomaten en meng met de pesto door de pasta."))
    boek.toevoegen(r1)

    # Recept 2 — Kip Kerrie
    r2 = Recept("Kip Kerrie", "Klassieke kip kerrie met rijst, mild van smaak.")
    tofu_alt = Ingredient("tofu", 200, "g", 160)
    r2.voeg_ingredient_toe(Ingredient("kipfilet", 200, "g", 220, plantaardig_alternatief=tofu_alt))
    r2.voeg_ingredient_toe(Ingredient("rijst (ongekookt)", 75, "g", 260))
    r2.voeg_ingredient_toe(Ingredient("kerriepoeder", 8, "g", 24))
    r2.voeg_ingredient_toe(Ingredient("ui", 0.5, "stuk", 20))
    r2.voeg_stap_toe(Stap("Kook de rijst."))
    r2.voeg_stap_toe(Stap("Fruit de ui, bak de kip en voeg kerriepoeder toe.", tip="Blus met een scheutje water of kokosmelk."))
    r2.voeg_stap_toe(Stap("Serveer de kip kerrie met de rijst."))
    boek.toevoegen(r2)

    # Recept 3 — Quiche Spinazie
    r3 = Recept("Quiche met Spinazie", "Vegetarische quiche met spinazie en kaas.")
    blader_alt = Ingredient("vegan bladerdeeg", 2, "plakjes", 220)
    kaas_alt = Ingredient("plantaardige rasp", 50, "g", 180)
    r3.voeg_ingredient_toe(Ingredient("bladerdeeg", 2, "plakjes", 220, plantaardig_alternatief=blader_alt))
    r3.voeg_ingredient_toe(Ingredient("spinazie", 200, "g", 40))
    r3.voeg_ingredient_toe(Ingredient("geraspte kaas", 50, "g", 200, plantaardig_alternatief=kaas_alt))
    r3.voeg_stap_toe(Stap("Bekleed een kleine vorm met bladerdeeg."))
    r3.voeg_stap_toe(Stap("Vul met spinazie en kaas; bak 30 min op 180°C.", tip="Prik in het midden om te checken of hij gaar is."))
    boek.toevoegen(r3)

def toon_overzicht(boek: Receptenboek) -> None:
    print("Recepten:\n")
    for i, r in enumerate(boek.lijst(), start=1):
        print(f"{i}. {r.get_naam()}")

def vraag_int(vraag: str, min_value: int = 1) -> int:
    while True:
        val = input(vraag).strip()
        if val.isdigit() and int(val) >= min_value:
            return int(val)
        print("Ongeldige invoer. Probeer opnieuw.")

def vraag_ja_nee(vraag: str) -> bool:
    while True:
        antw = input(vraag + " (j/n): ").strip().lower()
        if antw in ("j", "ja"): return True
        if antw in ("n", "nee"): return False
        print("Antwoord met j of n.")

def keuze_vragen(aantal: int) -> int:
    while True:
        invoer = input("\nKies een receptnummer (of 'q' om te stoppen): ").strip().lower()
        if invoer in ("q", "quit", "exit"):
            return -1
        if invoer.isdigit():
            idx = int(invoer) - 1
            if 0 <= idx < aantal:
                return idx
        print("Ongeldige invoer. Probeer opnieuw.")

def main() -> None:
    boek = Receptenboek()
    seed_data(boek)

    print("Welkom bij het Receptenboek (console)!\n")
    toon_overzicht(boek)

    idx = keuze_vragen(len(boek.lijst()))
    if idx == -1:
        print("Afgesloten.")
        return

    # Week 2: aantal personen + plantaardig
    personen = vraag_int("\nVoor hoeveel personen wil je dit recept? ")
    plantaardig = vraag_ja_nee("Wil je een plantaardige variant gebruiken waar mogelijk?")

    recept = boek.get_by_index(idx)
    if not recept:
        print("Recept niet gevonden.")
        return

    recept.set_aantal_personen(personen)
    print("\n" + recept.as_text(plantaardig))

if __name__ == "__main__":
    main()
