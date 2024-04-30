#!/usr/bin/env python3
""" Function """


def insert_school(mongo_collection: object, **kwargs):
    """function that inserts a new document in a collection
    based on kwargs

    Args:
        mongo_collection (object): pymongo collection object
    """
    data = mongo_collection.insert_one({**kwargs})
    return data.inserted_id
