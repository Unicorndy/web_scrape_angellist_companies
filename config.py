#insert company data into mongoDb
from pymongo import MongoClient


client=MongoClient('localhost',27017)
db = client.angelCoScrapeMax
db_sg = client.angelCoScrapeSingapore
db_market = client.angelCoScrapeMarket