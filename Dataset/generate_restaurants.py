"""
File:
    generate_restaurants.py

Purpose:
    Generates realistic restaurant data and inserts it
    into MongoDB.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from random import choice, randint, uniform

from faker import Faker
from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME,
    RESTAURANT_COLLECTION,
    NUMBER_OF_RESTAURANTS
)

fake = Faker("en_IN")


RESTAURANT_NAMES = [
    "Spice Garden",
    "Biryani House",
    "Pizza Point",
    "Burger Hub",
    "Chinese Wok",
    "South Spice",
    "Punjabi Dhaba",
    "The Curry Bowl",
    "Urban Kitchen",
    "Food Junction",
    "Grill Nation",
    "Taste of India",
    "Cafe Delight",
    "The Hungry Spoon",
    "Mughlai Express",
    "Saffron Kitchen",
    "BBQ Palace",
    "Fresh Bites",
    "City Diner",
    "Royal Tandoor"
]


CUISINES = [
    "North Indian",
    "South Indian",
    "Chinese",
    "Italian",
    "Fast Food",
    "Biryani",
    "Cafe",
    "Bakery",
    "Mughlai",
    "Street Food"
]


def connect_database():
    """
    Connect to MongoDB and return the database object.
    """

    client = MongoClient(MONGO_URI)

    return client[DATABASE_NAME]


def generate_restaurant(restaurant_number):
    """
    Generates one restaurant document.
    """

    return {
        "restaurantID": f"R{restaurant_number:05}",
        "restaurantName": choice(RESTAURANT_NAMES),
        "city": fake.city(),
        "state": fake.state(),
        "cuisine": choice(CUISINES),
        "rating": round(uniform(3.5, 5.0), 1),
        "deliveryTime": randint(20, 60),
        "isPureVeg": choice([True, False]),
        "openingTime": "09:00",
        "closingTime": "23:00",
        "active": choice([True, True, True, True, False])
    }


def main():

    database = connect_database()

    restaurants = database[RESTAURANT_COLLECTION]

    restaurant_list = []

    for number in range(1, NUMBER_OF_RESTAURANTS + 1):

        restaurant_list.append(
            generate_restaurant(number)
        )

    restaurants.insert_many(restaurant_list)

    print("=" * 50)
    print(f"{NUMBER_OF_RESTAURANTS} Restaurants Inserted Successfully")
    print("=" * 50)


if __name__ == "__main__":
    main()