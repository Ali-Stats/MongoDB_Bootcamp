"""
File:
    18_bucket.py

Purpose:
    Demonstrate the MongoDB $bucket stage.

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


def bucket_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [

        {

            "$bucket": {

                "groupBy": "$grandTotal",

                "boundaries": [

                    0,
                    500,
                    1000,
                    2000,
                    5000

                ],

                "default": "Above 5000",

                "output": {

    "totalOrders": {

        "$sum": 1

    },

    "totalRevenue": {

        "$sum": "$grandTotal"

    },

    "averageOrder": {

        "$avg": "$grandTotal"

    }

}
            }

        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 95)
    print("ORDER VALUE DISTRIBUTION")
    print("=" * 95)

    for bucket in results:

        print("-" * 95)

        print(f"Bucket Range    : {bucket['_id']}")
        print(f"Total Orders    : {bucket['totalOrders']}")

    print("-" * 95)

    client.close()


if __name__ == "__main__":

    bucket_demo()