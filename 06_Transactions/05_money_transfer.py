"""
File:
    05_money_transfer.py

Purpose:
    Demonstrate MongoDB Transactions using a Bank
    Money Transfer example.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from datetime import datetime

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME
)


ACCOUNT_COLLECTION = "bank_accounts"

TRANSACTION_COLLECTION = "bank_transactions"


def create_demo_accounts(accounts):

    if accounts.count_documents({}) == 0:

        accounts.insert_many(

            [

                {

                    "accountNumber": "ACC1001",

                    "holderName": "Alice",

                    "balance": 10000

                },

                {

                    "accountNumber": "ACC1002",

                    "holderName": "Bob",

                    "balance": 5000

                }

            ]

        )

        print("Demo Accounts Created.\n")


def money_transfer():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    accounts = db[ACCOUNT_COLLECTION]

    transactions = db[TRANSACTION_COLLECTION]

    create_demo_accounts(accounts)

    sender = accounts.find_one(

        {

            "accountNumber": "ACC1001"

        }

    )

    receiver = accounts.find_one(

        {

            "accountNumber": "ACC1002"

        }

    )

    amount = 2000

    print("=" * 100)
    print("BEFORE TRANSFER")
    print("=" * 100)

    print(
        f"{sender['holderName']} : ₹{sender['balance']}"
    )

    print(
        f"{receiver['holderName']} : ₹{receiver['balance']}"
    )

    print()

    try:

        with client.start_session() as session:

            with session.start_transaction():

                accounts.update_one(

                    {

                        "_id": sender["_id"]

                    },

                    {

                        "$inc": {

                            "balance": -amount

                        }

                    },

                    session=session

                )

                accounts.update_one(

                    {

                        "_id": receiver["_id"]

                    },

                    {

                        "$inc": {

                            "balance": amount

                        }

                    },

                    session=session

                )

                transactions.insert_one(

                    {

                        "from": sender["accountNumber"],

                        "to": receiver["accountNumber"],

                        "amount": amount,

                        "timestamp": datetime.now(),

                        "status": "SUCCESS"

                    },

                    session=session

                )

        print("Transaction Committed Successfully.\n")

    except Exception as error:

        print(error)

    sender = accounts.find_one(

        {

            "accountNumber": "ACC1001"

        }

    )

    receiver = accounts.find_one(

        {

            "accountNumber": "ACC1002"

        }

    )

    print("=" * 100)
    print("AFTER TRANSFER")
    print("=" * 100)

    print(
        f"{sender['holderName']} : ₹{sender['balance']}"
    )

    print(
        f"{receiver['holderName']} : ₹{receiver['balance']}"
    )

    print()

    print("=" * 100)
    print("TRANSACTION HISTORY")
    print("=" * 100)

    latest = transactions.find().sort("_id", -1).limit(1)

    for transaction in latest:

        print(transaction)

    client.close()


if __name__ == "__main__":

    money_transfer()