class Huone:
    def __init__(self, koordinaatit, intro, esineet=[]): #normi huoneeseen kolme tarvittua infoa. jos ei esineitä, ottaa tyhjän listan. tällöin tarvitsee huoneesta antaa vain koordinatit ja intro alustaessa
        self.koordinaatit = koordinaatit
        self.intro = intro
        self.esineet = esineet