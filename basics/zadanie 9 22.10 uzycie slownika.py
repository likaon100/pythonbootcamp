#1. Robimy zakupy w pętli. Po wpisaniu zakończ program powinien się zakończyć
#2. "Sorry nie ma tego produktu"
#2a. Dodajemy produkty do koszyka i po zakończeniu zakupów drugujemy parago
#3. Wprowadzimy magazyn przechowyjący ilosc produktu. "Sorry nioe ma tego produktu"
#4. Dodanie produktu do sklepu

produkty = {
    "ziemniaki": 3,
    "cebula": 2,
    "woda": 1.5,
    "piwo": 2.5
}

magazyn = {"ziemniaki": 10,
    "cebula": 10,
    "woda": 10,
    "piwo": 10}
koszyk = {}

while True:
    komenda = input("""Wybierz opcje:"
                [d] - dodaj do magazynu"
                [k] - kup
                [z] - zakończ""")
    if komenda == 'k':
    elif komenda == 'd':
    elif komenta == 'z':
        co = input("Jaki produkt chcesz kupic")
        ile = int(input(f" Ile {co} chcesz kupic?"))
        magazyn[co] = magazyn.get(co,0) + ile
        if co not in produkty:
            cena = float(input(f'Jaka cena'))
            produkty[co]


    print("W naszym sklepie oferujemy: ")
    for produkt in produkty:
        print(f" - {produkt} - w cenie: {produkty[produkt]} PLN")

    print()
    wybor_produktu = input("Który produkt chcesz kupić?  (wpisz koniec żeby zakończyc zapupy)")
    if wybor_produktu == "koniec":
        break
    if wybor_produktu in produkty:
        ile = int(input(f"Ile chcesz kupić [{wybor_produktu}]"))
        if ile <= magazyn[wybor_produktu]:
            koszyk[wybor_produktu] = ile

        else:
            print(f"Przykro mi. Nie mam tyle tego produktu. Mam {magazyn[wybor_produktu]}")
        #cena = int(ile) * produkty[wybor_produktu]
        koszyk[wybor_produktu] = int(ile)
    else:
        print("Sorry nie ma tego produktu")


print("Twój rachunek:")
sumarycznie = 0
for produkt in koszyk:
    cena = koszyk[produkt] * produkty[produkt]
    print(f" - {produkt} [{koszyk[produkt]}] : {cena} PLN")
    sumarycznie+= cena

print("="*30)
print(f"Suma: {sumarycznie} PLN")




