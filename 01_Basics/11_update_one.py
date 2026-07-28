"""
File:
    11_update_one.py

Purpose:
    Update a single document in MongoDB.

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


def update_customer():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    result = customers.update_one(
        {
            "customerID": "CUST900001"
        },
        {
            "$set": {
                "city": "Hyderabad"
            }
        }
    )

    return result


def main():

    result = update_customer()

    print("=" * 60)
    print("UPDATE ONE")
    print("=" * 60)

    print(result)

    print(type(result))

    print("\nMatched Count :", result.matched_count)
    print("Modified Count:", result.modified_count)


if __name__ == "__main__":
    main()