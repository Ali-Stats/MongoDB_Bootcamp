"""
File:
    generate_customers.py

Purpose:
    Generates realistic customer data and inserts it
    into MongoDB.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from random import randint, choice

from faker import Faker
from pymongo import MongoClient

from config import (
    MONGO_URI,
    DATABASE_NAME,
    CUSTOMER_COLLECTION,
    NUMBER_OF_CUSTOMERS
)


fake = Faker("en_IN")


def connect_database():
    """
    Connect to MongoDB and return the database object.
    """

    client = MongoClient(MONGO_URI)

    return client[DATABASE_NAME]


def generate_customer(customer_number):
    """
    Generates one customer document.
    """

    return {
        "customerID": f"C{customer_number:05}",
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "age": randint(18, 70),
        "gender": choice(["Male", "Female"]),
        "city": fake.city(),
        "state": fake.state(),
        "premiumMember": choice([True, False]),
        "joinDate": str(fake.date_between("-5y", "today"))
    }


def main():

    database = connect_database()

    customers = database[CUSTOMER_COLLECTION]

    customer_list = []

    for number in range(1, NUMBER_OF_CUSTOMERS + 1):

        customer_list.append(
            generate_customer(number)
        )

    customers.insert_many(customer_list)

    print("=" * 50)
    print(f"{NUMBER_OF_CUSTOMERS} Customers Inserted Successfully")
    print("=" * 50)


if __name__ == "__main__":
    main()