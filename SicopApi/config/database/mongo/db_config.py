from config.common.database.abcDatabase.abcDatabase import DataBaseConnection
from pymongo import CursorType
class DataBase(DataBaseConnection):
    
    def __init__(self,cursor,collection:str="licitaciones"):
       self.cursor= cursor
       self.db = cursor.get_collection(collection)

    def find(self,filter={}):
        result:CursorType = self.db.find(filter)
        return result
    
    def insertMany(self,data):
        result:CursorType = self.db.insert_many(data)
        return result
    
    def set_table(self,collection:str):
        self.db=self.cursor.get_collection(collection)