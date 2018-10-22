# napis = "Ala ma kota D".lower()
# print(napis[0])
# print("d" in napis)
# print("D" in napis)
#
# for litera in napis:
#     print(litera)

napis = input("podaj napis:")
licznik = 0
SAMOGLOSKI = 'aeiou'

for litera in napis.lower():
    if litera in SAMOGLOSKI:
        licznik += 1

print(f" W napisie jest {licznik} samogłosek")


# for litera in napis:    coś tu  źle
#     if litera == "a" or litera == "A":
#         i += 1
#     if litera == "e" or litera =="E":
#         i += 1
#     if litera == "i" or litera == "I":
#         i += 1
#     if litera == "O" or litera == "O":
#         i += 1
#     if litera == "u" or litera == "U":
#         i += 1
#
# print(f"{i}")