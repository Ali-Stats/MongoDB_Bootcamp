"""
File:
    02_one_to_one.py

Purpose:
    Demonstrate One-to-One Relationships
    in MongoDB.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""


def one_to_one_demo():

    print("=" * 100)
    print("ONE-TO-ONE RELATIONSHIP")
    print("=" * 100)

    print("\nEMBEDDED MODEL\n")

    embedded_customer = {

        "customerID": "C001",

        "customerName": "Syed Ali Ashraf",

        "wallet": {

            "walletID": "W001",

            "balance": 5200,

            "rewardPoints": 350

        }

    }

    print(embedded_customer)

    print()

    print("=" * 100)

    print("\nREFERENCED MODEL\n")

    customer = {

        "customerID": "C001",

        "customerName": "Syed Ali Ashraf"

    }

    wallet = {

        "walletID": "W001",

        "customerID": "C001",

        "balance": 5200,

        "rewardPoints": 350

    }

    print("Customer Collection")

    print(customer)

    print()

    print("Wallet Collection")

    print(wallet)

    print()

    print("=" * 100)
    print("WHEN TO EMBED?")
    print("=" * 100)

    print("• Small documents")

    print("• Read together")

    print("• Rare updates")

    print()

    print("=" * 100)
    print("WHEN TO REFERENCE?")
    print("=" * 100)

    print("• Frequently updated")

    print("• Security separation")

    print("• Independent lifecycle")

    print("• Large documents")

    print()

    print("=" * 100)
    print("PROJECT EXAMPLE")
    print("=" * 100)

    print("Customer ↔ Wallet")

    print("Recommendation : Reference")

    print("Reason : Financial information changes independently.")


if __name__ == "__main__":

    one_to_one_demo()