from abc import ABC, abstractmethod
from utils.process_utils import get_time_response
from utils.database_manager import DatabaseManager
import os, psutil

class Process(ABC):
    def __init__(self, case_range: range, case_number: str):
        self.case_range = case_range
        self.__case_number = f'caso {case_number}'
        self.__time_process = 0
        self.__space_process = 0
        self.count_entrance = 0
        self.database = DatabaseManager("localhost","poupay",os.environ['USER_MYSQL'], os.environ['PASSWORD_MYSQL'])
        

    def run(self):
        self.process()
        self.__get_time()
        self.__get_space()
        self.__save()

    @abstractmethod
    def process(self):
        pass

    def __get_time(self):
        self.__time_process = get_time_response(self.process)

    def __get_space(self):
        self.__space_process = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2

    def __save(self):
        data = (self.__space_process, self.__case_number, self.__time_process, self.count_entrance)
        self.database.insert('INSERT INTO metricas (espaco, caso, tempo, \
                   entrance, created_at) VALUES (%s,  %s, %s, %s, now())',data)
        print(f"As informações de execução do {self.__case_number} foram armazenadas com sucesso no banco de dados.")

