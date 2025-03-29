from abc import ABC, abstractmethod
class DataBaseConnection(ABC):
    
    def __init__(self,db):
        self.db = db

    @abstractmethod
    def find(self,filter):
        pass

   