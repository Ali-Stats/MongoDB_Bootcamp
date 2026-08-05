"""
File:
    03_commit_transaction.py

Purpose:
    Demonstrate committing a MongoDB transaction.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME,
    CUSTOMER_COLLECTION
)


def commit_transaction_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    customers = db[CUSTOMER_COLLECTION]

    print("=" * 100)
    print("BEFORE TRANSACTION")
    print("=" * 100)

    customer = customers.find_one()

    if customer is None:

        print("No customer found.")

        client.close()

        return

    customer_id = customer["_id"]

    old_points = customer.get("loyaltyPoints", 0)

    print(f"Customer ID       : {customer_id}")
    print(f"Old Loyalty Points: {old_points}")

    with client.start_session() as session:

        with session.start_transaction():

            result = customers.update_one(

                {"_id": customer_id},

                {
                    "$set": {
                        "loyaltyPoints": old_points + 100
                    }
                },

                session=session

            )

            print()

            print("=" * 100)
            print("TRANSACTION IN PROGRESS")
            print("=" * 100)

            print(f"Matched Documents : {result.matched_count}")
            print(f"Modified Documents: {result.modified_count}")

        print()

        print("Transaction Committed Successfully.")

    updated_customer = customers.find_one(
        {"_id": customer_id}
    )

    print()

    print("=" * 100)
    print("AFTER COMMIT")
    print("=" * 100)

    print(f"Customer ID       : {customer_id}")
    print(
        f"New Loyalty Points: "
        f"{updated_customer.get('loyaltyPoints', 0)}"
    )

    client.close()


if __name__ == "__main__":

    commit_transaction_demo()