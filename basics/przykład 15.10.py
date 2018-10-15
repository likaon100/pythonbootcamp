from random import randint

graczX = randint(0,10)
graczY = randint(0,10)

while True:
    ruch = input("podaj jaki chcesz wykonać ruch: g, d, p, l:")

    if ruch == "g":
        graczY = graczY + 1
    elif ruch == "d":
        graczY = graczY - 1
    elif ruch == "p":
        graczX = graczX + 1
    elif ruch == "l":
        graczX = graczX - 1

    if (ruch == "koniec"):
        break

print(f"pozycja gracza to: {graczX, graczY}")




