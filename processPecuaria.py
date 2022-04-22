from random import randrange
from process import Process
from utils.process_utils import randomValor

peso_co = 0.375
peso_sul = 0.214
peso_norte = 0.176
peso_ne = 0.135
peso_sudeste = 0.10

class ProcessPecuaria(Process):

    def __init__(self, ano: int, mes: int):
        super().__init__()
        self.__ano = ano
        self.__periodo = ano + '-' + mes + '-01'
        self.__valores = {}

    def process(self):

        variacao = 0

        while variacao == 0:
            # Variação deve usar como range a taxa de variação da média para os valores min e max 
            variacao = randrange(-5, 3)/100

        valores = {
            'sul': {
                'quantidade': randomValor(peso_sul, variacao),
                'valor': 1
            },
            'norte': {
                'quantidade': randomValor(peso_norte, variacao),
                'valor': 1
            },
            'centro-oeste': {
                'quantidade': randomValor(peso_co, variacao),
                'valor': 1
            },
            'nordeste': {
                'quantidade': randomValor(peso_ne, variacao),
                'valor': 1
            },
            'sudeste': {
                'quantidade': randomValor(peso_sudeste, variacao),
                'valor': 1
            },
        }
        
        self._set_valores(valores)
    
    def _set_valores(self, valores):
        self.__valores = valores
    
    def _save(self):
        for v in self.__valores.keys():
            qtd = self.__valores[v]['quantidade']
            valor = self.__valores[v]['valor']
            data = (v, valor, qtd, self.__ano, self.__periodo)
            self.database.insert('INSERT INTO valores (regiao, valor, quantidade, \
                ano, mes) VALUES (%s,  %s, %s, %s, monthname(%s))',data)
        print(f"Dados gerados e enviados para o banco!")