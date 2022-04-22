from process import Process
from utils.process_utils import get_time_response
import os, psutil

class ProcessLoop(Process):
    def __init__(self, case_range: range, case_number: str):
        super().__init__()
        self.case_range = case_range
        self.__case_number = f'caso {case_number}'
        self.__time_process = 0
        self.__space_process = 0

    def process(self):
        list_process = []
        for number in self.case_range:
            list_process.append(number)
            list_process.pop()
            self.count_entrance += 1
        self.__get_time()
        self.__get_space()
    
    def __get_time(self):
        self.__time_process = get_time_response(self.process)

    def __get_space(self):
        self.__space_process = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
    
    def _save(self):
        data = (self.__space_process, self.__case_number, self.__time_process, self.count_entrance)
        self.database.insert('INSERT INTO metricas (espaco, caso, tempo, \
                   entrance, created_at) VALUES (%s,  %s, %s, %s, now())',data)
        print(f"As informações de execução do {self.__case_number} foram armazenadas com sucesso no banco de dados.")