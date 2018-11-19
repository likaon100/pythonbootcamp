from random import randint
from przedmiot import Przedmiot

#randint liczba calkowita z przediazłu 1-10 ?


class Postac():
    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self.atak = atak
        self.zdrowie =zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek = {}

    def przedstaw_sie(self):
        # print(f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia")
        print(self)

    def __str__(self):
        if self.czy.zyje():
            napis = "Ekwipunek:"

        return f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia"

    def otrzymaj_obrazenia(self, ile):
        print(f"{self.imie} oberwal za {ile} obrazen")
        self.zdrowie = self.zdrowie - ile
        if self.zdrowie <0:
            self.zdrowie = 0

    def czy_zyje(self):
        return self.zdrowie >0


    def moc_ataku(self):
        wynik = randint(self.atak // 2, self.atak)
        return wynik




    def wylecz(self):
        return self.zdrowie > 0

    def leczenie(self, lek):
       if self.zdrowie + lek < self.max_zdrowie:
           self.zdrowie = self.zdrowie + lek
       else:
           self.zdrowie=self.max_zdrowie

    @staticmethod
    def walka(atakujacy, broniacy):
        print(f"Walka: {atakujacy.imie} vs {broniacy.imie}")
        print(atakujacy)
        print(broniacy)
        atak_atakujacego = atakujacy.moc_ataku()
        atak_broniacego = broniacy.moc_ataku()
        broniacy.otrzymaj_obrazenia(atakujacy.atak)
        print(f"{atakujacy.imie} udzerza {broniacy.imie} za {atakujacy.atak} obrazen")
        broniacy.otrzymaj_obrazenia(atakujacy.atak)
        print(f"{broniacy.imie} uderza {atakujacy.imie} za {broniacy.atak} obrazen")
        atakujacy.otrzymaj_obrazenia(broniacy.atak)
        print("Koniec walki")

    def daj_przedmiot(self)




rufus = Postac("Rufus",3,100)
janina = Postac("Janina",4,80)
Postac.walka(rufus,janina)
tulipan = Przedmiot("Zielony tulipan zniszczenia",5)

rufus.przedstaw_sie()
rufus.otrzymaj_obrazenia(40)
rufus.max_zdrowie = 200
print(rufus)
rufus.otrzymaj_obrazenia(5)
rufus.leczenie(5)
print(rufus)
print(janina)


# def test_nowa_postac():
#     postac = Postac("Albert",1,20)
#     assert postac.imie
