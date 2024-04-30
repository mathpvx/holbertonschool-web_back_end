#!/usr/bin/env python3
""" Function """


from typing import List


def update_topics(mongo_collection: object, name: str, topics: List[str]):
    """Change all topics of a school document based on the name
    """
    data = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return data.modified_count
