"""
File:
    10_insert_many.py

Purpose:
    Insert multiple documents into MongoDB.

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


def insert_customers():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    result = customers.insert_many(
        [
            {
                "customerID": "CUST900002",
                "name": "Rahul Sharma",
                "age": 28,
                "city": "Delhi",
                "premiumMember": False
            },
            {
                "customerID": "CUST900003",
                "name": "Priya Singh",
                "age": 30,
                "city": "Mumbai",
                "premiumMember": True
            },
            {
                "customerID": "CUST900004",
                "name": "Aman Khan",
                "age": 35,
                "city": "Lucknow",
                "premiumMember": True
            }
        ]
    )

    return result


def main():

    result = insert_customers()

    print("=" * 60)
    print("INSERT MANY")
    print("=" * 60)

    print(result)

    print(type(result))

    print("\nInserted IDs:")

    for document_id in result.inserted_ids:
        print(document_id)

    print(type(result.inserted_ids))


if __name__ == "__main__":
    main()