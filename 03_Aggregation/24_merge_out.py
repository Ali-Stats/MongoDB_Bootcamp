"""
File:
    24_merge_out.py

Purpose:
    Demonstrate the MongoDB $merge and
    $out aggregation stages.

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


def merge_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [

        {

            "$group":{

                "_id":"$restaurantID",

                "totalRevenue":{

                    "$sum":"$grandTotal"

                },

                "totalOrders":{

                    "$sum":1

                }

            }

        },

        {

            "$merge":"restaurant_sales"

        }

    ]

    list(orders.aggregate(pipeline))

    print("=" * 100)
    print("MERGE COMPLETED")
    print("=" * 100)

    print()

    print("Aggregation results have been written to")

    print("Collection : restaurant_sales")

    print()

    print("Open MongoDB Compass")

    print("RetailAnalyticsDB")

    print("restaurant_sales")

    print("=" * 100)

    client.close()


def out_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    orders = db[ORDER_COLLECTION]

    pipeline = [

        {

            "$group":{

                "_id":"$paymentMethod",

                "totalOrders":{

                    "$sum":1

                }

            }

        },

        {

            "$out":"payment_summary"

        }

    ]

    list(orders.aggregate(pipeline))

    print()

    print("=" * 100)
    print("OUT COMPLETED")
    print("=" * 100)

    print()

    print("Aggregation results have been written to")

    print("Collection : payment_summary")

    print()

    print("Open MongoDB Compass")

    print("RetailAnalyticsDB")

    print("payment_summary")

    print("=" * 100)

    client.close()


if __name__ == "__main__":

    merge_demo()

    out_demo()