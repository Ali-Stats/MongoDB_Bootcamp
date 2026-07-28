"""
File:
    03_list_collections.py

Purpose:
    Display all collections available inside a MongoDB database.

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


def list_collections():
    """
    Returns all collection names
    present inside the database.
    """

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    return database.list_collection_names()


def main():

    collections = list_collections()

    print("=" * 50)
    print(f"Collections in {DATABASE_NAME}")
    print("=" * 50)

    for collection in collections:
        print(collection)


if __name__ == "__main__":
    main()