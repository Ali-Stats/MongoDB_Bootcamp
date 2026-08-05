"""
File:
    04_find_one_and_update.py

Purpose:
    Demonstrate MongoDB find_one_and_update().

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

COLLECTION_NAME = "bank_accounts"


def line():

    print("=" * 100)


def withdraw_money():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection = db[COLLECTION_NAME]

    collection.delete_many({})

    collection.insert_one(

        {

            "accountNumber": "SB1001",

            "customerName": "Rahul Sharma",

            "balance": 10000

        }

    )

    line()

    print("BEFORE WITHDRAWAL")

    line()

    print()

    print(collection.find_one({}, {"_id": 0}))

    amount = int(

        input(

            "\nEnter Withdrawal Amount : "

        )

    )

    updated_document = collection.find_one_and_update(

        {

            "accountNumber": "SB1001",

            "balance": {

                "$gte": amount

            }

        },

        {

            "$inc": {

                "balance": -amount

            }

        },

        return_document=ReturnDocument.AFTER

    )

    print()

    line()

    print("AFTER WITHDRAWAL")

    line()

    print()

    if updated_document:

        print(updated_document)

    else:

        print("Insufficient Balance!")

    client.close()


if __name__ == "__main__":

    withdraw_money()