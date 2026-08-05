"""
File:
    06_find_one_and_delete.py

Purpose:
    Demonstrate MongoDB find_one_and_delete().

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

COLLECTION_NAME = "ticket_bookings"


def line():

    print("=" * 100)


def cancel_booking():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection = db[COLLECTION_NAME]

    collection.delete_many({})

    collection.insert_many(

        [

            {

                "bookingID": "BK001",

                "customer": "Rahul",

                "movie": "Avengers",

                "seat": "A10"

            },

            {

                "bookingID": "BK002",

                "customer": "Priya",

                "movie": "Batman",

                "seat": "B12"

            }

        ]

    )

    line()

    print("CURRENT BOOKINGS")

    line()

    print()

    for booking in collection.find({}, {"_id": 0}):

        print(booking)

    print("\nDEBUG: Loop Completed")

    booking_id = input(

        "\nEnter Booking ID to Cancel : "

    ).strip()

    deleted_booking = collection.find_one_and_delete(

        {

            "bookingID": booking_id

        }

    )

    print()

    line()

    print("RESULT")

    line()

    print()

    if deleted_booking:

        print("Cancelled Booking")

        print()

        print(deleted_booking)

    else:

        print("Booking Not Found")

    print()

    line()

    print("REMAINING BOOKINGS")

    line()

    print()

    for booking in collection.find({}, {"_id": 0}):

        print(booking)

    client.close()


if __name__ == "__main__":

    cancel_booking()