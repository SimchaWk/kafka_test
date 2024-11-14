from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


def get_mongo_client():
    return MongoClient(os.environ['MONGO_URL'])


def get_all_messages_collection():
    db = get_mongo_client()['messages_archive']
    return db['all_messages']
