from pymongo import MongoClient
from dotenv import main
import os
main.load_dotenv()
try:
    __uri=os.getenv("MONGO_URI")
    if not(len(__uri)) or __uri is None:
        __host=os.getenv("MONGO_HOST")
        try:
            __port=int(os.getenv("MONGO_PORT"))
        except ValueError:
            raise ValueError("Port Most Be a Number")
        if (not(len(__host)) or __host is None)  and (not(len(__host)) or __host is None):
            raise AttributeError(" Host And Port Can't be Undefined, Null  Or Empty")
        __HostClient = MongoClient(host=__host,port=__port)
    else:
        __HostClient = MongoClient(__uri)

    __dataBaseName=os.getenv("MONGO_DATABASE")
    DB=__HostClient.get_database(name=__dataBaseName)
except Exception as error:
    print(error)
    DB= None
