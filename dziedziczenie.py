class Zwierz():
    def przedstaw_sie(self):
        print("Nie wiem czym jestem")

class pies(Zwierz):
    def przedstaw_sie(self):
        print("Jestem psem")

z = pies
z.przedstaw_sie
