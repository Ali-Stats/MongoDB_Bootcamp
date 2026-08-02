"""
File:
    09_hashed_index.py

Purpose:
    Demonstrate MongoDB Hashed Index.

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


def hashed_index_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    print("=" * 100)
    print("CREATING HASHED INDEX")
    print("=" * 100)

    index_name = orders.create_index(

        [

            ("customerID", "hashed")

        ]

    )

    print(f"\nIndex Created : {index_name}")

    print()

    print("=" * 100)
    print("EQUALITY SEARCH")
    print("=" * 100)

    print("Step 1 - Inspecting Sample Customer IDs")

    sample = orders.find(

        {},

        {

            "_id": 0,

            "customerID": 1

        }

    ).limit(5)

    customer_ids = []

    for doc in sample:

        print(doc)

        customer_ids.append(doc["customerID"])

    print()

    search_customer = customer_ids[0]

    print(f"Searching for Customer : {search_customer}")

    print()

    results = orders.find(

        {

            "customerID": search_customer

        }

    ).limit(10)

    for index, order in enumerate(results, start=1):

        print("-" * 100)

        print(f"Record         : {index}")
        print(f"Order ID       : {order['orderID']}")
        print(f"Customer ID    : {order['customerID']}")
        print(f"Restaurant ID  : {order['restaurantID']}")
        print(f"Grand Total    : ₹{order['grandTotal']:,.2f}")

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

    hashed_index_demo()