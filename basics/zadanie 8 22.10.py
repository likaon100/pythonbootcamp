# 1 SPOSÓB

# napis = "Ala ma <kota>, a kot ma Ale"
#
# licznik = 0
#
# for litera in napis.lower():
#     if litera == "<":
#         x = napis.index(litera)
#     elif litera ==">":
#         y = napis.index(litera)
#
# z = y - x - 1
#
# print(f"Liczba znaków w podanych przez uzytkownika napisie w <> wynosi: {z} ")



# 2 sposób - prowadzącego

# napis = "Ala ma <kota>, a kot ma Ale"
#
# licznik = 0
#
# czy_zliczac = False
#
# for i in napis:
#     if i == "<":
#         czy_zliczac = True
#     elif i == ">":
#         break
#
# print(licznik)


# 3 jak kilka <>

napis = "Ala ma <kota>, a <kot> ma Ale"

licznik = 0

czy_zliczac = False

for i in napis:
    if i == "<":
        czy_zliczac = True
    elif i == ">":
        czy_zliczac = False
    elif czy_zliczac:
        licznik += 1

print(licznik)



#
# apis = "ssss <Ala> sdd"
#
# nawiasy = "<>"
#
# licznik = 0
# for i in nawiasy:
#     if i in nawiasy:
#         licznik += 1
# print(licznik+1)