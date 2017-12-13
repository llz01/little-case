import pymongo

client = pymongo.MongoClient('',)
db = client.news

def InsertNews(data):
    collection = db.content
    collection.insert(data)
    
def InsertComments(data):
    collection = db.comment
    collection.insert(data)
