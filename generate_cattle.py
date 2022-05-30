from random import randint, choice

from process import Process
from utils.enums import Region

class GenerateCattle(Process):
    def __init__(self, year=2009):
        super().__init__()
        self.year = year
        self.datas = []
        self.type = 'Cabeça de Gado'
        self.cattle_value_in_years = {
            "2009": 78.87,
            "2010": 88.51,
            "2011": 101.74,
            "2012": 94.80,
            "2013": 102.64,
            "2014": 126.29,
            "2015": 145.42,
            "2016": 152.90,
            "2017": 138.81,
            "2018": 144.91,
            "2019": 162.68,
            "2020": 226.18
        }

    def generate(self) -> None:
        quantity = randint(205307954, 218190768)
        for region in list(Region):
            percentile = self.__get_percentile(region)
            quantity_percentil = round(quantity * (percentile / 100), 0)
            total_value = self.__get_value(quantity_percentil)
            self.datas.append((
                self.year,
                self.type,
                region.value,
                quantity_percentil,
                total_value
            ))

    def __get_percentile(self, region: Region) -> float:
        if region == Region.SUL:
            return 17.6
        elif region == Region.NORTE:
            return 14.5
        elif region == Region.SUDESTE:
            return 11
        elif region == Region.NORDESTE:
            return 21.4
        else:
            return 35.5

    def __get_value(self, quantity):
        unit_value = self.cattle_value_in_years[self.year]
        ox_to_arroba = 18
        return round(unit_value * quantity * ox_to_arroba, 2)

    def save(self):
        for data in self.datas:
            print(data)
            self.database.insert("insert into valores(ano, tipo,regiao, quantidade, valor)\
                                values(%s,%s,%s,%s,%s)", data)
        print("Salvou no banco")
