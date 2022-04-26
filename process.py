from abc import ABC, abstractmethod
from utils.database_manager import DatabaseManager
import os
<<<<<<< HEAD

class Process(ABC):
    def __init__(self):
        self.count_entrance = 0
        self.database = DatabaseManager("localhost","poupay",os.environ['USER_MYSQL'], os.environ['PASSWORD_MYSQL'])
        
    def run(self):
        self.process()
        self._save()
=======


class Process(ABC):
    def __init__(self):
        self.database = DatabaseManager("localhost", "poupay", os.environ['USER_MYSQL'], os.environ['PASSWORD_MYSQL'])

    def run(self):
        self.generate()
        self.save()
>>>>>>> 864b9894bd1f52a06434e53af9d017b16236001a

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
<<<<<<< HEAD
    def _save(self):
        pass


=======
    def save(self):
        pass
>>>>>>> 864b9894bd1f52a06434e53af9d017b16236001a
