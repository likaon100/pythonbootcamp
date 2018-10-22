liczby = [5,2,1,4,3]
#indexy = [0,1,2,3,4]


# min_ = None
# max_ = None

min_ = liczby[0]
max_ = liczby[0]

for liczba in liczby:
    if liczba < min_:
        min_ = liczba
    if liczba > max_:
        max_ = liczba

print("Wartości", min_, max_)
print("Indeksy, czyli Pozycje", liczby.index(min_), liczby.index(max_))


liczby[liczby.index(min_)],liczby[liczby.index(max_)] = max_, min_

print(liczby)






# for i in range(len(liczby)):
#     print(liczby[i])

# assert False
#
# #assert True
#
# assert liczby == [1,2,5,4,3]