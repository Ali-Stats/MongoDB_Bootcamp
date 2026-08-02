"""
File:
    04_text_index.py

Purpose:
    Demonstrate MongoDB Text Index.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient

from Dataset.config import (

    MONGO_URI,

    DATABASE_NAME,

    MENU_COLLECTION

)


def text_index_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    menu = db[MENU_COLLECTION]

    print("=" * 100)
    print("SAMPLE MENU ITEMS")
    print("=" * 100)

    sample = menu.find(

        {},

        {

            "_id": 0,

            "menuID": 1,

            "itemName": 1,

            "description": 1

        }

    ).limit(5)

    for doc in sample:

        print(doc)

    print()

    print("=" * 100)
    print("CREATING TEXT INDEX")
    print("=" * 100)

    index_name = menu.create_index(

        [

            ("itemName", "text"),

            ("description", "text")

        ]

    )

    print(f"\nIndex Created : {index_name}")

    print()

    keyword = input("Enter a keyword to search : ")

    print()

    pipeline = [

        {

            "$match": {

                "$text": {

                    "$search": keyword

                }

            }

        },

        {

            "$project": {

                "_id": 0,

                "menuID": 1,

                "itemName": 1,

                "description": 1,

                "score": {

                    "$meta": "textScore"

                }

            }

        },

        {

            "$sort": {

                "score": {

                    "$meta": "textScore"

                }

            }

        },

        {

            "$limit": 10

        }

    ]

    results = menu.aggregate(pipeline)

    print("=" * 100)
    print("SEARCH RESULTS")
    print("=" * 100)

    found = False

    for index, item in enumerate(results, start=1):

        found = True

        print("-" * 100)

        print(f"Rank         : {index}")
        print(f"Menu ID      : {item['menuID']}")
        print(f"Item Name    : {item['itemName']}")
        print(f"Description  : {item['description']}")
        print(f"Score        : {item['score']:.4f}")

    if not found:

        print("No matching documents found.")

    print("-" * 100)

    client.close()


if __name__ == "__main__":

    text_index_demo()