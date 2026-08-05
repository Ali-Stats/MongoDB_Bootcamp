"""
File:
    08_collation.py

Purpose:
    Demonstrate MongoDB Collation.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient
from pymongo.collation import Collation

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME
)

COLLECTION_NAME = "customer_collation"


def line():

    print("=" * 100)


def collation_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection = db[COLLECTION_NAME]

    collection.delete_many({})

    collection.insert_many(

        [

            {"name": "Rahul"},

            {"name": "rahul"},

            {"name": "RAHUL"},

            {"name": "Priya"},

            {"name": "PRIYA"}

        ]

    )

    line()

    print("Documents")

    line()

    print()

    for document in collection.find({}, {"_id": 0}):

        print(document)

    print()

    search_name = input(

        "Enter Name : "

    )

    print()

    line()

    print("Case Sensitive Search")

    line()

    print()

    for document in collection.find(

        {

            "name": search_name

        },

        {

            "_id": 0

        }

    ):

        print(document)

    print()

    line()

    print("Case Insensitive Search")

    line()

    print()

    for document in collection.find(

        {

            "name": search_name

        },

        {

            "_id": 0

        },

        collation=Collation(

            locale="en",

            strength=2

        )

    ):

        print(document)

    client.close()


if __name__ == "__main__":

    collation_demo()