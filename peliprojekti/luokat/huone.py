class Huone:
    def __init__(self, koordinaatit, intro, tyhja_intro, esineet=[], kauppa=[]): #normi huoneeseen kolme tarvittua infoa. jos ei esineitä, ottaa tyhjän listan. tällöin tarvitsee huoneesta antaa vain koordinatit ja intro alustaessa. intro eri jos ei esineitä
        self.koordinaatit = koordinaatit
        self.intro = intro
        self.tyhja_intro = tyhja_intro
        self.esineet = esineet
        self.kauppa = kauppa

    def esittely(self):
        if len(self.esineet) == 0:
            print(self.tyhja_intro)
        else:
            print(self.intro)

    def poista_esine(self, esine):
        if esine != "onki" and esine != "kala" and esine != "diesel": #esineet jotka ei ole näitä poistetaan listasta
            self.esineet.remove(esine)