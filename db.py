from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "mongodb+srv://baselanaya:<password>@cluster1.ssuf1ci.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('Food')
user_collection = pymongo.collection.Collection(db, 'Food')