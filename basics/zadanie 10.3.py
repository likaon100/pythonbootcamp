suma_t = 0
i = 0

while True:
    dane = input(" temperatura lub wpisz k by zakończych")

    if dane == "k":
        break

    suma_t += float(dane)
    i += 1
print("srednia temp. to: ", (suma_t/i))

