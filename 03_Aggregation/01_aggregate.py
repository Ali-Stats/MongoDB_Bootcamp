"""
File:
    01_aggregate.py

Purpose:
    Introduction to MongoDB Aggregation Framework.

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


def aggregate_orders():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db.orders

    pipeline = []

    results = orders.aggregate(pipeline)

    print("=" * 50)
    print("Orders")
    print("=" * 50)

    for document in results:
        print(document)

    client.close()


if __name__ == "__main__":
    aggregate_orders()