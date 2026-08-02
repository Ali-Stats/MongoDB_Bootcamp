"""
File:
    13_index_performance.py

Purpose:
    Compare MongoDB query performance
    with and without an index.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

import time

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME,
    ORDER_COLLECTION
)


def index_performance_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    print("=" * 100)
    print("STEP 1 - SAMPLE CUSTOMER")
    print("=" * 100)

    sample = orders.find_one(
        {},
        {
            "_id": 0,
            "customerID": 1
        }
    )

    customer = sample["customerID"]

    print(f"Customer ID : {customer}")

    print()

    print("=" * 100)
    print("STEP 2 - REMOVING customerID INDEX (IF EXISTS)")
    print("=" * 100)

    try:

        orders.drop_index("customerID_1")

        print("customerID_1 index removed.")

    except Exception:

        print("customerID_1 index not found.")

    print()

    print("=" * 100)
    print("QUERY WITHOUT INDEX")
    print("=" * 100)

    start = time.perf_counter()

    results = list(

        orders.find(

            {

                "customerID": customer

            }

        )

    )

    end = time.perf_counter()

    no_index_time = end - start

    print(f"Returned Documents : {len(results)}")

    print(f"Execution Time     : {no_index_time:.6f} seconds")

    print()

    print("=" * 100)
    print("STEP 3 - CREATING INDEX")
    print("=" * 100)

    orders.create_index(

        [

            ("customerID", 1)

        ]

    )

    print("customerID_1 created.")

    print()

    print("=" * 100)
    print("QUERY WITH INDEX")
    print("=" * 100)

    start = time.perf_counter()

    results = list(

        orders.find(

            {

                "customerID": customer

            }

        )

    )

    end = time.perf_counter()

    index_time = end - start

    print(f"Returned Documents : {len(results)}")

    print(f"Execution Time     : {index_time:.6f} seconds")

    print()

    print("=" * 100)
    print("PERFORMANCE SUMMARY")
    print("=" * 100)

    print(f"Without Index : {no_index_time:.6f} seconds")

    print(f"With Index    : {index_time:.6f} seconds")

    if index_time < no_index_time:

        improvement = no_index_time / index_time

        print(f"Approx Speedup : {improvement:.2f}x")

    else:

        print("Difference is very small.")

    client.close()


if __name__ == "__main__":

    index_performance_demo()