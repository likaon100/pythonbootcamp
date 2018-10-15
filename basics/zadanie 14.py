znalezione_max = None
znalezione_min = None

while True:
    wejscie = input("podaj liczbę:")

    if wejscie == "koniec":
        break

    x = int(wejscie)

    if znalezione_max is None or x > znalezione_max:
        znalezione_max = x
    if znalezione_min is None or x < znalezione_min:
        znalezione_min = x

if znalezione_max is None:
    print("brak maksium - nie wprowadzono danych")
else:
    print(f"Znalezione maksimum: {znalezione_max}; znalezione minimum: {znalezione_min}")