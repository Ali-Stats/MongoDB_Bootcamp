"""
File:
    09_index_hints.py

Purpose:
    Demonstrate MongoDB Index Hints.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME
)

COLLECTION_NAME = "customer_index_demo"


def line():

    print("=" * 100)


def index_hint_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection = db[COLLECTION_NAME]

    collection.drop()

    customers = []

    for number in range(1, 1001):

        customers.append(

            {

                "customerID": f"C{number:05}",

                "name": f"Customer {number}",

                "city": f"City {number % 10}",

                "email": f"user{number}@gmail.com"

            }

        )

    collection.insert_many(customers)

    collection.create_index("customerID")

    collection.create_index("city")

    collection.create_index("email")

    line()

    print("Indexes")

    line()

    print()

    for index in collection.list_indexes():

        print(index)

    print()

    line()

    print("Query Using Hint")

    line()

    print()

    results = collection.find(

        {

            "city": "City 5"

        }

    ).hint("city_1")

    count = 0

    for document in results:

        print(document)

        count += 1

        if count == 5:

            break

    print()

    print("Showing First 5 Matching Documents")

    client.close()


if __name__ == "__main__":

    index_hint_demo()