"""
File:
    20_facet.py

Purpose:
    Demonstrate the MongoDB $facet stage.

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


def facet_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [
        {
            "$facet" :{
            "topRestaurants": [
                {
                    "$group" : {
                        "_id":"$restaurantID",
                        "revenue" : {
                            "$sum" : "$grandTotal"
                        }
                    }

                },
                {
                    "$sort":{
                        "revenue": -1
                    }
                },
                {
                    "$limit" : 5
                }
            ],

            "paymentMethods":[
                {
                "$sortByCount":"$paymentMethod"
                }
            ],
            "orderStatus":[
            {
                "$sortByCount": "$orderStatus"
            }
            ]

    }
    }

    ]

    result = list(orders.aggregate(pipeline))[0]

    print("=" * 100)
    print("TOP RESTAURANTS")
    print("=" * 100)

    for index, restaurant in enumerate(result["topRestaurants"], start=1):

        print("-" * 100)

        print(f"Rank           : {index}")
        print(f"Restaurant ID  : {restaurant['_id']}")
        print(f"Revenue        : ₹{restaurant['revenue']:,.2f}")

    print()

    print("=" * 100)
    print("PAYMENT METHOD DISTRIBUTION")
    print("=" * 100)

    for index, payment in enumerate(result["paymentMethods"], start=1):

        print("-" * 100)

        print(f"Rank             : {index}")
        print(f"Payment Method   : {payment['_id']}")
        print(f"Orders           : {payment['count']}")

    print()

    print("=" * 100)
    print("ORDER STATUS DISTRIBUTION")
    print("=" * 100)

    for index, status in enumerate(result["orderStatus"], start=1):

        print("-" * 100)

        print(f"Rank           : {index}")
        print(f"Status         : {status['_id']}")
        print(f"Orders         : {status['count']}")

    print("-" * 100)

    client.close()


if __name__ == "__main__":

    facet_demo()