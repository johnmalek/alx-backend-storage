#!/usr/bin/env python3
"""
A python function
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection
    mongo_collection: the collection to be used
    Returns:
        the new _id
    """
    docs = mongo_collection.insert_one(kwargs)
    return docs.inserted_id
