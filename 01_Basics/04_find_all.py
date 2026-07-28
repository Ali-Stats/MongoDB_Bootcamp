"""
File:
    04_find_all.py

Purpose:
    Read every document from the customers collection.

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

    return customers.find()


def main():

    cursor = get_customers()

    print("=" * 60)
    print("ALL CUSTOMERS")
    print("=" * 60)

    for customer in cursor:
        print(customer)


if __name__ == "__main__":
    main()