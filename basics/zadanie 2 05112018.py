napis = "Ten $produkt kosztuje $cena"
napis2 = "Zajęcia z $przedmiot zostały odwołane"


def formatuj(*napisy,**co_na_co ):
    wynik = []
    for napis in napisy:
        napis = napis.replace("$"+ klucz, co_na_co[klucz])
    wynik.append(napis)
if len(wynik) == 1:

    return wynik[0]







assert formatuj(napis, produkt="Samochod", cena="200000") == "Ten Samochod kosztuje 200000"

# assert formatuj(napis, przedmiot="Fizyki") == "Zajecia z Fizyki zostały odwołane"