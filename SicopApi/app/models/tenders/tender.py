from datetime import datetime
class Tender():
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

    def to_dict(self):
        return {
        "number" :  self.number
        , "name" :  self.name
        , "descrip" :  self.descrip
        , "in_charge" :  self.in_charge
        , "publishDate" :  self.publishDate
        , "openingDate" :  self.openingDate
        , "status" :  self.status
        }