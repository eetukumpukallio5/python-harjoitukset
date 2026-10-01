class Pelaaja:
    def __init__(self, nimi, inventaario, x, y):
        self.nimi = nimi
        self.inventaario = inventaario
        self.x = x
        self.y = y
        self.sijainti = "huone" + str(x) + str(y)
        self.raha = 0
        #pelajaan tiedot. missä pelaaja on, tavaraluettelo, raha ja nimi

    def liiku(self, suunta):
        pass

    def poimi(self):
        pass