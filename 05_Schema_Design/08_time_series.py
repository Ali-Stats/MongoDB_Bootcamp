"""
File:
    08_time_series.py

Purpose:
    Demonstrate MongoDB Time Series Collections.

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


def time_series_demo():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    collection_name = "server_metrics"

    if collection_name in db.list_collection_names():

        db.drop_collection(collection_name)

    db.command({

        "create": collection_name,

        "timeseries": {

            "timeField": "timestamp",

            "metaField": "server"

        }

    })

    metrics = db[collection_name]

    print("=" * 100)
    print("TIME SERIES COLLECTION CREATED")
    print("=" * 100)

    metrics.insert_many([

        {

            "timestamp": datetime.utcnow(),

            "server": "Server-A",

            "cpu": 35,

            "memory": 62

        },

        {

            "timestamp": datetime.utcnow(),

            "server": "Server-A",

            "cpu": 38,

            "memory": 65

        },

        {

            "timestamp": datetime.utcnow(),

            "server": "Server-B",

            "cpu": 52,

            "memory": 71

        }

    ])

    print()

    print("Sample Metrics Inserted Successfully.")

    print()

    print("=" * 100)
    print("SERVER METRICS")
    print("=" * 100)

    for metric in metrics.find({}, {"_id": 0}):

        print("-" * 100)

        print(metric)

    print("-" * 100)

    client.close()


if __name__ == "__main__":

    time_series_demo()