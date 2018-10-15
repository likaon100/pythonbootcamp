bok_a = float(input("podaj bok a opakowania w cm:"))
bok_b = float(input("podaj bok b opakowania w cm:"))
bok_c = float(input("podaj bok c opakowania w cm:"))
objetosc_opakowania = bok_a * bok_b * bok_c


#1 sposób
# print(objetosc_opakowania)
# print(f"Objętość opakowania większa od 1000 cm2: {objetosc_opakowania>1000}")
# print(f"Objętość opakowania mniejsza od 1000 cm2: {objetosc_opakowania<1000}")

#lub
# if objetosc_opakowania >1000:
#     print("Objętość większa niż 1 litr")
# else:
#     print("Objętość mniejsza lub równa 1 litr")

# lub
if objetosc_opakowania >1000:
    print("Objętość większa niż 1 litr")
elif objetosc_opakowania == 1000:
    print("Objętość oakowania wynosi 1 litr")
else:
    print("Objętość mniejsza lub równa 1 litr")