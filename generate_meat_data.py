from random import randint, randrange
from utils.meat_values import MeatValues


class GenerateMeat():
    def __init__(self):
        self.paises = ['Argentina', 'Brazil', 'China', 'Germany']
        self.media_gado = {}
        self.media_frango = {}
        self.media_porco = {}
        self.meat_values = MeatValues()
        self.retorno = {}
        self.definir_medias()

    def definir_medias(self):
        medias = self.meat_values
        for p in self.paises:
            self.media_gado[p] = medias.mean_gado[p]
            self.media_frango[p] = medias.mean_frango[p]
            self.media_porco[p] = medias.mean_porco[p]

    def generate(self):
        for p in self.paises:
            variacao_gado = randrange(-10, 10)/100 * self.media_gado[p]
            variacao_frango = randrange(-10, 10)/100 * self.media_frango[p]
            variacao_porco = randrange(-10, 10)/100 * self.media_porco[p]
            self.retorno[p] = {
                'gado': self.media_gado[p] - variacao_gado,
                'frango': self.media_frango[p] - variacao_frango,
                'porco': self.media_porco[p] - variacao_porco
            }

        return self.retorno
