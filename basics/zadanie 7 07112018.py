data = [1, 2, 3, 4, 5, 6, 7, 8, 2, 4]
start = lambda x: x > 3
stop = lambda x: x== 6


def przycinaj(data, start, stop):
    lista = []
    for element in data:
        if start(element):
            lista.append(element)
        if stop(element):
            break
    return lista

wynik = przycinaj(data, start, stop)
print(wynik)


