"""
File:
    30_distinct.py

Purpose:
    Demonstrate MongoDB distinct() method.

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


def get_distinct_cities():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    cities = customers.distinct("city")

    print("=" * 60)
    print("DISTINCT CITIES")
    print("=" * 60)

    for city in cities:
        print(city)


def main():

    get_distinct_cities()


if __name__ == "__main__":
    main()