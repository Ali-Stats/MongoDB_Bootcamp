"""
File:
    03_project.py

Purpose:
    Select specific fields using the $project stage.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME,
    ORDER_COLLECTION
)


def project_orders():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [
        {
            "$project": {
                "_id": 0,
                "orderID": 1,
                "customerID": 1,
                "grandTotal": 1
            }
        },
        {
            "$limit": 10
        }
    ]

    results = orders.aggregate(pipeline)

    print("=" * 60)
    print("Projected Orders (Top 10)")
    print("=" * 60)

    for index, order in enumerate(results, start=1):
        print(f"{index}. {order}")

    client.close()


if __name__ == "__main__":
    project_orders()