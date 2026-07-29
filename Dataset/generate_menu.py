"""
File:
    generate_menu.py

Purpose:
    Generates realistic menu data for restaurants
    and inserts it into MongoDB.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from random import choice, randint

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME,
    RESTAURANT_COLLECTION,
    MENU_COLLECTION
)


MENU_ITEMS = {
    "North Indian": [
        ("Paneer Butter Masala", True),
        ("Butter Chicken", False),
        ("Dal Makhani", True),
        ("Chicken Curry", False),
        ("Naan", True),
        ("Jeera Rice", True)
    ],

    "South Indian": [
        ("Masala Dosa", True),
        ("Plain Dosa", True),
        ("Idli", True),
        ("Vada", True),
        ("Sambar Rice", True),
        ("Chicken Chettinad", False)
    ],

    "Chinese": [
        ("Veg Fried Rice", True),
        ("Chicken Fried Rice", False),
        ("Veg Noodles", True),
        ("Chicken Noodles", False),
        ("Manchurian", True),
        ("Chilli Chicken", False)
    ],

    "Italian": [
        ("Margherita Pizza", True),
        ("Farmhouse Pizza", True),
        ("Pepperoni Pizza", False),
        ("White Sauce Pasta", True),
        ("Chicken Pasta", False),
        ("Garlic Bread", True)
    ],

    "Fast Food": [
        ("Veg Burger", True),
        ("Chicken Burger", False),
        ("French Fries", True),
        ("Cheese Fries", True),
        ("Hot Dog", False),
        ("Cold Drink", True)
    ],

    "Biryani": [
        ("Veg Biryani", True),
        ("Chicken Biryani", False),
        ("Mutton Biryani", False),
        ("Egg Biryani", False),
        ("Raita", True),
        ("Gulab Jamun", True)
    ],

    "Cafe": [
        ("Cold Coffee", True),
        ("Cappuccino", True),
        ("Latte", True),
        ("Brownie", True),
        ("Sandwich", True),
        ("Club Sandwich", False)
    ],

    "Bakery": [
        ("Chocolate Cake", True),
        ("Black Forest Cake", True),
        ("Croissant", True),
        ("Muffin", True),
        ("Garlic Puff", True),
        ("Chicken Puff", False)
    ],

    "Mughlai": [
        ("Chicken Korma", False),
        ("Mutton Rogan Josh", False),
        ("Seekh Kebab", False),
        ("Roomali Roti", True),
        ("Paneer Korma", True),
        ("Firni", True)
    ],

    "Street Food": [
        ("Pani Puri", True),
        ("Pav Bhaji", True),
        ("Vada Pav", True),
        ("Samosa", True),
        ("Kachori", True),
        ("Chicken Roll", False)
    ]
}


CATEGORY_MAP = {
    "Pizza": "Main Course",
    "Burger": "Main Course",
    "Pasta": "Main Course",
    "Rice": "Main Course",
    "Biryani": "Main Course",
    "Dosa": "Main Course",
    "Idli": "Main Course",
    "Noodles": "Main Course",
    "Cake": "Dessert",
    "Brownie": "Dessert",
    "Jamun": "Dessert",
    "Firni": "Dessert",
    "Coffee": "Beverage",
    "Latte": "Beverage",
    "Cappuccino": "Beverage",
    "Drink": "Beverage"
}


def connect_database():
    """
    Connect to MongoDB and return database object.
    """

    client = MongoClient(MONGO_URI)

    return client[DATABASE_NAME]


def get_category(item_name):
    """
    Determines category from item name.
    """

    for keyword, category in CATEGORY_MAP.items():

        if keyword.lower() in item_name.lower():

            return category

    return "Main Course"


def main():

    database = connect_database()

    restaurants = list(
        database[RESTAURANT_COLLECTION].find()
    )

    menu_collection = database[MENU_COLLECTION]

    menu_documents = []

    menu_number = 1

    for restaurant in restaurants:

        cuisine = restaurant["cuisine"]

        menu_items = MENU_ITEMS[cuisine].copy()

        number_of_items = randint(5, len(menu_items))

        selected_items = menu_items[:]

        while len(selected_items) > number_of_items:

            selected_items.pop(randint(0, len(selected_items)-1))

        for item_name, is_veg in selected_items:

            menu_documents.append({

                "menuID": f"M{menu_number:06}",

                "restaurantID": restaurant["restaurantID"],

                "itemName": item_name,

                "category": get_category(item_name),

                "price": randint(99, 599),

                "isVeg": is_veg,

                "available": choice([True, True, True, False])

            })

            menu_number += 1

    menu_collection.insert_many(menu_documents)

    print("=" * 50)
    print(f"{len(menu_documents)} Menu Items Inserted Successfully")
    print("=" * 50)


if __name__ == "__main__":
    main()