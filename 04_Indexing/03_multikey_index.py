"""
File:
    03_multikey_index.py

Purpose:
    Demonstrate MongoDB Multikey Indexes.

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


def multikey_index_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    print("=" * 100)
    print("CREATING MULTIKEY INDEX")
    print("=" * 100)

    index_name = orders.create_index(

        [

            ("items.menuID", 1)

        ]

    )

    print(f"\nIndex Created : {index_name}")

    print()

    print("=" * 100)
    print("SEARCHING FOR ORDERS CONTAINING MENU ITEM : M001")
    print("=" * 100)

    results = orders.find(

        {

            "items.menuID": "M000162"

        }

    ).limit(10)

    found = False

    for index, order in enumerate(results, start=1):

        found = True

        print("-" * 100)

        print(f"Record         : {index}")
        print(f"Order ID       : {order['orderID']}")
        print(f"Customer ID    : {order['customerID']}")
        print(f"Restaurant ID  : {order['restaurantID']}")
        print(f"Grand Total    : ₹{order['grandTotal']:,.2f}")

    if not found:

        print("No matching orders found.")

    print()

    print("=" * 100)
    print("AVAILABLE INDEXES")
    print("=" * 100)

    for index in orders.list_indexes():

        print("-" * 100)
        print(f"Index Name : {index['name']}")
        print(f"Keys       : {index['key']}")

    print("-" * 100)

    client.close()


if __name__ == "__main__":

    multikey_index_demo()