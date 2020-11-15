import pymongo


client = pymongo.MongoClient("mongodb+srv://cluster0.idatz.mongodb.net/<dbname>' --username Aidan")

client.list_database_names()