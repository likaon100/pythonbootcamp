class Postac():
    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self. atak = atak
        self.zdrowie =zdrowie
        self.max_zdrowie = zdrowie

    def przedstaw_sie(self):
        # print(f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia")
        print(self)

    def __str__(self):
        return f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia"

    def otrzymaj_obrazenia(self, ile):
        print(f"{self.imie} oberwal za {ile} obrazen")
        self.zdrowie = self.zdrowie - ile
        if self.zdrowie <0:
            self.zdrowie = 0

    def czy_zyje(self):
        return self.zdrowie >0

    def wylecz(self):
        return self.zdrowie > 0

    def leczenie(self, lek):
       if self.zdrowie + lek < self.max_zdrowie:
           self.zdrowie = self.zdrowie + lek
       else:
           self.zdrowie=self.max_zdrowie





rufus = Postac("Rufus",3,100)
rufus.przedstaw_sie()
rufus.otrzymaj_obrazenia(40)
rufus.max_zdrowie = 200
print(rufus)
rufus.otrzymaj_obrazenia(5)
rufus.leczenie(201)
print(rufus)

# def test_nowa_postac():
#     postac = Postac("Albert",1,20)
#     assert postac.imie
