#!/usr/bin/env python3
"""Python code that changes topics of a school document"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Python code that changes topics of a school document"""
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
