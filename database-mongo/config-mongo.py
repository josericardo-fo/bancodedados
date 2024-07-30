from pymongo import MongoClient


def get_mongo_client():
    client = MongoClient("mongodb://localhost:27017/")
    return client


def get_database(db_name):
    client = get_mongo_client()
    return client[db_name]
