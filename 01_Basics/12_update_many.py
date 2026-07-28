"""
File:
    12_update_many.py

Purpose:
    Update multiple documents in MongoDB.

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


def update_customers():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    result = customers.update_many(
        {
            "city": "Lucknow"
        },
        {
            "$set": {
                "premiumMember": True
            }
        }
    )

    return result


def main():

    result = update_customers()

    print("=" * 60)
    print("UPDATE MANY")
    print("=" * 60)

    print(result)

    print(type(result))

    print("\nMatched Count :", result.matched_count)
    print("Modified Count:", result.modified_count)


if __name__ == "__main__":
    main()