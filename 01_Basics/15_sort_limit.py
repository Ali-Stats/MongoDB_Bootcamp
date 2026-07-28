"""
File:
    15_sort_limit.py

Purpose:
    Sort and limit MongoDB query results.

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



def get_customers():


    client = MongoClient(MONGO_URI)


    database = client[DATABASE_NAME]


    customers = database["customers"]


    result = customers.find(
        {}
    ).sort(
        "age",
        -1
    ).limit(
        3
    )


    return result




def main():


    customers = get_customers()


    print("=" * 60)
    print("SORT AND LIMIT")
    print("=" * 60)


    for customer in customers:

        print(customer)



if __name__ == "__main__":
    main()