import sys

try:
    print(sys.argv)
except IndexError:
    print("zapomniales podac nazwy pliku")



print("ścieżka do plitu to:", sys.argv[1])

with open(sys.argv[1]) as f:
    i = 0
    for line in f:
        print(i, line, end="")
        i+=1