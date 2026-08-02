"""
File:
    06_unique_index.py

Purpose:
    Demonstrate MongoDB Unique Index.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME
)


def unique_index_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    customers = db["customer_demo"]

    customers.drop()

    print("=" * 100)
    print("CREATING UNIQUE INDEX")
    print("=" * 100)

    index_name = customers.create_index(

        [("email", 1)],

        unique=True

    )

    print(f"\nIndex Created : {index_name}")

    print()

    customer_1 = {

        "customerID": "C001",

        "name": "Syed Ali Ashraf",

        "email": "syed@gmail.com"

    }

    customer_2 = {

        "customerID": "C002",

        "name": "John Doe",

        "email": "syed@gmail.com"

    }

    customers.insert_one(customer_1)

    print("=" * 100)
    print("FIRST CUSTOMER INSERTED")
    print("=" * 100)

    print(customer_1)

    print()

    try:

        customers.insert_one(customer_2)

    except DuplicateKeyError as error:

        print("=" * 100)
        print("DUPLICATE KEY ERROR")
        print("=" * 100)

        print("MongoDB prevented duplicate email insertion.")

        print()

        print(error)

    client.close()


if __name__ == "__main__":

    unique_index_demo()