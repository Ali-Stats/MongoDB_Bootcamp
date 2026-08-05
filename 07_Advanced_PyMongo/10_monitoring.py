"""
File:
    10_monitoring.py

Purpose:
    Demonstrate MongoDB Query Monitoring and Performance Measurement.

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

COLLECTION_NAME = "monitor_demo"


def line():

    print("=" * 100)


def monitoring_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection = db[COLLECTION_NAME]

    collection.drop()

    customers = []

    for number in range(1, 10001):

        customers.append(

            {

                "customerID": f"C{number:05}",

                "name": f"Customer {number}",

                "city": f"City {number % 20}",

                "points": number * 10

            }

        )

    collection.insert_many(customers)

    collection.create_index("city")

    print()

    line()

    print("COLLECTION INFORMATION")

    line()

    print()

    print(f"Collection Name : {COLLECTION_NAME}")

    print(f"Total Documents : {collection.count_documents({})}")

    print()

    line()

    print("QUERY PERFORMANCE")

    line()

    print()

    start_time = time.perf_counter()

    results = list(

        collection.find(

            {

                "city": "City 5"

            }

        )

    )

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    print(f"Documents Returned : {len(results)}")

    print(f"Execution Time     : {execution_time:.6f} seconds")

    print()

    line()

    print("FIRST FIVE DOCUMENTS")

    line()

    print()

    for document in results[:5]:

        print(document)

    client.close()


if __name__ == "__main__":

    monitoring_demo()