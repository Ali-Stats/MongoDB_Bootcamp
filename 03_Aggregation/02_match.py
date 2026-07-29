"""
File:
    02_match.py

Purpose:
    Filter documents using the $match stage.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME,
    ORDER_COLLECTION
)


def match_orders():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [
        {
            "$match": {
                "orderStatus": "Delivered"
            }
        }
    ]

    results = orders.aggregate(pipeline)

    print("=" * 60)
    print("Delivered Orders")
    print("=" * 60)

    for order in results:
        print(order)

    client.close()


if __name__ == "__main__":
    match_orders()