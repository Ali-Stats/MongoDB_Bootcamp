"""
File:
    01_connect.py

Purpose:
    Demonstrates how to establish a connection between
    Python and MongoDB using PyMongo.

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


def connect_database():
    """
    Creates a MongoDB client and returns the database object.
    """

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    return database


def main():

    database = connect_database()

    print("=" * 50)
    print("MongoDB Connected Successfully")
    print("=" * 50)
    print(f"Connected Database : {database.name}")


if __name__ == "__main__":
    main()