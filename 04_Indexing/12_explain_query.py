"""
File:
    12_explain_query.py

Purpose:
    Demonstrate MongoDB Explain Plan.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pprint import pprint

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME,
    ORDER_COLLECTION
)


def explain_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    print("=" * 100)
    print("STEP 1 - SAMPLE CUSTOMER")
    print("=" * 100)

    sample = orders.find_one({}, {"_id": 0, "customerID": 1})

    customer = sample["customerID"]

    print(f"Customer ID : {customer}")

    print()

    print("=" * 100)
    print("STEP 2 - EXECUTION PLAN")
    print("=" * 100)

    explain = db.command({

        "explain": {

            "find": ORDER_COLLECTION,

            "filter": {

                "customerID": customer

            }

        },

        "verbosity": "executionStats"

    })

    winning_stage = explain["queryPlanner"]["winningPlan"]

    print("Winning Plan")
    print("-" * 100)

    pprint(winning_stage)

    print()

    print("=" * 100)
    print("EXECUTION STATISTICS")
    print("=" * 100)

    stats = explain["executionStats"]

    print(f"Documents Returned : {stats['nReturned']}")
    print(f"Documents Examined : {stats['totalDocsExamined']}")
    print(f"Keys Examined      : {stats['totalKeysExamined']}")
    print(f"Execution Time(ms) : {stats['executionTimeMillis']}")

    print()

    client.close()


if __name__ == "__main__":

    explain_demo()