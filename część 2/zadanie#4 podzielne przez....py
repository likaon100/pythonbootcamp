
ilosc = 0
listailosc = []
for x in range (0,101):
    if x%3 == 0 or x%5 == 0:
        ilosc +=1
        # print(x)
        listailosc.append(x)
print(f"listy podzielne przez {listailosc}")
print(f"liczb podzielnych przez 3 lub 5 jest: {ilosc}")



