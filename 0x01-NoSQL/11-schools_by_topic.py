#!/usr/bin/env python3
"""
A python function
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    a function that returns the list of schools having a specific topic
    """
    return mongo_collection.find({"topic": topic})
