"""
File:
    07_connection_pooling.py

Purpose:
    Demonstrate MongoDB Connection Pooling.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient
import time

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME
)


def line():

    print("=" * 100)


def connection_pool_demo():

    line()

    print("Creating MongoClient...")

    line()

    client = MongoClient(

        MONGO_URI,

        maxPoolSize=5,

        minPoolSize=2

    )

    db = client[DATABASE_NAME]

    collection = db["bulk_customers"]

    for request in range(1, 11):

        count = collection.count_documents({})

        print(

            f"Request {request:02} "

            f"| Documents = {count}"

        )

        time.sleep(0.5)

    client.close()

    print()

    line()

    print("MongoClient Closed")

    line()


if __name__ == "__main__":

    connection_pool_demo()