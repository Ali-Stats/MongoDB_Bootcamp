"""
File:
    06_find_one.py

Purpose:
    Demonstrate MongoDB find_one().

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


def get_customer():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    return customers.find_one()


def main():

    customer = get_customer()

    print("=" * 50)
    print("FIRST CUSTOMER")
    print("=" * 50)

    print(customer)

    print("\n")

    print(type(customer))


if __name__ == "__main__":
    main()