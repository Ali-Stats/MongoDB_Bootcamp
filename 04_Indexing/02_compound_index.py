"""
File:
    02_compound_index.py

Purpose:
    Demonstrate Compound Indexes.

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


def compound_index_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    print("=" * 100)
    print("CREATING COMPOUND INDEX")
    print("=" * 100)

    index_name = orders.create_index(

        [

            ("customerID", 1),

            ("orderStatus", 1)

        ]

    )

    print(f"\nIndex Created : {index_name}")

    print()

    print("=" * 100)
    print("AVAILABLE INDEXES")
    print("=" * 100)

    indexes = orders.list_indexes()

    for index in indexes:

        print("-" * 100)

        print(f"Index Name : {index['name']}")
        print(f"Keys       : {index['key']}")

    print("-" * 100)

    print()

    print("=" * 100)
    print("SAMPLE QUERY USING COMPOUND INDEX")
    print("=" * 100)

    results = orders.find(

        {

            "customerID": "C00001",

            "orderStatus": "Delivered"

        }

    ).limit(5)

    for i, order in enumerate(results, start=1):

        print("-" * 100)

        print(f"Record         : {i}")
        print(f"Order ID       : {order['orderID']}")
        print(f"Customer ID    : {order['customerID']}")
        print(f"Order Status   : {order['orderStatus']}")
        print(f"Grand Total    : ₹{order['grandTotal']:,.2f}")

    print("-" * 100)

    client.close()


if __name__ == "__main__":

    compound_index_demo()