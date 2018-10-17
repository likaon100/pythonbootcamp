lista = (-2,4,-1,33,-4,5,-3,6,-7,1,2)

dodatnich = 0
ujemnych = 0

for x in lista:
        if x > 0:
            dodatnich += 1

        elif x <0:
            ujemnych -=1

print(f"ilość ujemnych {ujemnych}, ilość dodatnich {dodatnich}")


