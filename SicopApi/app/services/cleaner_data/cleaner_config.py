from config.common.database.abcDatabase.abcDatabase import DataBaseConnection
class Cleaner():
    def __init__(self,DataBase:DataBaseConnection):
        self.dataBase=DataBase

    def Update_filter(self,filter):
        data = self.dataBase.find(filter=filter)
        for x in data:
            print(x)

    def set_table(self,table):
        self.dataBase.set_table(table)
    
    def Clean_data(self,data=[],tableFrom:str="",tableTo:str=""):
        if(len(tableFrom) <= 0 and len(tableTo) <= 0 ):
            return None
        dataFrom=self.__find_by_table(tableFrom,{})
        dataTo=self.__find_by_table(tableTo,{})
    
    def __find_by_table(self,table,filter):
        self.dataBase.set_table(table)
        data = self.dataBase.find(filter=filter)
        return data

    
        


