"""
File:
    06_production_money_transfer.py

Purpose:
    Production Grade MongoDB Money Transfer
    using Transactions.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from datetime import datetime
import uuid

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME
)

ACCOUNT_COLLECTION = "bank_accounts"
TRANSACTION_COLLECTION = "bank_transactions"


def print_separator():

    print("=" * 100)


def create_demo_accounts(accounts):

    if accounts.count_documents({}) == 0:

        accounts.insert_many([

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

        ])

        print("Demo Accounts Created.\n")


def validate_accounts(sender, receiver):

    if sender is None:

        raise Exception("Sender account does not exist.")

    if receiver is None:

        raise Exception("Receiver account does not exist.")

    if sender["accountNumber"] == receiver["accountNumber"]:

        raise Exception("Sender and Receiver cannot be same.")


def validate_amount(amount):

    if amount <= 0:

        raise Exception("Transfer amount must be greater than zero.")


def validate_balance(sender, amount):

    if sender["balance"] <= amount:

        raise Exception("Insufficient Account Balance.")


def generate_reference():

    return f"BANK-{uuid.uuid4().hex[:10].upper()}"


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

    amount = 25000

    reference = generate_reference()

    print_separator()
    print("BEFORE TRANSFER")
    print_separator()

    print(f"Sender   : {sender['holderName']}")
    print(f"Balance  : ₹{sender['balance']:,}")

    print()

    print(f"Receiver : {receiver['holderName']}")
    print(f"Balance  : ₹{receiver['balance']:,}")

    print()

    try:

        validate_accounts(sender, receiver)

        validate_amount(amount)

        validate_balance(sender, amount)

        with client.start_session() as session:

            with session.start_transaction():

                accounts.update_one(

                    {
                        "_id": sender["_id"]
                    },

                    {
                        "$inc":
                        {
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
                        "$inc":
                        {
                            "balance": amount
                        }
                    },

                    session=session

                )

                transactions.insert_one(

                    {

                        "referenceNumber": reference,

                        "fromAccount": sender["accountNumber"],

                        "toAccount": receiver["accountNumber"],

                        "amount": amount,

                        "status": "SUCCESS",

                        "timestamp": datetime.now()

                    },

                    session=session

                )

        print_separator()
        print("TRANSFER SUCCESSFUL")
        print_separator()

        print(f"Reference Number : {reference}")
        print(f"Amount           : ₹{amount:,}")

    except Exception as error:

        print_separator()
        print("TRANSFER FAILED")
        print_separator()

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

    print()

    print_separator()
    print("UPDATED ACCOUNT BALANCES")
    print_separator()

    print(f"{sender['holderName']} : ₹{sender['balance']:,}")
    print(f"{receiver['holderName']} : ₹{receiver['balance']:,}")

    print()

    print_separator()
    print("LATEST TRANSACTION")
    print_separator()

    latest = transactions.find().sort("_id", -1).limit(1)

    for transaction in latest:

        print(transaction)

    client.close()


if __name__ == "__main__":

    money_transfer()