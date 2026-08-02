"""
File:
    27_setWindowFields.py

Purpose:
    Demonstrate MongoDB $setWindowFields.

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


def window_function_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [

        {
            "$setWindowFields": {

                "sortBy": {

                    "orderDate": 1

                },

                "output": {

                    "runningRevenue": {

                        "$sum": "$grandTotal",

                        "window": {

                            "documents": [

                                "unbounded",

                                "current"

                            ]

                        }

                    }

                }

            }

        },

        {

            "$limit": 10

        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 110)
    print("RUNNING REVENUE USING WINDOW FUNCTIONS")
    print("=" * 110)

    for index, order in enumerate(results, start=1):

        print("-" * 110)

        print(f"Record           : {index}")
        print(f"Order ID         : {order['orderID']}")
        print(f"Order Date       : {order['orderDate'].strftime('%d-%b-%Y')}")
        print(f"Grand Total      : ₹{order['grandTotal']:,.2f}")
        print(f"Running Revenue  : ₹{order['runningRevenue']:,.2f}")

    print("-" * 110)

    client.close()


if __name__ == "__main__":

    window_function_demo()