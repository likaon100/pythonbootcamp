class Osoba:

   def __init__ (self, imie, nazwisko):
        print("No siema")
        self.imie = imie
        self.nazwisko = nazwisko


   def przedstaw_sie(self):
       print(f"Nazwyam się (self.imie) (self.nazwisko)")

   @staticmethod
   def metoda_statystyczna():
        print("Metoda Statystyczna")

obiekt = Osoba("Adam", "Małysz")
obiekt2 = Osoba("Adam", "Mickiewicz")

obiekt2.imie = "Karol"



print(obiekt.imie)
print(obiekt2.imie)

obiekt.przedstaw_sie()


# niedokończone...