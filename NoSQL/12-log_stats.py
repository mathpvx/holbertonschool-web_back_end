#!/usr/bin/env python3
"""provides statistics about Nginx logs from MongoDB"""


from pymongo import MongoClient


def main(nginx_collection):
    """Prints statistics about Nginx logs in MongoDB collection"""
    counter_logs = nginx_collection.count_documents({})
    print(f"{counter_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    logs = nginx_collection.find({"method": "GET", "path": "/status"})
    print(f"{len(list(logs))} status check")


if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    nginx_collection = db.nginx
    main(nginx_collection)
