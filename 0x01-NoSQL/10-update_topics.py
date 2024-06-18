#!/usr/bin/env python3
""" a Python function that changes all topics of a school document based on the name """
from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """ Update the topics of a school document based on the name """
    return mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
