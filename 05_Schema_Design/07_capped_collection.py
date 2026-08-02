"""
File:
    07_capped_collection.py

Purpose:
    Demonstrate MongoDB Capped Collections.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from datetime import datetime

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME
)


def capped_collection_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection_name = "log_demo"

    if collection_name in db.list_collection_names():

        db.drop_collection(collection_name)

    db.command({

        "create": collection_name,

        "capped": True,

        "size": 10240,

        "max": 5

    })

    logs = db[collection_name]

    print("=" * 100)
    print("CAPPED COLLECTION CREATED")
    print("=" * 100)

    for i in range(1, 8):

        logs.insert_one({

            "logID": i,

            "message": f"Application Log {i}",

            "createdAt": datetime.utcnow()

        })

        print(f"Inserted Log {i}")

    print()

    print("=" * 100)
    print("DOCUMENTS PRESENT")
    print("=" * 100)

    for log in logs.find({}, {"_id": 0}):

        print("-" * 100)

        print(log)

    print("-" * 100)

    client.close()


if __name__ == "__main__":

    capped_collection_demo()