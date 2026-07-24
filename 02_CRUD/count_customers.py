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

    premium_count = customers.count_documents(
        {
            "premiumMember": True
        }
    )

    print("=" * 50)
    print("PREMIUM CUSTOMERS")
    print("=" * 50)
    print(premium_count)
    print(type(premium_count))


if __name__ == "__main__":
    main()