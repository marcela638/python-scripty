import json

class Produkt:
    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena
        self.ve_sleve = False

    def aplikuj_slevu(self, procento):
        if procento > 0 and not self.ve_sleve:
            sleva = self.cena * (procento / 100)
            self.cena -= sleva
            self.ve_sleve = True

    def vypis_info(self):
        print(f"Název: {self.nazev}")
        print(f"Cena: {self.cena:.2f} Kč")
        print("Ve slevě: Ano" if self.ve_sleve else "Ve slevě: Ne")

    def to_dict(self):
        return {
            "nazev": self.nazev,
            "cena": round(self.cena, 2),
            "ve_sleve": self.ve_sleve
        }

# Načtení produktů ze souboru
with open("produkty.json", "r", encoding="utf-8") as soubor:
    data = json.load(soubor)

produkty = []

# Vytvoření objektů a aplikace slevy
for polozka in data:
    p = Produkt(polozka["nazev"], polozka["cena"])
    p.aplikuj_slevu(polozka["sleva"])
    produkty.append(p)

# Výpis pouze produktů ve slevě
print("Produkty ve slevě:")
for p in produkty:
    if p.ve_sleve:
        p.vypis_info()
        print("-" * 30)


vystup_data = [p.to_dict() for p in produkty]

with open("produkty_vystup.json", "w", encoding="utf-8") as vystup:
    json.dump(vystup_data, vystup, ensure_ascii=False, indent=4)

print("Produkty byly uloženy do 'produkty_vystup.json'")        
