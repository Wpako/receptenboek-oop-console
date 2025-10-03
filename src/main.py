from receptenboek import Receptenboek
from recept import Recept
from ingredient import Ingredient
from stap import Stap

def seed_data(boek: Receptenboek) -> None:
    # Recept 1 — Pasta Pesto
    r1 = Recept("Pasta Pesto", "Snelle pasta met basilicumpesto en cherrytomaat.")
    r1.voeg_ingredient_toe(Ingredient("pasta", 100, "g"))
    r1.voeg_ingredient_toe(Ingredient("pesto", 30, "g"))
    r1.voeg_ingredient_toe(Ingredient("cherrytomaten", 100, "g"))
    r1.voeg_stap_toe(Stap("Kook de pasta beetgaar volgens de verpakking."))
    r1.voeg_stap_toe(Stap("Halveer de tomaten en meng met de pesto door de pasta."))
    boek.toevoegen(r1)

    # Recept 2 — Kip Kerrie
    r2 = Recept("Kip Kerrie", "Klassieke kip kerrie met rijst, mild van smaak.")
    r2.voeg_ingredient_toe(Ingredient("kipfilet", 150, "g"))
    r2.voeg_ingredient_toe(Ingredient("rijst", 75, "g"))
    r2.voeg_ingredient_toe(Ingredient("kerriepoeder", 1, "el"))
    r2.voeg_ingredient_toe(Ingredient("ui", 0.5, "stuk"))
    r2.voeg_stap_toe(Stap("Kook de rijst."))
    r2.voeg_stap_toe(Stap("Fruit de ui, bak de kip en voeg kerriepoeder toe."))
    r2.voeg_stap_toe(Stap("Serveer de kip kerrie met de rijst."))
    boek.toevoegen(r2)

    # Recept 3 — Quiche Spinazie
    r3 = Recept("Quiche met Spinazie", "Vegetarische quiche met spinazie en kaas.")
    r3.voeg_ingredient_toe(Ingredient("bladerdeeg", 2, "plakjes"))
    r3.voeg_ingredient_toe(Ingredient("spinazie", 200, "g"))
    r3.voeg_ingredient_toe(Ingredient("geraspte kaas", 50, "g"))
    r3.voeg_stap_toe(Stap("Bekleed een kleine vorm met bladerdeeg."))
    r3.voeg_stap_toe(Stap("Vul met spinazie en kaas; bak 30 min op 180°C."))
    boek.toevoegen(r3)

def toon_overzicht(boek: Receptenboek) -> None:
    print("Recepten:\n")
    for i, r in enumerate(boek.lijst(), start=1):
        print(f"{i}. {r.get_naam()}")

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

    recept = boek.get_by_index(idx)
    print("\n" + str(recept) if recept else "Recept niet gevonden.")

if __name__ == "__main__":
    main()
