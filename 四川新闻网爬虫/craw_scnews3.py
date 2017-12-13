#coding:utf-8
import pymongo

client = pymongo.MongoClient('127.0.0.1',27017)
db = client.news

def Insert(data):
    collection = db.content
    collection.insert(data)
