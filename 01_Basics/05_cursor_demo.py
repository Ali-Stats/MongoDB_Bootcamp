"""
File:
    05_cursor_demo.py

Purpose:
    Demonstrate how MongoDB Cursor works.

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


def get_cursor():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    return customers.find()


def main():

    cursor = get_cursor()

    print("=" * 60)
    print("FIRST LOOP")
    print("=" * 60)

    count = 0

    for customer in cursor:

        print(customer["name"])

        count += 1

        if count == 5:
            break

    print("\n")

    print("=" * 60)
    print("SECOND LOOP")
    print("=" * 60)

    count = 0

    for customer in cursor:

        print(customer["name"])

        count += 1

        if count == 5:
            break


if __name__ == "__main__":
    main()