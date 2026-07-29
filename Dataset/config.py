"""
File:
    config.py

Purpose:
    Stores application-wide configuration values.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

MONGO_URI = "mongodb://localhost:27017/"

DATABASE_NAME = "RetailAnalyticsDB"

CUSTOMER_COLLECTION = "customers"
RESTAURANT_COLLECTION = "restaurants"
MENU_COLLECTION = "menu"
ORDER_COLLECTION = "orders"

NUMBER_OF_CUSTOMERS = 5000
NUMBER_OF_RESTAURANTS = 50
NUMBER_OF_MENU_ITEMS = 300
NUMBER_OF_ORDERS = 10000