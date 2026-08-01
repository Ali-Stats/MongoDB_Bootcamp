"""
File:
    16_replaceRoot_replaceWith.py

Purpose:
    Demonstrate the MongoDB $replaceRoot and
    $replaceWith aggregation stages.

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


def replace_root_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [

        {
            "$lookup": {

                "from": "customers",

                "localField": "customerID",

                "foreignField": "customerID",

                "as": "customerInfo"

            }

        },

        {
            "$unwind": "$customerInfo"
        },

        {
            "$replaceRoot": {

                "newRoot": "$customerInfo"

            }

        },

        {
            "$limit": 10
        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 95)
    print("REPLACE ROOT DEMONSTRATION")
    print("=" * 95)

    for index, customer in enumerate(results, start=1):

        print("-" * 95)

        print(f"Record           : {index}")
        print(f"Customer ID      : {customer['customerID']}")
        print(f"Customer Name    : {customer['name']}")
        print(f"Email            : {customer['email']}")
        print(f"City             : {customer['city']}")
        print(f"State            : {customer['state']}")
        print(f"Premium Member   : {customer['premiumMember']}")

    print("-" * 95)

    client.close()


if __name__ == "__main__":

    replace_root_demo()