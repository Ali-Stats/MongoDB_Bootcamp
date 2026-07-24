"""
File:
    read_customers.py

Purpose:
    Demonstrates reading customer documents from MongoDB.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME,
    CUSTOMER_COLLECTION
)


def connect_database():
    """
    Returns the RetailAnalytics database.
    """

    client = MongoClient(MONGO_URI)

    return client[DATABASE_NAME]


def main():

    database = connect_database()

    customers = database[CUSTOMER_COLLECTION]

    result = customers.find()

    print("=" * 70)
    print("FIRST 10 CUSTOMERS")
    print("=" * 70)

    counter = 0

    for customer in result:

        print(
            f"{customer['customerID']} | "
            f"{customer['name']} | "
            f"{customer['city']} | "
            f"{customer['premiumMember']}"
        )

        counter += 1

        if counter == 10:
            break


if __name__ == "__main__":
    main()