"""
File:
    15_unset.py

Purpose:
    Demonstrate the MongoDB $unset stage.

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


def unset_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [

        {

            "$unset": [

                "paymentMethod",

                "orderStatus",

                "restaurantID"

            ]

        },

        {

            "$limit": 10

        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 95)
    print("UNSET DEMONSTRATION")
    print("=" * 95)

    for index, order in enumerate(results, start=1):

        print("-" * 95)

        print(f"Record        : {index}")
        print(f"Order ID      : {order['orderID']}")
        print(f"Customer ID   : {order['customerID']}")
        print(f"Grand Total   : ₹{order['grandTotal']:,.2f}")

    print("-" * 95)

    client.close()


if __name__ == "__main__":

    unset_demo()