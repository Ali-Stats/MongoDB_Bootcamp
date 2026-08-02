"""
File:
    05_schema_validation.py

Purpose:
    Demonstrate MongoDB Schema Validation.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient
from pymongo.errors import WriteError

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME
)


def schema_validation_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection_name = "customer_validation_demo"

    if collection_name in db.list_collection_names():

        db.drop_collection(collection_name)

    db.command({

        "create": collection_name,

        "validator": {

            "$jsonSchema": {

                "bsonType": "object",

                "required": [

                    "customerID",

                    "customerName"

                ]

            }

        },

        "validationLevel": "strict",

        "validationAction": "error"

    })

    customers = db[collection_name]

    print("=" * 100)
    print("VALID COLLECTION CREATED")
    print("=" * 100)

    valid_customer = {

        "customerID": "C001",

        "customerName": "Syed Ali Ashraf"

    }

    invalid_customer = {

        "customerID": "C002"

    }

    customers.insert_one(valid_customer)

    print("\nValid document inserted successfully.\n")

    try:

        customers.insert_one(invalid_customer)

    except WriteError as error:

        print("=" * 100)
        print("VALIDATION ERROR")
        print("=" * 100)

        print(error)

    client.close()


if __name__ == "__main__":

    schema_validation_demo()