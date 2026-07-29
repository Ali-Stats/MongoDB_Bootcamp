"""
File:
    10_first_last.py

Purpose:
    Find the first and last order date for each customer
    using the $first and $last aggregation operators.

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


def first_last_order():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [
        {
            "$sort": {
                "orderDate": 1
            }
        },
        {
            "$group": {
                "_id": "$customerID",
                "firstOrderDate": {
                    "$first": "$orderDate"
                },
                "lastOrderDate": {
                    "$last": "$orderDate"
                }
            }
        },
        {
            "$limit": 10
        }
    ]

    results = orders.aggregate(pipeline)

    print("=" * 75)
    print("FIRST AND LAST ORDER DATE FOR EACH CUSTOMER")
    print("=" * 75)

    for index, customer in enumerate(results, start=1):

        first_date = customer["firstOrderDate"].strftime("%d-%b-%Y")
        last_date = customer["lastOrderDate"].strftime("%d-%b-%Y")

        print("-" * 75)
        print(f"Record           : {index}")
        print(f"Customer ID      : {customer['_id']}")
        print(f"First Order Date : {first_date}")
        print(f"Last Order Date  : {last_date}")

    print("-" * 75)

    client.close()


if __name__ == "__main__":
    first_last_order()