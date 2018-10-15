x= int(input("podaj współrzędną x"))
y= int(input("podaj współrzędną y"))

# wspolrzedne = x,y
# print(wspolrzedne)

if x >100 or x<0 or y> 100 or y<0:
    pozycja = "poza planszą"
elif x >=90 and y>=90:
    pozycja = " prawy górny róg"
# elif x =<10 and y>90:
# #     pozycja = "lewy górny róg"
# elif y <=10
#     pozycja = "lewy dolny róg"
else:
    print("nie udalo się")

print(f"twoja pozycja to {pozycja}")