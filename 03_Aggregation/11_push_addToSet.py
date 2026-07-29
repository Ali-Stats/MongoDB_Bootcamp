"""
File:
    11_push_addToSet.py

Purpose:
    Demonstrate the difference between
    $push and $addToSet.

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


def push_add_to_set():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [
        {
            "$group": {
                "_id": "$customerID",

                "paymentMethods": {
                    "$push": "$paymentMethod"
                },

                "uniquePaymentMethods": {
                    "$addToSet": "$paymentMethod"
                }
            }
        },
        {
            "$limit": 10
        }
    ]

    results = orders.aggregate(pipeline)

    print("=" * 90)
    print("PAYMENT METHODS USED BY CUSTOMERS")
    print("=" * 90)

    for index, customer in enumerate(results, start=1):

        print("-" * 90)
        print(f"Record                  : {index}")
        print(f"Customer ID             : {customer['_id']}")
        print(f"All Payment Methods     : {customer['paymentMethods']}")
        print(f"Unique Payment Methods  : {customer['uniquePaymentMethods']}")

    print("-" * 90)

    client.close()


if __name__ == "__main__":
    push_add_to_set()