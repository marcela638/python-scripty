class Produkt:
    def __init__(self, nazev, cena):
        self.nazev=nazev
        self.cena=cena

    def vypis_info(self):
        print(f"Název: {self.nazev}")    
        print(f"Cena: {self.cena:.2f}Kč")   

    def vypocitej_slevu(self, procento):
        sleva=self.cena*(procento/100)      
        nova_cena =self.cena - sleva
        return nova_cena   
                
produkty = [Produkt("mléko", 25.90), Produkt("Chléb", 19.90), Produkt("Sýr", 45.90)]

for produkt in produkty:
    produkt.vypis_info()
    mova_cena = produkt.vypocitej_slevu(10)
    print(f"cena po slevě je: {mova_cena:.2f} Kč")
    print("-" * 30)
