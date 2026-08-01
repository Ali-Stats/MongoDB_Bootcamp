"""
File:
    14_addFields_set.py

Purpose:
    Demonstrate the MongoDB $addFields and
    $set aggregation stages.

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


def add_fields_demo():
    """
    Demonstrate the use of $addFields by
    calculating GST and Final Amount.
    """

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [

        {
            "$addFields": {

                "gst": {

                    "$multiply": [
                        "$grandTotal",
                        0.18
                    ]

                }

            }

        },

        {
            "$addFields": {

                "finalAmount": {

                    "$add": [
                        "$grandTotal",
                        "$gst"
                    ]

                }

            }

        },

        {
            "$limit": 10
        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 95)
    print("ADD FIELDS DEMONSTRATION")
    print("=" * 95)

    for index, order in enumerate(results, start=1):

        print("-" * 95)

        print(f"Record        : {index}")
        print(f"Order ID      : {order['orderID']}")
        print(f"Customer ID   : {order['customerID']}")
        print(f"Grand Total   : ₹{order['grandTotal']:,.2f}")
        print(f"GST (18%)     : ₹{order['gst']:,.2f}")
        print(f"Final Amount  : ₹{order['finalAmount']:,.2f}")

    print("-" * 95)

    client.close()


if __name__ == "__main__":
    add_fields_demo()