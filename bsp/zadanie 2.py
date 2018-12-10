import json
import sys

try:
    with open ("pracownicy.json", "r") as plik:
        pracownicy = json.load(plik)
except FileNotFoundError:
    pracownicy = []

op = input("Co chcesz zrobić? [d - dodaj], [w-wypisz]:")

if op == 'd':
    imie = input("imie: ")
    nazwisko = input("nazwisko: ")
    rok_ur = int(input("rok_urodzenia: "))
    pensja = float(input("pensja: "))
    pracownicy.append({"imie": imie, "nazwisko": nazwisko,
                        "rok_urodzenia": rok_ur, "pensja": pensja})
    with open("pracownicy.json", 'w') as plik:
        json.dump(pracownicy, plik)

elif op == "w":
    for nr, p in enumerate(pracownicy, 1):
        print(f" - [{nr}] {p['imie']} {p['nazwisko']} {p['rok_urodzenia']} {p['pensja']} PLN")


