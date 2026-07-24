"""
File:
    02_list_databases.py

Purpose:
    List all databases available on the MongoDB server.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient
from Dataset.config import MONGO_URI


def list_databases():
    """
    Connects to MongoDB and returns
    all available database names.
    """

    client = MongoClient(MONGO_URI)

    return client.list_database_names()


def main():

    databases = list_databases()

    print("=" * 50)
    print("DATABASES AVAILABLE")
    print("=" * 50)

    for database in databases:
        print(database)


if __name__ == "__main__":
    main()