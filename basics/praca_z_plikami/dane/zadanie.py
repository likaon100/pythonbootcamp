import sys
import os

def tree(katalog, ile_wciec=0):
    for elem in os.scandir(katalog):
      #  print(ile_wciec * '|  ', elem.name, sep = "")
      if elem == zawartosc[-1]:
          print(ile_wciec * " ___")
        if elem.is_dir():
            tree(elem, ile_wciec + 1)


directory = sys.argv[1]
tree(directory)
