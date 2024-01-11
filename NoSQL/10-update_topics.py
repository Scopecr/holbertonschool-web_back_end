#!/usr/binenv python3
"""Python code that changes topics of a school document"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Python code that changes topics of a school document"""
    return mongo_collection.updateMany({'name': name}, {'$set': {'topics': topics}})
