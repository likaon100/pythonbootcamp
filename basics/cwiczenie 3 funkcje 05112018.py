def policz_znaki(napis, start="<", stop=">"):
    poziom_zaglebienia = 0
    wynik = 0
    for znak in napis:
        if znak == start:
            poziom_zaglebienia += 1
        elif znak == stop:
            poziom_zaglebienia -= 1
        else:
            wynik += poziom_zaglebienia
    return wynik
def test_policz_znaki_bez_znacznikow():
    assert policz_znaki('ala ma kota a kot ma ale') == 0

def test_policz_znaki_jeden_poziom_zaglebienie_stanadrowe_znaczniki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4

def test_policz_znaki_wiele_poziomow_zaglebienia_niestandardowe_znaczniki():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18
    assert policz_znaki('ala [kota [a kot]] ma [ale]', start='[', end=']') == 18

print(policz_znaki("Ala <ma> kota"))
print(policz_znaki('ala ma <kota> a kot ma ale'))
print(policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']'))
