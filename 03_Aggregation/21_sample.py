"""
File:
    21_sample.py

Purpose:
    Demonstrate the MongoDB $sample stage.

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


def sample_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [

        {

            "$sample": {

                "size": 10

            }

        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 100)
    print("RANDOM SAMPLE OF ORDERS")
    print("=" * 100)

    for index, order in enumerate(results, start=1):

        print("-" * 100)

        print(f"Record          : {index}")
        print(f"Order ID        : {order['orderID']}")
        print(f"Customer ID     : {order['customerID']}")
        print(f"Restaurant ID   : {order['restaurantID']}")
        print(f"Payment Method  : {order['paymentMethod']}")
        print(f"Order Status    : {order['orderStatus']}")
        print(f"Grand Total     : ₹{order['grandTotal']:,.2f}")

    print("-" * 100)

    client.close()


if __name__ == "__main__":

    sample_demo()