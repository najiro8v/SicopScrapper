import os
import re
from datetime import datetime
from bs4 import BeautifulSoup
from .scrapper_config import header,MainURL,getUrlPage
from models.licitaciones import licitacion
from app.services.request.request_service import Axios

Licitations=[]
def getJustNumber(text:str):
    try:
        number = "".join(re.findall(r'\d', text))
        return number
    except:
        return 0

def getDate(date_str):
    try:
        date_object = datetime.strptime(date_str.text, '%d/%m/%Y %H:%M')
        return date_object
    except:
        
        for string in date_str.stripped_strings:
            newDate = string
        date_object = datetime.strptime(newDate, '%d/%m/%Y %H:%M')
        return date_object

def getRowSicopFormat(td:BeautifulSoup):
    #Number And Name
    numberAndName = td[0].find("b")
    numberLicit=numberAndName.text
    nameLicit=numberAndName.next_sibling.next_element.text
    DescripciAll = td[1].find("a")
    #description
    DescripLicit=DescripciAll.text
    #person in charge 
    in_charge=DescripciAll.next_sibling.next_sibling.next_sibling.next_element.text
    #dates
    publishDate = getDate(td[2])
    openingDate = getDate(td[3])
    #status
    statusLicit = td[4].text
    newLicit= licitacion.Licitacion(numberLicit,nameLicit,DescripLicit,in_charge,publishDate,openingDate,statusLicit)
    return newLicit

def getScrapperSicop(page : int = 0):
    if(page == 0):
        urls = MainURL
    else:
        urls = getUrlPage(page) 
    text = ''
    try:
        response= Axios.Get(header=header,url=urls)
        if response.ok:
            text=response.text
    except Axios.axios.exceptions.ConnectionError as exc:
        print(exc)
    soup= BeautifulSoup(text, 'html.parser')
    TotalPageHtml=soup.find("div",attrs={"id": "total"}).text
    TotalPageText = TotalPageHtml.split("[")
    ActualPage = getJustNumber(TotalPageText[1].split("de")[0])
    EndPage = getJustNumber(TotalPageText[1].split("de")[1])
    TotalRow= getJustNumber(TotalPageText[0])
    table = soup.find_all('table',attrs={"class":"eptable"})
    
    if table is not None:
        for subTable in table:
            tr=subTable.find_all("tr")
            for subTr in tr:
                td=subTr.find_all("td")
                if len(td) > 0:
                    licit= getRowSicopFormat(td)
                    if licit is not None:
                        Licitations.append(licit)
    print("Actual Row :", ActualPage , "  - To: ",EndPage)
    
    if(ActualPage == EndPage):
        return 
    else:
        if(ActualPage != "0"):
            getScrapperSicop(int(ActualPage) + 1)
        else:
            return 
