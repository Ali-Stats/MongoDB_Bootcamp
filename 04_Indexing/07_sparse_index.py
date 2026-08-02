"""
File:
    07_sparse_index.py

Purpose:
    Demonstrate MongoDB Sparse Index.

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


def sparse_index_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    customers = db["customer_demo"]

    customers.drop()

    customers.insert_many([

        {
            "customerID":"C001",
            "name":"Syed",
            "passportNumber":"P12345"
        },

        {
            "customerID":"C002",
            "name":"John"
        },

        {
            "customerID":"C003",
            "name":"Ali"
        },

        {
            "customerID":"C004",
            "name":"Sara",
            "passportNumber":"P56789"
        }

    ])

    print("="*100)
    print("CREATING SPARSE INDEX")
    print("="*100)

    index_name = customers.create_index(

        [

            ("passportNumber",1)

        ],

        sparse=True

    )

    print(f"\nIndex Created : {index_name}")

    print()

    print("="*100)
    print("CUSTOMERS HAVING PASSPORT")
    print("="*100)

    results = customers.find(

        {

            "passportNumber":{

                "$exists":True

            }

        },

        {

            "_id":0

        }

    )

    for index, customer in enumerate(results, start=1):

        print("-"*100)

        print(f"Record            : {index}")
        print(f"Customer ID       : {customer['customerID']}")
        print(f"Name              : {customer['name']}")
        print(f"Passport Number   : {customer['passportNumber']}")

    print("-"*100)

    print()

    print("="*100)
    print("AVAILABLE INDEXES")
    print("="*100)

    for index in customers.list_indexes():

        print("-"*100)

        print(f"Index Name : {index['name']}")
        print(f"Key        : {index['key']}")

    print("-"*100)

    client.close()


if __name__=="__main__":

    sparse_index_demo()