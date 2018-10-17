lista = []
i = 0

while len(lista) <10:
   x = input("Podaj liczbe:")
   if x == "k":
       break
   liczba  = int(x)
   lista.append(liczba)
if len(lista) == 0:
    print("nie podano danych")
else:
    sredna = sum(lista)/len(lista)
    print(f"Średnia to {lista}")