"""
File:
    29_count_documents.py

Purpose:
    Count documents in MongoDB.

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


def count_customers():

    client = MongoClient(MONGO_URI)

    database = client[DATABASE_NAME]

    customers = database["customers"]

    total_customers = customers.count_documents({})

    premium_customers = customers.count_documents(
        {
            "premiumMember": True
        }
    )

    delhi_customers = customers.count_documents(
        {
            "city": "Delhi"
        }
    )

    print("=" * 60)
    print(f"Total Customers   : {total_customers}")
    print(f"Premium Customers : {premium_customers}")
    print(f"Delhi Customers   : {delhi_customers}")
    print("=" * 60)


def main():

    count_customers()


if __name__ == "__main__":
    main()