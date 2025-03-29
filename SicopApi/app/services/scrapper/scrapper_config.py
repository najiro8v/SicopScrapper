from dotenv import main
from config.setting import BASE_DIR
import os
import sys
main.load_dotenv()
# &page_no=2

with open(BASE_DIR/"txtData/params.txt","r") as fh:
     _Cookie = fh.readline()

_MainURL=os.getenv("URL_SICOP")
_MainHeader=os.getenv("URL_HEADER_MANDATORY_SICOP_REFERER")
MainURL =_MainURL + f"?cartelTestYn=Y&cartelNm=&proceType=&cartelInstCd=&instNm=&regDtFrom=11%2F09%2F2024&regDtTo=10%2F03%2F2025&openbidDtFrom=11%2F09%2F2024&openbidDtTo=09%2F05%2F2025&instCartelNo=&cartelNo=&prodNm=&prodUnitUserYn=&prodUnit=&cateId=&prodCate=&biddocRcvYn=Y"
header={"referer":_MainHeader,"Cookie":_Cookie}