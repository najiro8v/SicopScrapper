import sqlite3
from dotenv import main
import os
main.load_dotenv()
try:
    __uri=os.getenv("SQL_LITE__HOST")
    if not(len(__uri)) or __uri is None:
        raise AttributeError(" SQL LITE Host Can't be Undefined, Null  Or Empty")
    else:
        con = sqlite3.connect(__uri)
        DB = con.cursor()
except Exception as error:
    print(error)
    DB= None
