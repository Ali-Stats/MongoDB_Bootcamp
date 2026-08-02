"""
File:
    03_one_to_many.py

Purpose:
    Demonstrate One-to-Many Relationships.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""


def one_to_many_demo():

    print("=" * 100)
    print("ONE-TO-MANY RELATIONSHIP")
    print("=" * 100)

    print("\nEMBEDDED MODEL\n")

    embedded_customer = {

        "customerID": "C001",

        "customerName": "Syed Ali Ashraf",

        "orders": [

            {
                "orderID": "ORD001",
                "grandTotal": 850
            },

            {
                "orderID": "ORD002",
                "grandTotal": 1200
            }

        ]

    }

    print(embedded_customer)

    print()

    print("=" * 100)

    print("\nREFERENCED MODEL\n")

    customer = {

        "customerID": "C001",

        "customerName": "Syed Ali Ashraf"

    }

    orders = [

        {
            "orderID": "ORD001",
            "customerID": "C001",
            "grandTotal": 850
        },

        {
            "orderID": "ORD002",
            "customerID": "C001",
            "grandTotal": 1200
        }

    ]

    print("Customer Collection")

    print(customer)

    print()

    print("Orders Collection")

    for order in orders:

        print(order)

    print()

    print("=" * 100)
    print("WHEN TO EMBED?")
    print("=" * 100)

    print("• Small number of child documents")

    print("• Read together")

    print("• Rare updates")

    print()

    print("=" * 100)
    print("WHEN TO REFERENCE?")
    print("=" * 100)

    print("• Thousands of child documents")

    print("• Frequently changing data")

    print("• Large collections")

    print("• Independent lifecycle")

    print()

    print("=" * 100)
    print("PROJECT EXAMPLE")
    print("=" * 100)

    print("Customers  →  Orders")

    print("Relationship : One-to-Many")

    print("Implementation : Referencing")

    print("Join Method : $lookup")


if __name__ == "__main__":

    one_to_many_demo()