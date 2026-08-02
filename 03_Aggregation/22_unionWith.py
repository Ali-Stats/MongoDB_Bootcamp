"""
File:
    22_unionWith.py

Purpose:
    Demonstrate the MongoDB $unionWith stage.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME,
    CUSTOMER_COLLECTION
)


def union_with_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    customers = db[CUSTOMER_COLLECTION]

    pipeline = [

        {

            "$project": {

                "_id": 0,

                "id": "$customerID",

                "name": "$name",

                "type": {

                    "$literal": "Customer"

                }

            }

        },

        {

            "$unionWith": {

                "coll": "restaurants",

                "pipeline": [

                    {

                        "$project": {

                            "_id": 0,

                            "id": "$restaurantID",

                            "name": "$restaurantName",

                            "type": {

                                "$literal": "Restaurant"

                            }

                        }

                    }

                ]

            }

        },

        {

            "$limit": 20

        }

    ]

    results = customers.aggregate(pipeline)

    print("=" * 100)
    print("CUSTOMERS + RESTAURANTS")
    print("=" * 100)

    for index, record in enumerate(results, start=1):

        print("-" * 100)

        print(f"Record : {index}")
        print(f"ID     : {record['id']}")
        print(f"Name   : {record['name']}")
        print(f"Type   : {record['type']}")

    print("-" * 100)

    client.close()


if __name__ == "__main__":

    union_with_demo()