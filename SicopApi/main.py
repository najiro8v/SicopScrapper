import venv
from config import config
from app.services.scrapper import scrapper_service
from app.services.cleaner_data import cleaner_data
#scrapper_service.getScrapperSicop()
#config.database.insertMany(scrapper_service.Licitations)
newCleaner = cleaner_data.Cleaner(config.database)

newCleaner.Update_filter(filter={'status': 'En recepción de ofertas'})