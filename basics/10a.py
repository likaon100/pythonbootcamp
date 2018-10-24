napis = input("Podaj napis: ")

liczniki = {}

print(liczniki)
liczniki[litera] = 1

for litera in napis:

    if litera in liczniki:
        liczniki[litera] = liczniki.get[litera,0] + 1
    else:
        liczniki[litera] = 1


for litera in liczniki:
    print(f"litera: {litera} wystąpiła {liczniki[litera]} razy")
# liczniki['a'] = liczniki.get('a') + 1

print(liczniki)