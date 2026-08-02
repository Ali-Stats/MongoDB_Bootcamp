"""
File:
    09_data_modeling_case_study.py

Purpose:
    Food Delivery System Data Modeling Case Study.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""


def case_study():

    print("=" * 100)
    print("FOOD DELIVERY SYSTEM - DATA MODELING CASE STUDY")
    print("=" * 100)

    print("\nCollections")

    collections = [

        "customers",
        "restaurants",
        "menu",
        "orders",
        "payments",
        "drivers",
        "reviews",
        "coupons",
        "customer_addresses",
        "restaurant_promotions"

    ]

    for collection in collections:

        print(f"• {collection}")

    print()

    print("=" * 100)
    print("EMBEDDED DOCUMENTS")
    print("=" * 100)

    embedded = [

        "Order Items",

        "Small Customer Preferences",

        "Delivery Address (Optional)"

    ]

    for item in embedded:

        print(f"• {item}")

    print()

    print("=" * 100)
    print("REFERENCED DOCUMENTS")
    print("=" * 100)

    referenced = [

        "Customers",

        "Restaurants",

        "Menu",

        "Payments",

        "Drivers",

        "Reviews"

    ]

    for item in referenced:

        print(f"• {item}")

    print()

    print("=" * 100)
    print("RECOMMENDED INDEXES")
    print("=" * 100)

    indexes = [

        "customerID (Unique)",

        "restaurantID (Unique)",

        "customerID (Orders)",

        "restaurantID + orderStatus (Compound)",

        "itemName (Text)",

        "location (2dsphere)"

    ]

    for index in indexes:

        print(f"• {index}")

    print()

    print("=" * 100)
    print("SCALABILITY")
    print("=" * 100)

    print("Designed to support millions of orders using")
    print("- Referencing")
    print("- Compound Indexes")
    print("- Embedded Order Items")
    print("- JSON Schema Validation")


if __name__ == "__main__":

    case_study()