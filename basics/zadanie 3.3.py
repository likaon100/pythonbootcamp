# pierwsza_cyfra= (input("podaj pierwszą cyfre"))
# druga_cyfra = int(input("podaj drugą cyfre"))
# podaj_rodzaj_opercaji = input{"+","-", "*" ,"/"}
# if pierwsza_cyfra * druga_cyfra
#     print (wyn)
# to co na górze jest źle

# przyjęcie argumentów
pierwsza_cyfra= (input("podaj pierwszą cyfre"))
druga_cyfra = (input("podaj drugą cyfre"))


# if na operacje

if pierwsza_cyfra.isnumeric() and druga_cyfra.isnumeric():
    pierwsza_cyfra = int(pierwsza_cyfra)
    druga_cyfra = int(druga_cyfra)

    operacja = input("Jaka operacja?[+-*/]")

    if operacja == "-":
        wynik = pierwsza_cyfra - druga_cyfra
    elif operacja == "+":
        wynik = pierwsza_cyfra + druga_cyfra
    elif operacja == "*":
        wynik = pierwsza_cyfra * druga_cyfra
    elif operacja == "/":
            if druga_cyfra == 0:
                wynik = "nie dziel przez O"
            else:
                wynik = pierwsza_cyfra /druga_cyfra
    else:
        print("niezrozumiała operacja")

    print( f" wynik {operacja} na argumentach {pierwsza_cyfra}, {druga_cyfra} to: {wynik}")
else:
    print("Argumenty powinny byc liczbami")