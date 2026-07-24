"""
File:
    01_connect.py

Purpose:
    Establish a connection between Python and MongoDB.

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
    Creates and returns a database object.
    """

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    return database


def main():

    database = connect_database()

    print("=" * 50)
    print("MongoDB Connected Successfully")
    print("=" * 50)
    print(f"Database : {database.name}")


if __name__ == "__main__":
    main()