from datetime import datetime
class Licitacion():
    number:str
    name:str
    descrip:str
    in_charge:str
    publishDate:datetime
    openingDate:datetime
    status:str

    def __init__(self,number,name,descrip,in_charge,publishDate,openingDate,status):
        self.number = number
        self.name = name
        self.descrip = descrip
        self.in_charge = in_charge
        self.publishDate = publishDate
        self.openingDate = openingDate
        self.status = status