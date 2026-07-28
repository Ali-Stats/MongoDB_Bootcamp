"""
File:
    21_lte_operator.py

Purpose:
    Demonstrate MongoDB Less Than or Equal Operator ($lte).

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient

from Dataset.config import MONGO_URI, DATABASE_NAME


def get_customers():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    cursor = customers.find(
        {
            "age": {
                "$lte": 30
            }
        },
        {
            "_id": 0,
            "customerID": 1,
            "name": 1,
            "age": 1
        }
    )

    return cursor


def main():

    customers = get_customers()

    print("=" * 60)
    print("CUSTOMERS AGE <= 30")
    print("=" * 60)

    for customer in customers:
        print(customer)


if __name__ == "__main__":
    main()