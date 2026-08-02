"""
File:
    23_graphLookup.py

Purpose:
    Demonstrate MongoDB $graphLookup using
    an employee hierarchy.

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


def graph_lookup_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    employees = db["employee_demo"]

    employees.delete_many({})

    employees.insert_many([

        {
            "employeeID":1,
            "name":"CEO",
            "managerID":None
        },

        {
            "employeeID":2,
            "name":"VP Engineering",
            "managerID":1
        },

        {
            "employeeID":3,
            "name":"Manager A",
            "managerID":2
        },

        {
            "employeeID":4,
            "name":"Developer 1",
            "managerID":3
        },

        {
            "employeeID":5,
            "name":"Developer 2",
            "managerID":3
        }

    ])

    pipeline=[

        {

            "$match":{

                "employeeID":2

            }

        },

        {

            "$graphLookup":{

                "from":"employee_demo",

                "startWith":"$employeeID",

                "connectFromField":"employeeID",

                "connectToField":"managerID",

                "as":"subordinates"

            }

        }

    ]

    result=list(employees.aggregate(pipeline))[0]

    print("="*100)
    print("GRAPH LOOKUP DEMONSTRATION")
    print("="*100)

    print(f"Manager : {result['name']}")

    print()

    print("Subordinates")

    print("-"*100)

    for index, employee in enumerate(result["subordinates"],start=1):

        print(f"{index}. {employee['name']}")

    print("-"*100)

    client.close()


if __name__=="__main__":

    graph_lookup_demo()