"""
File:
    11_geospatial_index.py

Purpose:
    Demonstrate MongoDB Geospatial Index (2dsphere).

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


def geospatial_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    restaurants = db["restaurant_location_demo"]

    restaurants.drop()

    restaurants.insert_many([

        {

            "restaurant":"Delhi Spice",

            "location":{

                "type":"Point",

                "coordinates":[77.2090,28.6139]

            }

        },

        {

            "restaurant":"Tandoori Hub",

            "location":{

                "type":"Point",

                "coordinates":[77.2200,28.6200]

            }

        },

        {

            "restaurant":"Burger World",

            "location":{

                "type":"Point",

                "coordinates":[77.1800,28.5900]

            }

        }

    ])

    print("="*100)
    print("CREATING 2DSPHERE INDEX")
    print("="*100)

    index_name = restaurants.create_index(

        [

            ("location","2dsphere")

        ]

    )

    print(f"\nIndex Created : {index_name}")

    print()

    print("="*100)
    print("NEAREST RESTAURANTS (WITHIN 5 KM)")
    print("="*100)

    results = restaurants.find(

        {

            "location":{

                "$near":{

                    "$geometry":{

                        "type":"Point",

                        "coordinates":[77.2090,28.6139]

                    },

                    "$maxDistance":5000

                }

            }

        }

    )

    for index, restaurant in enumerate(results,start=1):

        print("-"*100)

        print(f"Rank         : {index}")
        print(f"Restaurant   : {restaurant['restaurant']}")

    print("-"*100)

    client.close()


if __name__=="__main__":

    geospatial_demo()