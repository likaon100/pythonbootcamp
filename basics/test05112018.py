# def foo(pierwszy, *reszta):
#     # print("pierwszy:", pierwszy)
#     # print("reszta:", reszta)
#     if reszta:
#         return pierwszy + reszta[-1]
#         return pierwszy
#
#
# print(foo(1))
# print(foo(1, 2))
# print(foo(1, 5, 2, 10))
#
# reszta = [1, 2, 5, "cos tam"]
# print(1, 2, 5, "cos tam")
# print(reszta)
# print(*reszta)
#
#
# def druga_funkcja(**slownik):
#     if 'd' in slownik:
#         return slownik['a'] + slownik['d']
#     if slownik:
#         return slownik['a']
#     return "Zaden warunek nie był spełniony"
#
#
# print(druga_funkcja(a=2))
# print(druga_funkcja(a=2, b=2, c=4))
# print(druga_funkcja(a=2, b=2, c=4, d=14, ))


# Zmiana Ala ma kota na kot ma Ale

def zamien(jakis_tekst, **co_na_co):
    print(type(co_na_co))
    for klucz in co_na_co:
        jakis_tekst = jakis_tekst.replace(klucz, co_na_co[klucz])
    return jakis_tekst
co_na_co = {
    "Ala": "Kot",
    "kota": "Alę"
}
print(zamien("Ala ma kota"))



print(zamien("Ala ma kota", **co_na_co))

