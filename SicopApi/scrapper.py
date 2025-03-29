from pathlib import PurePath,Path
from dotenv import main
import os
import sys
from bs4 import BeautifulSoup
import requests

main.load_dotenv()

MainURL=os.getenv("URL_SICOP")
MainHeader=os.getenv("URL_HEADER_MANDATORY_SICOP_REFERER")
print(MainURL)
with open("params.txt","r") as fh:
    Cookie = fh.readline()
MainURL +="?cartelTestYn=Y&cartelNm=&proceType=&cartelInstCd=&instNm=&regDtFrom=11%2F09%2F2024&regDtTo=10%2F03%2F2025&openbidDtFrom=11%2F09%2F2024&openbidDtTo=09%2F05%2F2025&instCartelNo=&cartelNo=&prodNm=&prodUnitUserYn=&prodUnit=&cateId=&prodCate=&biddocRcvYn=Y&page_no=2"
with open("urls.txt","r") as fh:
    urls= fh.readlines()
urls = [MainURL]  # strip `\n`
for url in urls:
    file_name = "Sicop.html"#//PurePath(url).name
    file_path= os.path.join(".",file_name)
    text = ''
    header={"referer":MainHeader,"Cookie":Cookie}
    try:
        response= requests.get(url,headers=header)
        print(response)
        if response.ok:
            text=response.text
    except requests.exceptions.ConnectionError as exc:
        print(exc)
    
    with open(file_name,"w", encoding="utf-8") as fh:
        fh.write(text)
    
    print("written to", file_path)
    with open(file_path, 'r', encoding="utf-8") as fh:
        content = fh.read()
    soup= BeautifulSoup(content, 'html.parser')
    container = soup.find('div',attrs={"class": "jurAbsatz"} )
    if container is not None:
        print (container.get_text())
