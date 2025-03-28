from config import config
result = config.database.find()
for x in result:
    print(x)
