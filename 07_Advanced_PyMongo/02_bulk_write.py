"""
File:
    02_bulk_write.py

Purpose:
    Demonstrate MongoDB Bulk Write Operations.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient
from pymongo import InsertOne
from pymongo import UpdateOne
from pymongo import DeleteOne
from pymongo import ReplaceOne

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME
)

COLLECTION_NAME = "bulk_write_demo"


def line():

    print("=" * 100)


def bulk_write_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection = db[COLLECTION_NAME]

    collection.delete_many({})

    collection.insert_many(
        [
            {
                "customerID": "C00001",
                "name": "Rahul",
                "points": 100
            },
            {
                "customerID": "C00002",
                "name": "Priya",
                "points": 200
            }
        ]
    )

    operations = [

        InsertOne(

            {
                "customerID": "C00003",
                "name": "Aman",
                "points": 300
            }

        ),

        UpdateOne(

            {
                "customerID": "C00001"
            },

            {
                "$inc":
                {
                    "points": 50
                }
            }

        ),

        ReplaceOne(

            {
                "customerID": "C00002"
            },

            {
                "customerID": "C00002",
                "name": "Priya Sharma",
                "points": 500
            }

        ),

        DeleteOne(

            {
                "customerID": "C00003"
            }

        )

    ]

    line()

    print("Executing Bulk Write")

    line()

    result = collection.bulk_write(operations)

    print()

    print(f"Inserted Count : {result.inserted_count}")

    print(f"Modified Count : {result.modified_count}")

    print(f"Deleted Count  : {result.deleted_count}")

    print(f"Matched Count  : {result.matched_count}")

    print()

    print("Final Documents")

    print()

    for document in collection.find({}, {"_id": 0}):

        print(document)

    client.close()


if __name__ == "__main__":

    bulk_write_demo()