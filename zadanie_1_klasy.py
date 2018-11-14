class Product():
    def __init__ (self,ID, nazwa, cena):
        self.ID = ID
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"Produkt {self.ID}, {self.nazwa}, {self.cena}")

produkt = Product(1, "Masło", 4.99)
produkt2 = Product(2, "Bułka", 0.20)

produkt.print_info()
produkt2.print_info()