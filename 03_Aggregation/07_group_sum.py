"""
File:
    07_group_sum.py

Purpose:
    Group documents and calculate total revenue.

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


def restaurant_revenue():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [
        {
            "$group": {
                "_id": "$restaurantID",
                "totalRevenue": {
                    "$sum": "$grandTotal"
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

    print("=" * 60)
    print("Top Restaurants by Revenue")
    print("=" * 60)

    for index, restaurant in enumerate(results, start=1):
        print(f"{index}. {restaurant}")

    client.close()


if __name__ == "__main__":
    restaurant_revenue()