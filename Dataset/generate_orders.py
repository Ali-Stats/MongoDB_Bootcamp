"""
File:
    generate_orders.py

Purpose:
    Generates realistic order data and inserts it
    into MongoDB.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from random import (
    choice,
    randint,
    sample,
    random,
    choices
)

from datetime import (
    datetime,
    timedelta
)

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME,
    CUSTOMER_COLLECTION,
    RESTAURANT_COLLECTION,
    MENU_COLLECTION,
    ORDER_COLLECTION,
    NUMBER_OF_ORDERS
)

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Wallet",
    "Cash"
]

PAYMENT_WEIGHTS = [
    50,
    20,
    15,
    10,
    5
]

ORDER_STATUS = [
    "Delivered",
    "Preparing",
    "Cancelled"
]

ORDER_STATUS_WEIGHTS = [
    80,
    15,
    5
]

def connect_database():
    """
    Connect to MongoDB and return the database object.
    """

    client = MongoClient(MONGO_URI)

    return client[DATABASE_NAME]

def load_customers(database):
    """
    Loads all customers.
    """

    return list(
        database[CUSTOMER_COLLECTION].find()
    )

def load_restaurants(database):
    """
    Loads all restaurants.
    """

    return list(
        database[RESTAURANT_COLLECTION].find()
    )

def load_menu(database):
    """
    Groups menu items by restaurant.
    """

    menu_collection = database[MENU_COLLECTION]

    menu = {}

    for item in menu_collection.find():

        restaurant_id = item["restaurantID"]

        if restaurant_id not in menu:

            menu[restaurant_id] = []

        menu[restaurant_id].append(item)

    return menu

def generate_random_date():
    """
    Generates a random order date
    within the last year.
    """

    today = datetime.today()

    random_days = randint(0, 365)

    return today - timedelta(days=random_days)

def calculate_totals(items):
    """
    Calculates subtotal, discount,
    delivery fee, tax and grand total.
    """

    subtotal = sum(
        item["totalPrice"]
        for item in items
    )

    if random() < 0.30:
        discount = randint(20, 150)
    else:
        discount = 0

    discount = min(discount, subtotal)

    delivery_fee = randint(20, 60)

    taxable_amount = subtotal - discount

    tax = round(taxable_amount * 0.05, 2)

    grand_total = round(
        taxable_amount +
        delivery_fee +
        tax,
        2
    )

    return (
        subtotal,
        discount,
        delivery_fee,
        tax,
        grand_total
    )


def generate_order(
        order_number,
        customers,
        restaurants,
        menu
):
    """
    Generates one order document.
    """

    customer = choice(customers)

    restaurant = choice(restaurants)

    restaurant_id = restaurant["restaurantID"]

    restaurant_menu = menu[restaurant_id]

    number_of_items = randint(1, min(4, len(restaurant_menu)))

    selected_items = sample(
        restaurant_menu,
        number_of_items
    )

    items = []

    for menu_item in selected_items:

        quantity = randint(1, 3)

        total_price = (
            menu_item["price"] *
            quantity
        )

        items.append({

            "menuID": menu_item["menuID"],

            "itemName": menu_item["itemName"],

            "quantity": quantity,

            "unitPrice": menu_item["price"],

            "totalPrice": total_price

        })

    (
        subtotal,
        discount,
        delivery_fee,
        tax,
        grand_total
    ) = calculate_totals(items)

    payment_method = choices(
        PAYMENT_METHODS,
        weights=PAYMENT_WEIGHTS,
        k=1
    )[0]

    order_status = choices(
        ORDER_STATUS,
        weights=ORDER_STATUS_WEIGHTS,
        k=1
    )[0]

    if order_status == "Delivered":

        delivery_time = randint(20, 60)

    else:

        delivery_time = None

    return {

        "orderID": f"O{order_number:06}",

        "customerID": customer["customerID"],

        "restaurantID": restaurant_id,

        "orderDate": generate_random_date(),

        "items": items,

        "subtotal": subtotal,

        "discount": discount,

        "deliveryFee": delivery_fee,

        "tax": tax,

        "grandTotal": grand_total,

        "paymentMethod": payment_method,

        "orderStatus": order_status,

        "deliveryTime": delivery_time

    }

def main():

    database = connect_database()

    customers = load_customers(database)

    restaurants = load_restaurants(database)

    menu = load_menu(database)

    orders = database[ORDER_COLLECTION]

    order_list = []

    for order_number in range(
            1,
            NUMBER_OF_ORDERS + 1
    ):

        order = generate_order(
            order_number,
            customers,
            restaurants,
            menu
        )

        order_list.append(order)

    orders.insert_many(order_list)

    print("=" * 50)
    print(f"{NUMBER_OF_ORDERS} Orders Inserted Successfully")
    print("=" * 50)


if __name__ == "__main__":
    main()