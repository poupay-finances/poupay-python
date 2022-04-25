from random import randint

from process import Process
from utils.enums import Region


class GenerateSoy(Process):
    def __init__(self, year=2009):
        super().__init__()
        self.year = year
        self.datas = []
        self.type = 'Tonelada de soja'
        self.cattle_value_in_years = {
            "2018": 84.43,
            "2019": 82.17,
            "2020": 121.23
        }

    def generate(self) -> None:
        quantity = randint(114_316_829, 127_797_712)
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
            return 15
        elif region == Region.NORTE:
            return 12.5
        elif region == Region.SUDESTE:
            return 8.2
        elif region == Region.NORDESTE:
            return 18.8
        else:
            return 45.5

    def __get_value(self, quantity):
        unit_value = self.cattle_value_in_years[self.year]
        package_to_ton = 16.6667
        return round((unit_value * quantity) * package_to_ton, 2)

    def save(self):
        for data in self.datas:
            print(data)
            self.database.insert("insert into valores(ano, tipo, regiao, quantidade, valor)\
                                values(%s,%s,%s,%s,%s)", data)
        print("Salvou no banco")
