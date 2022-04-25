from random import randint, choice

from process import Process
from utils.enums import Region

class GenerateSoy(Process):
    def __init__(self, year=2009, month=1):
        super().__init__()
        self.year = year
        self.month = month
        self.datas = []
        self.type = 'Saco de soja'
        self.cattle_value_in_years = {
            "2018": 84.43,
            "2019": 82.17,
            "2020": 121.23
        }

    def generate(self) -> None:
        quantity = randint(205_307_954, 218_190_768)
        for region in list(Region):
            percentile = self.__get_percentile(region)
            quantity = round(quantity * (percentile / 100), 0)
            total_value = self.__get_value(quantity)
            self.datas.append((
                self.year,
                self.month,
                self.type,
                region.value,
                quantity,
                total_value
            ))

    def __get_percentile(self, region: Region) -> float:
        if region == Region.SUL:
            return 25
        elif region == Region.NORTE:
            return 12.5
        elif region == Region.SUDESTE:
            return 9.2
        elif region == Region.NORDESTE:
            return 18.8
        else:
            return 45.8

    def __get_value(self, quantity):
        unit_value = self.cattle_value_in_years[self.year]
        return round(unit_value * quantity, 2)

    def save(self):
        for data in self.datas:
            print(data)
            self.database.insert("insert into valores(ano, mes, tipo,regiao, quantidade, valor)\
                                values(%s,%s,%s,%s,%s,%s)", data)
        print("Salvou no banco")
