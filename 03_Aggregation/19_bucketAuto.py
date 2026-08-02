"""
File:
    19_bucketAuto.py

Purpose:
    Demonstrate the MongoDB $bucketAuto stage.

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


def bucket_auto_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [

        {

            "$bucketAuto": {

                "groupBy": "$grandTotal",

                "buckets": 5,

                "output": {

                    "totalOrders": {

                        "$sum": 1

                    },

                    "averageOrder": {

                        "$avg": "$grandTotal"

                    },

                    "totalRevenue": {

                        "$sum": "$grandTotal"

                    }

                }

            }

        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 100)
    print("AUTOMATIC ORDER VALUE DISTRIBUTION")
    print("=" * 100)

    for index, bucket in enumerate(results, start=1):

        print("-" * 100)

        print(f"Bucket          : {index}")
        print(f"Minimum Value   : ₹{bucket['_id']['min']:,.2f}")
        print(f"Maximum Value   : ₹{bucket['_id']['max']:,.2f}")
        print(f"Total Orders    : {bucket['totalOrders']}")
        print(f"Average Order   : ₹{bucket['averageOrder']:,.2f}")
        print(f"Total Revenue   : ₹{bucket['totalRevenue']:,.2f}")

    print("-" * 100)

    client.close()


if __name__ == "__main__":

    bucket_auto_demo()