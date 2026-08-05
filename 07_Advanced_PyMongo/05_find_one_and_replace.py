"""
File:
    05_find_one_and_replace.py

Purpose:
    Demonstrate MongoDB find_one_and_replace().

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient
from pymongo import ReturnDocument

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME
)

COLLECTION_NAME = "employees_replace"


def line():

    print("=" * 100)


def replace_employee():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection = db[COLLECTION_NAME]

    collection.delete_many({})

    collection.insert_one(

        {

            "employeeID": "EMP001",

            "name": "Rahul",

            "department": "IT",

            "salary": 60000

        }

    )

    line()

    print("BEFORE REPLACE")

    line()

    print()

    print(collection.find_one({}, {"_id": 0}))

    updated_employee = collection.find_one_and_replace(

        {

            "employeeID": "EMP001"

        },

        {

            "employeeID": "EMP001",

            "name": "Rahul Sharma",

            "department": "HR",

            "salary": 85000,

            "experience": 6

        },

        return_document=ReturnDocument.AFTER

    )

    print()

    line()

    print("AFTER REPLACE")

    line()

    print()

    print(updated_employee)

    client.close()


if __name__ == "__main__":

    replace_employee()