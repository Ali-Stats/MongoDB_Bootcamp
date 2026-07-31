"""
File:
    13_unwind.py

Purpose:
    Demonstrate the MongoDB $unwind stage by creating
    a temporary collection with embedded arrays.

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


def unwind_demo():

    # -------------------------------------------------
    # Connect to MongoDB
    # -------------------------------------------------

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    demo = db["unwind_demo"]

    # -------------------------------------------------
    # Remove old demo data
    # -------------------------------------------------

    demo.delete_many({})

    # -------------------------------------------------
    # Insert Sample Documents
    # -------------------------------------------------

    sample_data = [

        {
            "orderID": "ORD001",
            "customerID": "C001",

            "items": [

                {
                    "name": "Burger",
                    "price": 250
                },

                {
                    "name": "Fries",
                    "price": 120
                },

                {
                    "name": "Coke",
                    "price": 60
                }

            ]
        },

        {
            "orderID": "ORD002",
            "customerID": "C002",

            "items": [

                {
                    "name": "Pizza",
                    "price": 450
                },

                {
                    "name": "Garlic Bread",
                    "price": 180
                }

            ]
        },

        {
            "orderID": "ORD003",
            "customerID": "C003",

            "items": [

                {
                    "name": "Burger",
                    "price": 250
                },

                {
                    "name": "Pizza",
                    "price": 450
                },

                {
                    "name": "Brownie",
                    "price": 200
                }

            ]
        }

    ]

    demo.insert_many(sample_data)

    # -------------------------------------------------
    # Aggregation Pipeline
    # -------------------------------------------------

    pipeline = [

        {
            "$unwind": "$items"
        }

    ]

    results = demo.aggregate(pipeline)

    # -------------------------------------------------
    # Display Results
    # -------------------------------------------------

    print("=" * 95)
    print("UNWIND DEMONSTRATION")
    print("=" * 95)

    for index, order in enumerate(results, start=1):

        print("-" * 95)

        print(f"Record      : {index}")
        print(f"Order ID    : {order['orderID']}")
        print(f"Customer ID : {order['customerID']}")
        print(f"Item Name   : {order['items']['name']}")
        print(f"Price       : ₹{order['items']['price']:,.2f}")

    print("-" * 95)

    # -------------------------------------------------
    # BONUS EXAMPLE
    # Count how many times each item appears
    # -------------------------------------------------

    pipeline = [

        {
            "$unwind": "$items"
        },

        {
            "$group": {

                "_id": "$items.name",

                "timesOrdered": {

                    "$sum": 1

                }

            }

        },

        {

            "$sort": {

                "timesOrdered": -1

            }

        }

    ]

    results = demo.aggregate(pipeline)

    print()
    print("=" * 95)
    print("MOST ORDERED ITEMS")
    print("=" * 95)

    for index, item in enumerate(results, start=1):

        print("-" * 95)

        print(f"Rank            : {index}")
        print(f"Item            : {item['_id']}")
        print(f"Times Ordered   : {item['timesOrdered']}")

    print("-" * 95)

    client.close()


if __name__ == "__main__":

    unwind_demo()