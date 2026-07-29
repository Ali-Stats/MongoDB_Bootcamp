"""
File:
    06_skip.py

Purpose:
    Skip documents using the $skip stage.

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


def skip_orders():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [
        {
            "$project": {
                "_id": 0,
                "orderID": 1,
                "customerID": 1,
                "grandTotal": 1
            }
        },
        {
            "$skip": 10
        },
        {
            "$limit": 10
        }
    ]

    results = orders.aggregate(pipeline)

    print("=" * 60)
    print("Orders 11 - 20")
    print("=" * 60)

    for index, order in enumerate(results, start=11):
        print(f"{index}. {order}")

    client.close()


if __name__ == "__main__":
    skip_orders()