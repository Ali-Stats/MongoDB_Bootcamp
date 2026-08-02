"""
File:
    25_fill_densify.py

Purpose:
    Demonstrate MongoDB $densify and $fill
    using daily sales data.

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


def fill_densify_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    sales = db["sales_demo"]

    sales.delete_many({})

    sales.insert_many([

        {
            "date": datetime(2026,1,1),
            "sales":1000
        },

        {
            "date": datetime(2026,1,2),
            "sales":1200
        },

        {
            "date": datetime(2026,1,3),
            "sales":1400
        },

        {
            "date": datetime(2026,1,6),
            "sales":1800
        },

        {
            "date": datetime(2026,1,9),
            "sales":2000
        }

    ])

    pipeline=[

        {

            "$densify":{

                "field":"date",

                "range":{

                    "step":1,

                    "unit":"day",

                    "bounds":"full"

                }

            }

        },

        {

            "$fill":{

                "sortBy":{

                    "date":1

                },

                "output":{

                    "sales":{

                        "method":"locf"

                    }

                }

            }

        }

    ]

    results=sales.aggregate(pipeline)

    print("="*95)
    print("FILL & DENSIFY DEMONSTRATION")
    print("="*95)

    for row in results:

        print("-"*95)

        print(f"Date  : {row['date'].strftime('%d-%b-%Y')}")
        print(f"Sales : ₹{row['sales']:,.2f}")

    print("-"*95)

    client.close()


if __name__=="__main__":

    fill_densify_demo()