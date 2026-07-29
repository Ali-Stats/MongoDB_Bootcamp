"""
File:
    09_group_multiple_fields.py

Purpose:
    Group documents using multiple fields.

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


def group_multiple_fields():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [
        {
            "$group": {
                "_id": {
                    "restaurantID": "$restaurantID",
                    "orderStatus": "$orderStatus"
                },
                "totalRevenue": {
                    "$sum": "$grandTotal"
                },
                "totalOrders": {
                    "$sum": 1
                }
            }
        },
        {
            "$sort": {
                "totalRevenue": -1
            }
        },
        {
            "$limit": 10
        }
    ]

    results = orders.aggregate(pipeline)

    print("=" * 70)
    print("Revenue by Restaurant and Order Status")
    print("=" * 70)

    for index, row in enumerate(results, start=1):
        print(f"{index}. {row}")

    client.close()


if __name__ == "__main__":
    group_multiple_fields()