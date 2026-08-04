"""
File:
    02_start_transaction.py

Purpose:
    Demonstrate how to start a MongoDB transaction.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient
from pymongo.read_concern import ReadConcern
from pymongo.write_concern import WriteConcern
from pymongo.read_preferences import ReadPreference

from Dataset.config import (
    MONGO_URI
)


def start_transaction_demo():

    client = MongoClient(MONGO_URI)

    print("=" * 100)
    print("STARTING CLIENT SESSION")
    print("=" * 100)

    with client.start_session() as session:

        print("\nSession Created Successfully.")

        print("\nSession ID:")
        print(session.session_id)

        print()

        print("=" * 100)
        print("STARTING TRANSACTION")
        print("=" * 100)

        with session.start_transaction(

            read_concern=ReadConcern("majority"),

            write_concern=WriteConcern("majority"),

            read_preference=ReadPreference.PRIMARY

        ):

            print()

            print("Transaction Started Successfully.")

            print()

            print("Read Concern     : majority")

            print("Write Concern    : majority")

            print("Read Preference  : PRIMARY")

            print()

            print("No database operations executed yet.")

            print("Transaction will automatically COMMIT")

            print("when this block exits successfully.")

        print()

        print("=" * 100)
        print("TRANSACTION FINISHED")
        print("=" * 100)

    print()

    print("Session Closed Successfully.")

    client.close()


if __name__ == "__main__":

    start_transaction_demo()