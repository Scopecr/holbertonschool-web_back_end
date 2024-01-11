#!/usr/bin/env python3
"""function that list all the documents in the database"""


def list_all(mongo_collection):
    """function that list all the documents in the database"""
    return mongo_collection.find({})
