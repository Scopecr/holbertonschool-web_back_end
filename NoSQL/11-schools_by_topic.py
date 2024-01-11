#!/usr/bin/env python3
"""Code that returns a list of school having a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Code returns list of school having a specific topic"""
    return mongo_collection.find({"topics": topic})
