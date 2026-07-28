"""
File:
    09_insert_one.py

Purpose:
    Insert a single document into MongoDB.

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


def insert_customer():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    result = customers.insert_one(
        {
            "customerID": "CUST900001",
            "name": "Syed Ali",
            "age": 33,
            "city": "Lucknow",
            "premiumMember": True
        }
    )

    return result


def main():

    result = insert_customer()

    print("=" * 60)
    print("INSERT ONE")
    print("=" * 60)

    print(result)

    print(type(result))

    print("\nInserted ID:")
    print(result.inserted_id)


if __name__ == "__main__":
    main()