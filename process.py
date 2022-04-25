from abc import ABC, abstractmethod
from utils.process_utils import get_time_response
from utils.database_manager import DatabaseManager
import os, psutil


class Process(ABC):
    def __init__(self):
        self.database = DatabaseManager("localhost", "poupay", os.environ['USER_MYSQL'], os.environ['PASSWORD_MYSQL'])

    def run(self):
        self.generate()
        self.save()

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def save(self):
        pass
