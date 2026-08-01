"""
File:
    17_count_sortByCount.py

Purpose:
    Demonstrate the MongoDB $count and
    $sortByCount aggregation stages.

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


def count_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    print("=" * 95)
    print("TOTAL NUMBER OF ORDERS")
    print("=" * 95)

    pipeline = [

        {
            "$count": "totalOrders"
        }

    ]

    results = list(orders.aggregate(pipeline))

    print(f"Total Orders : {results[0]['totalOrders']}")

    print()
    print("=" * 95)
    print("PAYMENT METHOD FREQUENCY")
    print("=" * 95)

    pipeline = [

        {
            "$sortByCount": "$paymentMethod"
        }

    ]

    results = orders.aggregate(pipeline)

    for index, payment in enumerate(results, start=1):

        print("-" * 95)

        print(f"Rank             : {index}")
        print(f"Payment Method   : {payment['_id']}")
        print(f"Total Orders     : {payment['count']}")

    print("-" * 95)

    client.close()


if __name__ == "__main__":

    count_demo()