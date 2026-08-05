"""
File:
    08_transaction_retry.py

Purpose:
    Demonstrate MongoDB Transaction Retry Logic.

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

MAX_RETRIES = 3


def retry_transaction():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    customers = db[CUSTOMER_COLLECTION]

    retries = 0

    while retries < MAX_RETRIES:

        try:

            print("=" * 100)

            print(
                f"Attempt {retries + 1}"
            )

            print("=" * 100)

            with client.start_session() as session:

                with session.start_transaction():

                    customer = customers.find_one()

                    if customer is None:

                        raise Exception(
                            "No Customer Found."
                        )

                    customers.update_one(

                        {

                            "_id": customer["_id"]

                        },

                        {

                            "$inc":

                            {

                                "loyaltyPoints": 5

                            }

                        },

                        session=session

                    )

                    print(
                        "Loyalty Updated."
                    )

                    #
                    # Simulate temporary error
                    #

                    if retries < 2:

                        raise Exception(
                            "TransientTransactionError"
                        )

                    print(
                        "Transaction Committed Successfully."
                    )

                    break

        except Exception as error:

            print()

            print(error)

            retries += 1

            if retries >= MAX_RETRIES:

                print()

                print(
                    "Maximum Retry Limit Reached."
                )

            else:

                print()

                print(
                    "Retrying Transaction..."
                )

    client.close()


if __name__ == "__main__":

    retry_transaction()