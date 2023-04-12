#!/usr/bin/env python3
"""
A python function
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on name
    mongo_collection: The collection to be used
    name: name to be affected
    topics: changes to be made
    """
    return mongo_collection.update_many({
            "name": name
        },
        {
            "$set:": {
                "topics": topics
            }
        })
