"""
File:
    15_sort_limit.py

Purpose:
    Sort and limit MongoDB query results.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient
from pymongo import DESCENDING

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME
)


def get_oldest_customers():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    cursor = (
        customers
        .find(
            {},
            {
                "_id": 0,
                "customerID": 1,
                "name": 1,
                "age": 1
            }
        )
        .sort("age", DESCENDING)
        .limit(10)
    )

    return cursor


def main():

    customers = get_oldest_customers()

    print("=" * 60)
    print("TOP 10 OLDEST CUSTOMERS")
    print("=" * 60)

    for customer in customers:

        print(
            customer["customerID"],
            customer["name"],
            customer["age"]
        )


if __name__ == "__main__":
    main()