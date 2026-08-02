"""
File:
    04_many_to_many.py

Purpose:
    Demonstrate Many-to-Many Relationships.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""


def many_to_many_demo():

    print("=" * 100)
    print("MANY-TO-MANY RELATIONSHIP")
    print("=" * 100)

    restaurant = {

        "restaurantID": "R001",

        "restaurantName": "Pizza Hub"

    }

    promotion = {

        "promotionID": "P001",

        "promotionName": "Weekend Offer"

    }

    bridge = {

        "restaurantID": "R001",

        "promotionID": "P001"

    }

    print("\nRESTAURANT COLLECTION\n")

    print(restaurant)

    print()

    print("PROMOTION COLLECTION\n")

    print(promotion)

    print()

    print("BRIDGE COLLECTION\n")

    print(bridge)

    print()

    print("=" * 100)
    print("REAL-WORLD EXAMPLES")
    print("=" * 100)

    examples = [

        "Students ↔ Courses",

        "Doctors ↔ Patients",

        "Actors ↔ Movies",

        "Users ↔ Roles",

        "Products ↔ Categories",

        "Restaurants ↔ Promotions"

    ]

    for example in examples:

        print(f"• {example}")

    print()

    print("=" * 100)
    print("PROJECT EXAMPLE")
    print("=" * 100)

    print("Restaurant ↔ Promotion")

    print("Relationship : Many-to-Many")

    print("Recommended Design : Bridge Collection")

    print("Reason : Avoids duplication and scales well.")

    print()

    print("=" * 100)
    print("BEST PRACTICE")
    print("=" * 100)

    print("• Avoid embedding both sides.")

    print("• Use separate collections.")

    print("• Store only IDs in the bridge collection.")

    print("• Use $lookup when related data is required.")


if __name__ == "__main__":

    many_to_many_demo()