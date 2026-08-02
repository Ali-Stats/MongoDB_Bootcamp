"""
File:
    05_ttl_index.py

Purpose:
    Demonstrate MongoDB TTL Index.

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


def ttl_index_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    sessions = db["session_demo"]

    sessions.drop()

    print("=" * 100)
    print("CREATING TTL INDEX")
    print("=" * 100)

    index_name = sessions.create_index(

        [("createdAt", 1)],

        expireAfterSeconds=60

    )

    print(f"\nIndex Created : {index_name}")

    print()

    session = {

        "sessionID": "SESSION001",

        "user": "Syed",

        "createdAt": datetime.utcnow()

    }

    sessions.insert_one(session)

    print("=" * 100)
    print("SESSION INSERTED")
    print("=" * 100)

    print(f"Session ID : {session['sessionID']}")
    print(f"User       : {session['user']}")
    print(f"Created At : {session['createdAt']}")

    print()

    print("=" * 100)
    print("VERIFY IN MONGODB COMPASS")
    print("=" * 100)

    print("Collection : session_demo")

    print()

    print("Wait approximately 60-90 seconds.")

    print("Refresh the collection.")

    print("The document should disappear automatically.")

    print("=" * 100)

    client.close()


if __name__ == "__main__":

    ttl_index_demo()