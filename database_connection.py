import pymongo

client = pymongo.MongoClient("mongodb://root:example@localhost:127017/")

db = client['srgan']

collection = db.get_collection('super_resolution')