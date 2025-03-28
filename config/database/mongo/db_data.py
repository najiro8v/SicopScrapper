from config.common.database.abcDatabase.abcDatabase import DataBaseConnection
from .mongo import DB
from pymongo import CursorType

class DataBase(DataBaseConnection):
    
    def find(self,filter=""):
        result:CursorType = self.db.find()
        return result

collection=DB.get_collection("licitaciones")
dataBase = DataBase(collection)

