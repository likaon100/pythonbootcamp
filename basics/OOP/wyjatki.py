lista = [1, 2, 3, 4]

try:
    print(lista[4])
    list.add(5)

except IndexError as e:
    raise IndexError("Próbujesz pobrac jakis element spoza listy")
except AttributeError as e:
    print("Prawdopodobnie wywołujesz metodę, której tej obiekt nie ma")

print("Ala ma tooo")