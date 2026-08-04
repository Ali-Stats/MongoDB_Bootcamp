"""
File:
    01_sessions.py

Purpose:
    Demonstrate MongoDB Sessions.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI
)


def session_demo():

    client = MongoClient(MONGO_URI)

    print("=" * 100)
    print("STARTING SESSION")
    print("=" * 100)

    session = client.start_session()

    print()

    print("MongoDB Session Started Successfully.")

    print()

    print(f"Session Object : {session}")

    print()

    print("=" * 100)
    print("ENDING SESSION")
    print("=" * 100)

    session.end_session()

    print()

    print("Session Closed Successfully.")

    client.close()


if __name__ == "__main__":

    session_demo()