"""
File:
    07_food_delivery_transaction.py

Purpose:
    Demonstrate a real-world Food Delivery Transaction
    using MongoDB Transactions across multiple collections.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from datetime import datetime
import uuid

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME
)

# ==========================================================
# COLLECTIONS
# ==========================================================

CUSTOMER_COLLECTION = "customers"
RESTAURANT_COLLECTION = "restaurants"
MENU_COLLECTION = "menu"
ORDER_COLLECTION = "orders"
PAYMENT_COLLECTION = "payments"


# ==========================================================
# UTILITIES
# ==========================================================

def line():

    print("=" * 100)


def create_payment_id():

    return "PAY" + uuid.uuid4().hex[:8].upper()


def create_order_id():

    return "ORD" + uuid.uuid4().hex[:8].upper()


# ==========================================================
# DISPLAY FUNCTIONS
# ==========================================================

def show_customers(customers):

    line()
    print("AVAILABLE CUSTOMERS")
    line()

    cursor = customers.find(
        {},
        {
            "_id": 0,
            "customerID": 1,
            "name": 1,
            "loyaltyPoints": 1
        }
    ).limit(10)

    for customer in cursor:

        print(
            f"{customer['customerID']} "
            f"| {customer['name']} "
            f"| Loyalty : {customer.get('loyaltyPoints',0)}"
        )


def show_restaurants(restaurants):

    line()
    print("AVAILABLE RESTAURANTS")
    line()

    cursor = restaurants.find(
        {"active": True},
        {
            "_id": 0,
            "restaurantID": 1,
            "restaurantName": 1,
            "city": 1
        }
    ).limit(10)

    for restaurant in cursor:

        print(
            f"{restaurant['restaurantID']} "
            f"| {restaurant['restaurantName']} "
            f"| {restaurant['city']}"
        )


def show_menu(menu, restaurant_id):

    line()
    print("MENU")
    line()

    cursor = menu.find(

        {
            "restaurantID": restaurant_id,
            "available": True
        },

        {
            "_id": 0,
            "menuID": 1,
            "itemName": 1,
            "price": 1
        }

    )

    found = False

    for item in cursor:

        found = True

        print(
            f"{item['menuID']} | "
            f"{item['itemName']} | "
            f"₹{item['price']}"
        )

    if not found:

        print("No Menu Items Found.")


# ==========================================================
# VALIDATIONS
# ==========================================================

def validate_customer(customers, customer_id):

    customer = customers.find_one(

        {
            "customerID": customer_id
        }

    )

    if customer is None:

        raise Exception("Customer Not Found.")

    return customer


def validate_restaurant(restaurants, restaurant_id):

    restaurant = restaurants.find_one(

        {
            "restaurantID": restaurant_id,
            "active": True
        }

    )

    if restaurant is None:

        raise Exception("Restaurant Not Found or Closed.")

    return restaurant


def validate_menu(menu, restaurant_id, menu_id):

    item = menu.find_one(

        {
            "restaurantID": restaurant_id,
            "menuID": menu_id,
            "available": True
        }

    )

    if item is None:

        raise Exception("Menu Item Not Available.")

    return item


def calculate_bill(price, quantity):

    subtotal = price * quantity

    tax = subtotal * 0.05

    delivery_fee = 40

    grand_total = subtotal + tax + delivery_fee

    return {

        "subtotal": subtotal,

        "tax": round(tax, 2),

        "deliveryFee": delivery_fee,

        "grandTotal": round(grand_total, 2)

    }


# ==========================================================
# MAIN
# ==========================================================

def food_delivery_transaction():

    client = MongoClient(MONGO_URI)

    db = client[DATABASE_NAME]

    customers = db[CUSTOMER_COLLECTION]

    restaurants = db[RESTAURANT_COLLECTION]

    menu = db[MENU_COLLECTION]

    orders = db[ORDER_COLLECTION]

    payments = db[PAYMENT_COLLECTION]

    line()
    print("FOOD DELIVERY TRANSACTION SYSTEM")
    line()

    show_customers(customers)

    customer_id = input(
        "\nEnter Customer ID : "
    ).strip()

    print()

    show_restaurants(restaurants)

    restaurant_id = input(
        "\nEnter Restaurant ID : "
    ).strip()

    print()

    show_menu(menu, restaurant_id)

    menu_id = input(
        "\nEnter Menu ID : "
    ).strip()

    quantity = int(

        input(

            "Quantity : "

        )

    )

    payment_method = input(

        "Payment Method (UPI/CARD/CASH): "

    ).upper()

    print()

    line()

    print("VALIDATING...")

    line()

    customer = validate_customer(

        customers,

        customer_id

    )

    print("✓ Customer Found")

    restaurant = validate_restaurant(

        restaurants,

        restaurant_id

    )

    print("✓ Restaurant Found")

    menu_item = validate_menu(

        menu,

        restaurant_id,

        menu_id

    )

    print("✓ Menu Available")

    bill = calculate_bill(

        menu_item["price"],

        quantity

    )

    print("✓ Bill Calculated")


    try:

        payment_id = create_payment_id()

        order_id = create_order_id()

        with client.start_session() as session:

            with session.start_transaction():

                # ==========================================
                # 1. CREATE PAYMENT
                # ==========================================

                payments.insert_one(

                    {

                        "paymentID": payment_id,

                        "orderID": order_id,

                        "customerID": customer_id,

                        "amount": bill["grandTotal"],

                        "paymentMethod": payment_method,

                        "status": "SUCCESS",

                        "createdAt": datetime.now()

                    },

                    session=session

                )

                print("✓ Payment Created")

                # ==========================================
                # 2. CREATE ORDER
                # ==========================================

                orders.insert_one(

                    {

                        "orderID": order_id,

                        "customerID": customer_id,

                        "restaurantID": restaurant_id,

                        "orderDate": datetime.now(),

                        "items": [

                            {

                                "menuID": menu_item["menuID"],

                                "itemName": menu_item["itemName"],

                                "price": menu_item["price"],

                                "quantity": quantity

                            }

                        ],

                        "subtotal": bill["subtotal"],

                        "discount": 0,

                        "deliveryFee": bill["deliveryFee"],

                        "tax": bill["tax"],

                        "grandTotal": bill["grandTotal"],

                        "paymentMethod": payment_method,

                        "orderStatus": "Preparing",

                        "deliveryTime": None

                    },

                    session=session

                )

                print("✓ Order Created")

                # ==========================================
                # 3. UPDATE CUSTOMER LOYALTY
                # ==========================================

                earned_points = int(

                    bill["grandTotal"] // 100

                )

                customers.update_one(

                    {

                        "customerID": customer_id

                    },

                    {

                        "$inc": {

                            "loyaltyPoints": earned_points

                        }

                    },

                    session=session

                )

                print("✓ Loyalty Points Updated")

                print("✓ Transaction Committed")

    except Exception as error:

        line()

        print("TRANSACTION FAILED")

        line()

        print(error)

        client.close()

        return

    # ==========================================
    # RECEIPT
    # ==========================================

    updated_customer = customers.find_one(

        {

            "customerID": customer_id

        }

    )

    print()

    line()

    print("ORDER RECEIPT")

    line()

    print(f"Order ID          : {order_id}")

    print(f"Payment ID        : {payment_id}")

    print(f"Customer          : {updated_customer['name']}")

    print(f"Restaurant        : {restaurant['restaurantName']}")

    print(f"Item              : {menu_item['itemName']}")

    print(f"Quantity          : {quantity}")

    print(f"Subtotal          : ₹{bill['subtotal']:.2f}")

    print(f"Delivery Fee      : ₹{bill['deliveryFee']:.2f}")

    print(f"Tax               : ₹{bill['tax']:.2f}")

    print(f"Grand Total       : ₹{bill['grandTotal']:.2f}")

    print(f"Payment Method    : {payment_method}")

    print(f"Loyalty Earned    : {earned_points}")

    print(
        f"Total Loyalty     : "
        f"{updated_customer.get('loyaltyPoints', 0)}"
    )

    print()

    line()

    print("ORDER PLACED SUCCESSFULLY")

    line()

    client.close()


if __name__ == "__main__":

    food_delivery_transaction()