"""
File:
    14_delete_many.py

Purpose:
    Delete multiple documents.

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


def delete_customers():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    result = customers.delete_many(
        {
            "city": "Hyderabad"
        }
    )

    return result


def main():

    result = delete_customers()

    print("=" * 60)
    print("DELETE MANY")
    print("=" * 60)

    print(result)

    print(type(result))

    print("\nDeleted Count:", result.deleted_count)


if __name__ == "__main__":
    main()