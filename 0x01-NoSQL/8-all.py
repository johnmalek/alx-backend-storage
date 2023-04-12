#!/usr/bin/env python3
"""
A python function
"""
import pymongo


def list_all(mongo_collection):
    """
    A python function that lists all documnents in a collection
    mongo_collection: the collection to be checked
    Returns:
        empty list if no document found, the documents otherwise
    """
    docs = mongo_collection.find()
    return [doc for doc in docs]
