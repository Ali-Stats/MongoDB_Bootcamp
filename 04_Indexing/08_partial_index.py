"""
File:
    08_partial_index.py

Purpose:
    Demonstrate MongoDB Partial Index.

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


def partial_index_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    print("=" * 100)
    print("CREATING PARTIAL INDEX")
    print("=" * 100)

    index_name = orders.create_index(

        [

            ("orderStatus", 1)

        ],

        partialFilterExpression={

            "orderStatus": "Delivered"

        }

    )

    print(f"\nIndex Created : {index_name}")

    print()

    print("=" * 100)
    print("SAMPLE DELIVERED ORDERS")
    print("=" * 100)

    results = orders.find(

        {

            "orderStatus": "Delivered"

        },

        {

            "_id": 0,

            "orderID": 1,

            "customerID": 1,

            "restaurantID": 1,

            "grandTotal": 1,

            "orderStatus": 1

        }

    ).limit(10)

    for index, order in enumerate(results, start=1):

        print("-" * 100)

        print(f"Record         : {index}")
        print(f"Order ID       : {order['orderID']}")
        print(f"Customer ID    : {order['customerID']}")
        print(f"Restaurant ID  : {order['restaurantID']}")
        print(f"Grand Total    : ₹{order['grandTotal']:,.2f}")
        print(f"Status         : {order['orderStatus']}")

    print("-" * 100)

    print()

    print("=" * 100)
    print("AVAILABLE INDEXES")
    print("=" * 100)

    for index in orders.list_indexes():

        print("-" * 100)
        print(f"Index Name : {index['name']}")
        print(f"Key        : {index['key']}")

    print("-" * 100)

    client.close()


if __name__ == "__main__":

    partial_index_demo()