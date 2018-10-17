from random import randint

graczX = randint(1,10)
graczY = randint(1,10)

skarbX = randint(1,10)
skarbY = randint(1,10)



while True:
    ruch = input("podaj jaki chcesz wykonać ruch: g, d, p, l:")

    print(f"pozycja gracza to: {graczX, graczY}")

    minKrokowPrzed =abs(skarbX-graczX) + abs(skarbY - graczY)

    if ruch == "g":
        graczY = graczY + 1
    elif ruch == "d":
        graczY = graczY - 1
    elif ruch == "p":
        graczX = graczX + 1
    elif ruch == "l":
        graczX = graczX - 1

    minKrokowPo = abs(skarbX - graczX) + abs(skarbY - graczY)

    if (ruch == "koniec"):
        break

    if minKrokowPrzed < minKrokowPo:
        print("oddalasz się")
    else:
        print("Zbliżasz się")

    if graczX == skarbX and graczY == skarbY:
        print("Znalazłeś skarb")
        break

    if graczX >10 or graczX <1 or graczY >10 or graczY <1:
        print("Spadłes z planszy!")
        break




