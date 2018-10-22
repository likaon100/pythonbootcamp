produkty = {"pomidor": 4.5,
            "papryka": 5,
            "ziemniak": 2}

produkt = input("podaj nazwe produktu: pomidor, papryka,lub ziemiak:")
waga = float(input("podaj wage produktu:"))


koszt = produkty[produkt]  * waga

print(f'koszt {waga} kg {produkt} kosztuje {koszt}')



# inaczej.... lepiej
for produkt in produkty:
    print(f"- {produkt}" - "w cenie")