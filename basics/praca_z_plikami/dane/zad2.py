import sys

try:
    print(sys.argv)
except IndexError:
    print("zapomniales podac nazwy pliku")



print("ścieżka do plitu to:", sys.argv[1])

user_zalogowany_login = {}
user_wylogowany_logout = {}
user_total_time = {}

with open(sys.argv[1]) as f:
   # i = 0
    for line in f:
        line = line.split (";")
        user = line[0]
        action = line[1]
        time = line[2]
        time = int(time)

        print(line, time)


        user, action, time = line.split(";")
        if action == "LOGIN":
            user_zalogowany_login =

        if action == "LOGOUT":




