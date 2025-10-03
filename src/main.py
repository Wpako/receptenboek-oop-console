from receptenboek import Receptenboek
from recept import Recept
from ingredient import Ingredient
from stap import Stap

# ------------------- Seed-data (met kcal & alternatieven) -------------------
def seed_data(boek: Receptenboek) -> None:
    # Recept 1 — Pasta Pesto
    r1 = Recept("Pasta Pesto", "Snelle pasta met basilicumpesto en cherrytomaat.")
    pesto_alt = Ingredient("vegan pesto", 30, "g", 130)
    r1.voeg_ingredient_toe(Ingredient("pasta", 100, "g", 360))
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

# ------------------- Helpers -------------------
def vraag_int(vraag: str, min_value: int = 1) -> int:
    while True:
        val = input(vraag).strip()
        if val.isdigit() and int(val) >= min_value:
            return int(val)
        print("Ongeldige invoer. Probeer opnieuw.")

def vraag_float(vraag: str, min_value: float = 0.0) -> float:
    while True:
        val = input(vraag).replace(",", ".").strip()
        try:
            f = float(val)
            if f >= min_value:
                return f
        except ValueError:
            pass
        print("Ongeldige invoer. Probeer opnieuw.")

def vraag_ja_nee(vraag: str) -> bool:
    while True:
        antw = input(vraag + " (j/n): ").strip().lower()
        if antw in ("j", "ja"): return True
        if antw in ("n", "nee"): return False
        print("Antwoord met j of n.")

def toon_overzicht(boek: Receptenboek) -> None:
    print("\nRecepten:\n")
    for i, r in enumerate(boek.lijst(), start=1):
        print(f"{i}. {r.get_naam()}")

def kies_recept_index(boek: Receptenboek) -> int:
    if boek.aantal() == 0:
        print("Er staan (nog) geen recepten in het boek.")
        return -1
    toon_overzicht(boek)
    while True:
        invoer = input("\nKies een receptnummer (of 'b' om terug te gaan): ").strip().lower()
        if invoer in ("b", "back"):
            return -1
        if invoer.isdigit():
            idx = int(invoer) - 1
            if 0 <= idx < boek.aantal():
                return idx
        print("Ongeldige invoer. Probeer opnieuw.")

# ------------------- Acties (FR-6..8) -------------------
def actie_tonen(boek: Receptenboek) -> None:
    idx = kies_recept_index(boek)
    if idx == -1:
        return
    personen = vraag_int("\nVoor hoeveel personen wil je dit recept? ")
    plantaardig = vraag_ja_nee("Wil je een plantaardige variant gebruiken waar mogelijk?")
    recept = boek.get_by_index(idx)
    if not recept:
        print("Recept niet gevonden.")
        return
    recept.set_aantal_personen(personen)
    print("\n" + recept.as_text(plantaardig))

def actie_toevoegen(boek: Receptenboek) -> None:
    print("\n--- Nieuw recept toevoegen ---")
    naam = input("Naam van het recept: ").strip()
    if not naam:
        print("Naam mag niet leeg zijn.")
        return
    omschrijving = input("Korte omschrijving: ").strip()
    nieuw = Recept(naam, omschrijving)

    # Ingrediënten (voor 1 persoon)
    print("\nIngrediënten toevoegen (voor 1 persoon).")
    while True:
        ing_naam = input("Ingrediëntnaam (of leeg om te stoppen): ").strip()
        if ing_naam == "":
            if len(nieuw._ingredient_list) == 0:
                print("Minstens één ingrediënt is vereist.")
                continue
            break
        hoeveelheid = vraag_float("Hoeveelheid (bijv. 100): ", 0.0)
        eenheid = input("Eenheid (bijv. g, ml, stuk): ").strip() or "g"
        kcal = vraag_float("kcal bij deze hoeveelheid: ", 0.0)

        alt = None
        if vraag_ja_nee("Bestaat er een plantaardig alternatief?"):
            alt_naam = input("  Alternatief naam: ").strip()
            alt_hoeveelheid = vraag_float("  Alternatief hoeveelheid: ", 0.0)
            alt_eenheid = input("  Alternatief eenheid: ").strip() or eenheid
            alt_kcal = vraag_float("  Alternatief kcal: ", 0.0)
            alt = Ingredient(alt_naam, alt_hoeveelheid, alt_eenheid, alt_kcal)

        nieuw.voeg_ingredient_toe(Ingredient(ing_naam, hoeveelheid, eenheid, kcal, alt))

    # Stappen
    print("\nBereidingsstappen toevoegen (minimaal 1).")
    while True:
        stap_beschrijving = input("Stap (beschrijving, of leeg om te stoppen): ").strip()
        if stap_beschrijving == "":
            if len(nieuw._stappen_list) == 0:
                print("Minstens één stap is vereist.")
                continue
            break
        tip = input("  Tip (optioneel, leeg laten voor geen): ").strip() or None
        nieuw.voeg_stap_toe(Stap(stap_beschrijving, tip))

    boek.toevoegen(nieuw)
    print(f"\nRecept '{naam}' is toegevoegd.")

def actie_verwijderen(boek: Receptenboek) -> None:
    idx = kies_recept_index(boek)
    if idx == -1:
        return
    recept = boek.get_by_index(idx)
    if not recept:
        print("Recept niet gevonden.")
        return
    print(f"\nJe staat op het punt '{recept.get_naam()}' te verwijderen.")
    if vraag_ja_nee("Weet je het zeker?"):
        if boek.verwijder_index(idx):
            print("Recept verwijderd.")
        else:
            print("Verwijderen mislukt.")
    else:
        print("Verwijderen geannuleerd.")

# ------------------- Hoofdmenu -------------------
def hoofdmenu() -> str:
    print("\n=== Receptenboek ===")
    print("[1] Recept tonen")
    print("[2] Recept toevoegen")
    print("[3] Recept verwijderen")
    print("[4] Afsluiten")
    return input("Maak een keuze: ").strip()

def main() -> None:
    boek = Receptenboek()
    seed_data(boek)

    while True:
        keuze = hoofdmenu()
        if keuze == "1":
            actie_tonen(boek)
        elif keuze == "2":
            actie_toevoegen(boek)
        elif keuze == "3":
            actie_verwijderen(boek)
        elif keuze == "4":
            print("Afgesloten.")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

if __name__ == "__main__":
    main()
