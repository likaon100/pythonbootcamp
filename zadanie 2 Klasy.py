class Employee():
    def __init__ (self,imie, nazwisko, stawka_za_godzine):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka_za_godzine
        self.time = 0.0

    def register_time(self, time):
        self.time += time
        if time > 8:
            self.time += time - 8
                  



    def pay_salary(self):
        wyplata = self.time * self.stawka
        self.time = 0.0
        return wyplata



employee = Employee("Jan", "Nowak", 100)
print(employee.pay_salary()) #0
employee.register_time(5)
employee.register_time(10) #8h +2 h
print(employee.pay_salary()) #1700/1500 nie lisząc nadgodzin
print(employee.pay_salary())



