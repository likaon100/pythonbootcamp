# Zadanie 4
def formatuj(*args, **kwarqs):
    tekst = "\n".join(arqs)
    for k in kwarqs:
        tekst = tekst.replace("$"+k, str(kwarqs[k]))
    return tekst

def test_formatuj():
    assert formatuj (
        'koszt $cena PLN',
        'kwota $cena brutto',
        cena = 10
    ) == 'koszt 10 PLN"\nkwota 10 brutto'



