"""
File:
    26_min_max.py

Purpose:
    Find the minimum and maximum order value
    for each restaurant using the $min and
    $max aggregation operators.

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


def minimum_maximum_orders():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [
        {
            "$group": {
                "_id": "$restaurantID",

                "minimumOrder": {
                    "$min": "$grandTotal"
                },

                "maximumOrder": {
                    "$max": "$grandTotal"
                }
            }
        },
        {
            "$sort": {
                "maximumOrder": -1
            }
        },
        {
            "$limit": 10
        }
    ]

    results = orders.aggregate(pipeline)

    print("=" * 90)
    print("MINIMUM AND MAXIMUM ORDER VALUE FOR EACH RESTAURANT")
    print("=" * 90)

    for index, restaurant in enumerate(results, start=1):

        print("-" * 90)
        print(f"Record          : {index}")
        print(f"Restaurant ID   : {restaurant['_id']}")
        print(f"Minimum Order   : ₹{restaurant['minimumOrder']:,.2f}")
        print(f"Maximum Order   : ₹{restaurant['maximumOrder']:,.2f}")

    print("-" * 90)

    client.close()


if __name__ == "__main__":
    minimum_maximum_orders()