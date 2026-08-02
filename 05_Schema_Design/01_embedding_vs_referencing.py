"""
File:
    01_embedding_vs_referencing.py

Purpose:
    Demonstrate Embedding vs Referencing
    in MongoDB.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""


def schema_design_demo():

    print("=" * 100)
    print("EMBEDDING VS REFERENCING")
    print("=" * 100)

    print("\nEMBEDDED DOCUMENT\n")

    embedded = {

        "orderID": "ORD001",

        "customer": {

            "customerID": "C001",

            "name": "Syed Ali Ashraf",

            "phone": "9876543210"

        },

        "grandTotal": 950

    }

    print(embedded)

    print()

    print("=" * 100)

    print("\nREFERENCED DOCUMENT\n")

    order = {

        "orderID": "ORD001",

        "customerID": "C001",

        "grandTotal": 950

    }

    customer = {

        "customerID": "C001",

        "name": "Syed Ali Ashraf",

        "phone": "9876543210"

    }

    print("Order Collection")

    print(order)

    print()

    print("Customer Collection")

    print(customer)

    print()

    print("=" * 100)

    print("PROJECT EXAMPLE")
    print("=" * 100)

    print()

    print("Our Food Delivery Project uses REFERENCING.")

    print("Orders store customerID and restaurantID.")

    print("Customer and Restaurant details are fetched using $lookup.")

    print()

    print("=" * 100)

    print("WHEN TO EMBED?")
    print("=" * 100)

    print("• Small child documents")

    print("• Read together")

    print("• Rarely updated")

    print()

    print("=" * 100)

    print("WHEN TO REFERENCE?")
    print("=" * 100)

    print("• Shared data")

    print("• Frequently updated")

    print("• Large collections")

    print("• Multiple relationships")


if __name__ == "__main__":

    schema_design_demo()