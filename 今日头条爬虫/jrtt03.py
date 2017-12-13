#coding:utf-8
import pymongo

client = pymongo.MongoClient('127.0.0.1', 8000)
db = client.news
def InsertNews(data):
    collection = db.content
    collection.insert(data)
def InsertComments(data):
    collection = db.comment
    collection.insert(data)
