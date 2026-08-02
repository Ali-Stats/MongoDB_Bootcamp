"""
File:
    06_json_schema.py

Purpose:
    Demonstrate MongoDB JSON Schema Validation.

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


def json_schema_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection_name = "customer_schema_demo"

    if collection_name in db.list_collection_names():

        db.drop_collection(collection_name)

    db.command({

        "create": collection_name,

        "validator": {

            "$jsonSchema": {

                "bsonType": "object",

                "required": [

                    "customerID",

                    "customerName",

                    "age",

                    "membership",

                    "phone"

                ],

                "properties": {

                    "customerID": {

                        "bsonType": "string"

                    },

                    "customerName": {

                        "bsonType": "string",

                        "minLength": 3,

                        "maxLength": 50

                    },

                    "age": {

                        "bsonType": "int",

                        "minimum": 18,

                        "maximum": 100

                    },

                    "membership": {

                        "enum": [

                            "Silver",

                            "Gold",

                            "Platinum"

                        ]

                    },

                    "phone": {

                        "bsonType": "string",

                        "pattern": "^[0-9]{10}$"

                    }

                }

            }

        },

        "validationLevel": "strict",

        "validationAction": "error"

    })

    customers = db[collection_name]

    print("=" * 100)
    print("JSON SCHEMA COLLECTION CREATED")
    print("=" * 100)

    valid_customer = {

        "customerID": "C001",

        "customerName": "Syed Ali Ashraf",

        "age": 33,

        "membership": "Gold",

        "phone": "9876543210"

    }

    invalid_customer = {

        "customerID": "C002",

        "customerName": "A",

        "age": 12,

        "membership": "Diamond",

        "phone": "ABCDE12345"

    }

    customers.insert_one(valid_customer)

    print("\nValid Customer Inserted Successfully\n")

    try:

        customers.insert_one(invalid_customer)

    except WriteError as error:

        print("=" * 100)
        print("JSON SCHEMA VALIDATION FAILED")
        print("=" * 100)

        print(error)

    client.close()


if __name__ == "__main__":

    json_schema_demo()