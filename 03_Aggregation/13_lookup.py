"""
File:
    13_lookup.py

Purpose:
    Demonstrate MongoDB $lookup by joining
    orders and customers collections.

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


def lookup_orders_customers():

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
            "$limit": 10
        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 100)
    print("ORDERS WITH CUSTOMER DETAILS")
    print("=" * 100)

    for index, order in enumerate(results, start=1):

        print("-" * 100)

        print(f"Record          : {index}")
        print(f"Order ID        : {order['orderID']}")
        print(f"Customer ID     : {order['customerID']}")
        print(f"Customer Name   : {order['customerInfo']['name']}")
        print(f"Email           : {order['customerInfo']['email']}")
        print(f"City            : {order['customerInfo']['city']}")
        print(f"Premium Member  : {order['customerInfo']['premiumMember']}")
        print(f"Grand Total     : ₹{order['grandTotal']:,.2f}")

    print("-" * 100)

    client.close()


if __name__ == "__main__":

    lookup_orders_customers()