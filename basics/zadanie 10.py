napis = input("Podaj napis: ")
ile_wystąpień_litery = {}

# zliczyć
for litera in napis:
    if litera != " ":
    ile_wystąpień_litery[litera] = ile_wystąpień_litery.get(litera, 0) + 1

# wyświetlić
for litera in ile_wystąpień_litery:
    print(f"litera: {litera} wystąpiła {ile_wystąpień_litery[litera]} razy")
