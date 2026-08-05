"""
File:
    04_abort_transaction.py

Purpose:
    Demonstrate aborting a MongoDB transaction.

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


def abort_transaction_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    customers = db[CUSTOMER_COLLECTION]

    customer = customers.find_one()

    if customer is None:

        print("No customer found.")

        client.close()

        return

    customer_id = customer["_id"]

    original_points = customer.get("loyaltyPoints", 0)

    print("=" * 100)
    print("BEFORE TRANSACTION")
    print("=" * 100)

    print(f"Customer ID        : {customer_id}")
    print(f"Loyalty Points     : {original_points}")

    print()

    try:

        with client.start_session() as session:

            with session.start_transaction():

                result = customers.update_one(

                    {"_id": customer_id},

                    {
                        "$set": {
                            "loyaltyPoints": original_points + 500
                        }
                    },

                    session=session

                )

                print("=" * 100)
                print("UPDATE EXECUTED")
                print("=" * 100)

                print(f"Matched Documents  : {result.matched_count}")
                print(f"Modified Documents : {result.modified_count}")

                print()

                print("Simulating Server Failure...")

                raise Exception(
                    "Artificial Exception for Transaction Rollback"
                )

    except Exception as error:

        print()

        print("=" * 100)
        print("TRANSACTION ABORTED")
        print("=" * 100)

        print(error)

    updated_customer = customers.find_one(

        {
            "_id": customer_id
        }

    )

    print()

    print("=" * 100)
    print("AFTER TRANSACTION")
    print("=" * 100)

    print(f"Customer ID        : {customer_id}")

    print(
        f"Loyalty Points     : "
        f"{updated_customer.get('loyaltyPoints', 0)}"
    )

    if updated_customer.get("loyaltyPoints", 0) == original_points:

        print()

        print("Rollback Successful.")

    else:

        print()

        print("Rollback Failed.")

    client.close()


if __name__ == "__main__":

    abort_transaction_demo()