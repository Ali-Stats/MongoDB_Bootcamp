from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME,
    CUSTOMER_COLLECTION
)


def connect_database():

    client = MongoClient(MONGO_URI)

    return client[DATABASE_NAME]


def main():

    database = connect_database()

    customers = database[CUSTOMER_COLLECTION]

    result = customers.find(
        {"premiumMember": True},
        {
            "_id": 0,
            "name": 1,
            "age": 1,
            "city": 1
        }
    ).sort("age", -1).limit(10)

    print("=" * 60)
    print("TOP 10 OLDEST PREMIUM CUSTOMERS")
    print("=" * 60)

    for customer in result:

        print(
            f"{customer['name']:<25}"
            f" Age : {customer['age']:<3}"
            f" City : {customer['city']}"
        )


if __name__ == "__main__":
    main()