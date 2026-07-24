from pymongo import MongoClient
import pymongo

print("=" * 50)
print("MongoDB Bootcamp - Environment Check")
print("=" * 50)

print(f"PyMongo Version: {pymongo.version}")

client = MongoClient("mongodb://localhost:27017/")

print("\nConnected successfully!")

print("\nDatabases:")

for db_name in client.list_database_names():
    print("-", db_name)