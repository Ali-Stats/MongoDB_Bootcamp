"""
File:
    31_match_stage.py

Purpose:
    Demonstrate MongoDB Aggregation Match Stage ($match).

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


def get_customers():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    pipeline = [
        {
            "$match": {
                "city": "Delhi"
            }
        }
    ]

    results = customers.aggregate(pipeline)

    return results


def main():

    customers = get_customers()

    print("=" * 60)
    print("CUSTOMERS FROM DELHI")
    print("=" * 60)

    for customer in customers:
        print(customer)


if __name__ == "__main__":
    main()