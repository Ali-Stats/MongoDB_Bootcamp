"""
File:
    08_group_average.py

Purpose:
    Calculate average order value using $avg.

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


def average_order_value():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [
        {
            "$group": {
                "_id": "$restaurantID",
                "averageOrderValue": {
                    "$avg": "$grandTotal"
                }
            }
        },
        {
            "$sort": {
                "averageOrderValue": -1
            }
        },
        {
            "$limit": 10
        }
    ]

    results = orders.aggregate(pipeline)

    print("=" * 60)
    print("Top Restaurants by Average Order Value")
    print("=" * 60)

    for index, restaurant in enumerate(results, start=1):
        print(f"{index}. {restaurant}")

    client.close()


if __name__ == "__main__":
    average_order_value()