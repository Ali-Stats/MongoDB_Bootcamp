"""
File:
    03_replace_one.py

Purpose:
    Demonstrate MongoDB replace_one().

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

COLLECTION_NAME = "employees"


def line():

    print("=" * 100)


def replace_employee():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection = db[COLLECTION_NAME]

    collection.delete_many({})

    collection.insert_one(

        {

            "employeeID": "E001",

            "name": "Rahul",

            "department": "IT",

            "salary": 50000

        }

    )

    line()

    print("BEFORE REPLACE")

    line()

    print()

    print(collection.find_one({}, {"_id": 0}))

    print()

    result = collection.replace_one(

        {

            "employeeID": "E001"

        },

        {

            "employeeID": "E001",

            "name": "Rahul Sharma",

            "department": "HR",

            "salary": 70000,

            "experience": 5

        }

    )

    line()

    print("AFTER REPLACE")

    line()

    print()

    print(collection.find_one({}, {"_id": 0}))

    print()

    print(f"Matched Count : {result.matched_count}")

    print(f"Modified Count: {result.modified_count}")

    client.close()


if __name__ == "__main__":

    replace_employee()