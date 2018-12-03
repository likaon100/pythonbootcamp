with open("dane/input.txt") as f:
    print(f.read())


# tryb do odczytu

with open("info.txt", "w") as f:
    for linia in f:
        if len(linia) > 600:
            print(linia)



with open("info.txt", "w", encoding= 'utf8') as f:
    f.write()