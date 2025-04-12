from Sicop.db.common.database.abcDatabase.abcDatabase import DataBaseConnection
from pymongo import CursorType
class DataBase(DataBaseConnection):
    
    def __init__(self,cursor):
       self.cursor= cursor
       #self.db = cursor.get_collection(collection)

    def find(self,filter={}):
        result:CursorType = self.db.find(filter)
        return result
    
    def insertMany(self,data):
        new_data= self.__format_array(data)
        result:CursorType = self.db.insert_many(new_data)
        return result
    
    def set_table(self,collection:str):
        self.db=self.cursor.get_collection(collection)

    def __format_data(self,data):
        return data.to_dict()
    
    def __format_array(self,data):
        array_format=[]
        for x in data:
            array_format.append(self.__format_data(x))    
        return array_format   