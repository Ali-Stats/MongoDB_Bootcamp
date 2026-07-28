"""
File:
    08_filter_demo.py

Purpose:
    Demonstrate MongoDB Filters (Query Documents).

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


def get_premium_customers():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    return customers.find(
        {
            "premiumMember": True
        }
    )


def main():

    premium_customers = get_premium_customers()

    print("=" * 60)
    print("PREMIUM CUSTOMERS")
    print("=" * 60)

    count = 0

    for customer in premium_customers:

        print(
            customer["customerID"],
            customer["name"],
            customer["premiumMember"]
        )

        count += 1

        if count == 10:
            break


if __name__ == "__main__":
    main()