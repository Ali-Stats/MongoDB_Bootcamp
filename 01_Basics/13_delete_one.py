"""
File:
    13_delete_one.py

Purpose:
    Delete a single document from MongoDB.

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


def delete_customer():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    result = customers.delete_one(
        {
            "customerID": "CUST900001"
        }
    )

    return result


def main():

    result = delete_customer()

    print("=" * 60)
    print("DELETE ONE")
    print("=" * 60)

    print(result)

    print(type(result))

    print("\nDeleted Count:", result.deleted_count)


if __name__ == "__main__":
    main()