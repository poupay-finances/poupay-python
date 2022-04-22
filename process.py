from abc import ABC, abstractmethod
from utils.database_manager import DatabaseManager
import os

class Process(ABC):
    def __init__(self):
        self.count_entrance = 0
        self.database = DatabaseManager("localhost","poupay",os.environ['USER_MYSQL'], os.environ['PASSWORD_MYSQL'])
        
    def run(self):
        self.process()
        self._save()

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def _save(self):
        pass


