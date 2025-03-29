from config.common.database.abcDatabase.abcDatabase import DataBaseConnection
from .sql import DB
from sqlite3 import Cursor

class DataBase(DataBaseConnection):
    
    def find(self,filter=""):
        result:Cursor = self.db.execute("SELECT * FROM licitaciones")
        return result

dataBase = DataBase(DB)

