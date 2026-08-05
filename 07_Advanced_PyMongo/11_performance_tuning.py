"""
File:
    11_performance_tuning.py

Purpose:
    Demonstrate MongoDB Performance Tuning Best Practices.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

import time

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME
)

COLLECTION_NAME = "performance_demo"


def line():

    print("=" * 100)


def performance_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection = db[COLLECTION_NAME]

    collection.drop()

    customers = []

    for number in range(1, 50001):

        customers.append(

            {

                "customerID": f"C{number:05}",

                "name": f"Customer {number}",

                "city": f"City {number % 20}",

                "email": f"user{number}@gmail.com",

                "points": number * 10

            }

        )

    print()

    line()

    print("Loading Test Data")

    line()

    print()

    collection.insert_many(customers)

    collection.create_index("customerID")

    collection.create_index("city")

    collection.create_index("email")

    line()

    print("Query Without Projection")

    line()

    print()

    start = time.perf_counter()

    result = list(

        collection.find(

            {

                "city": "City 5"

            }

        )

    )

    end = time.perf_counter()

    print(f"Documents : {len(result)}")

    print(f"Execution Time : {end-start:.6f} sec")

    print()

    line()

    print("Query With Projection")

    line()

    print()

    start = time.perf_counter()

    result = list(

        collection.find(

            {

                "city": "City 5"

            },

            {

                "_id": 0,

                "customerID": 1,

                "name": 1,

                "city": 1

            }

        )

    )

    end = time.perf_counter()

    print(f"Documents : {len(result)}")

    print(f"Execution Time : {end-start:.6f} sec")

    print()

    line()

    print("First Five Results")

    line()

    print()

    for document in result[:5]:

        print(document)

    client.close()


if __name__ == "__main__":

    performance_demo()