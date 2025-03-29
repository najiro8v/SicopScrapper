import os
from bs4 import BeautifulSoup
from .scrapper_config import header,MainURL
from app.services.request.request_service import Axios


urls = [MainURL]  # strip `\n`
for url in urls:
    file_name = "Sicop.html"#//PurePath(url).name
    file_path= os.path.join(".",file_name)
    text = ''
    try:
        response= Axios.Get(header=header,url=url)
        print(response)
        if response.ok:
            text=response.text
    except Axios.axios.exceptions.ConnectionError as exc:
        print(exc)
    soup= BeautifulSoup(text, 'html.parser')
    table = soup.find_all('table')
    if table is not None:
        for subTable in table:
            tr=subTable.find_all("tr")
            for subTr in tr:
                td=subTr.find_all("td")
                for subTd in td:
                    print(subTd.get_text().strip())
        
        
