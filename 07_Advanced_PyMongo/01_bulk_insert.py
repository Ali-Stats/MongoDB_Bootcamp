"""
File:
    01_bulk_insert.py

Purpose:
    Demonstrate Bulk Insert using MongoDB insert_many().

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

COLLECTION_NAME = "bulk_customers"


def line():

    print("=" * 100)


def create_customers():

    customers = []

    for number in range(1, 101):

        customer = {

            "customerID": f"C{number:05}",

            "name": f"Customer {number}",

            "city": f"City {number % 10}",

            "premiumMember": number % 2 == 0,

            "loyaltyPoints": number * 10

        }

        customers.append(customer)

    return customers


def bulk_insert():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection = db[COLLECTION_NAME]

    line()

    print("MongoDB Bulk Insert Example")

    line()

    customers = create_customers()

    result = collection.insert_many(customers)

    print()

    print(f"Inserted Documents : {len(result.inserted_ids)}")

    print()

    print("First Inserted ID")

    print(result.inserted_ids[0])

    print()

    print("Last Inserted ID")

    print(result.inserted_ids[-1])

    client.close()


if __name__ == "__main__":

    bulk_insert()