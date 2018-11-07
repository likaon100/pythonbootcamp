lista = [1, 2, 3, 4, 5, 6]

# warunek jest taki, że większe niż 3

out = [False, False, False, True, True, True]

def bigger_than_3(liczba):
    if liczba > 3:
        return True
    return False


def smaller_than_3(liczba):
    if liczba < 3:
        return True
    return False


def sprawdzam_czy_większe_niz_3(lista):
    out = []
    for element in lista:
        if element >3:
            out.append(True)
        else:
            out.append(False)


def sprawdzam_czy(lista, warunek):




assert sprawdzam_czy_wieksze_niz_3 == out
assert sprawdzam_czy_wieksze_niz_3 == out
