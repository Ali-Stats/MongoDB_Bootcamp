"""
File:
    01_create_index.py

Purpose:
    Create and view MongoDB indexes.

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


def create_index_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    print("=" * 100)
    print("CREATING INDEX ON customerID")
    print("=" * 100)

    index_name = orders.create_index(

        [("customerID", 1)]

    )

    print(f"\nIndex Created : {index_name}")

    print("\n")

    print("=" * 100)
    print("AVAILABLE INDEXES")
    print("=" * 100)

    indexes = orders.list_indexes()

    for index in indexes:

        print("-" * 100)

        print(f"Index Name : {index['name']}")
        print(f"Key        : {index['key']}")

    print("-" * 100)

    client.close()


if __name__ == "__main__":

    create_index_demo()