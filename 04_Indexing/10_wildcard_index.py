"""
File:
    10_wildcard_index.py

Purpose:
    Demonstrate MongoDB Wildcard Index.

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


def wildcard_index_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    products = db["product_demo"]

    products.drop()

    products.insert_many([

        {

            "name":"Laptop",

            "brand":"Dell",

            "ram":"16GB"

        },

        {

            "name":"Phone",

            "brand":"Samsung",

            "camera":"108MP"

        },

        {

            "name":"TV",

            "brand":"Sony",

            "screen":"55 Inch",

            "speaker":"Dolby"

        }

    ])

    print("=" * 100)
    print("CREATING WILDCARD INDEX")
    print("=" * 100)

    index_name = products.create_index(

        [

            ("$**", 1)

        ]

    )

    print(f"\nIndex Created : {index_name}")

    print()

    print("=" * 100)
    print("SEARCHING PRODUCTS")
    print("=" * 100)

    results = products.find(

        {

            "brand":"Sony"

        }

    )

    for index, product in enumerate(results, start=1):

        print("-" * 100)

        print(f"Record     : {index}")
        print(f"Name       : {product['name']}")
        print(f"Brand      : {product['brand']}")

        if "screen" in product:
            print(f"Screen     : {product['screen']}")

        if "speaker" in product:
            print(f"Speaker    : {product['speaker']}")

    print("-" * 100)

    print()

    print("=" * 100)
    print("AVAILABLE INDEXES")
    print("=" * 100)

    for index in products.list_indexes():

        print("-" * 100)

        print(f"Index Name : {index['name']}")
        print(f"Key        : {index['key']}")

    print("-" * 100)

    client.close()


if __name__=="__main__":

    wildcard_index_demo()