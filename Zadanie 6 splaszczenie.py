
def splaszcz(lista):
    out = []
    for element in lista:
        if isinstance(element,list):
            out.extend(splaszcz(element))
        else:
            out.append(element)
        return out

lista = [1, 2, 3, [4, 5, [6]],7]


def test_splaszczenie_niezagniezdzona_lista():
    lista = [1, 2, 3, 4, 5, 6]
    assert splaszcz(lista) == [1, 2, 3, 4, 5, 6]

def test_splaszczenie_tabela_zagniezdzona():
    lista = [1, [2, 3]]
    assert splaszcz(lista)




#
#     lista = [1, [2, 3]
#     assert splaszczlista
#
#
# lista[1]
# lista[3]
#
# assert isinstance(lista[0]), int)  #1
# assert isinstance(lista[3], int) # [4, 5, [6]]
#
# assert splaszcz(lista) == [1,2,3,4,5,6,7]