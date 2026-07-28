"""
File:
    07_projection_demo.py

Purpose:
    Demonstrate Projection in MongoDB.

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


def get_customer_details():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    return customers.find(
        {},
        {
            "_id": 0,
            "customerID": 1,
            "name": 1,
            "city": 1
        }
    )


def main():

    customer_details = get_customer_details()

    print("=" * 60)
    print("CUSTOMER DETAILS")
    print("=" * 60)

    count = 0

    for customer in customer_details:

        print(customer)

        count += 1

        if count == 10:
            break


if __name__ == "__main__":
    main()