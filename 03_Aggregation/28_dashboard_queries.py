"""
File:
    28_dashboard_queries.py

Purpose:
    Business Dashboard Queries using MongoDB
    Aggregation Framework.

Author:
    Syed Ali Ashraf

Course:
    MongoDB Bootcamp 2.0
"""

from pymongo import MongoClient

from Dataset.config import (
    MONGO_URI,
    DATABASE_NAME,
    ORDER_COLLECTION
)


client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]

orders = db[ORDER_COLLECTION]


# ============================================================
# Executive KPI Dashboard
# ============================================================

def executive_kpi():

    pipeline = [

        {
            "$group": {

                "_id": None,

                "totalOrders": {
                    "$sum": 1
                },

                "totalRevenue": {
                    "$sum": "$grandTotal"
                },

                "averageOrderValue": {
                    "$avg": "$grandTotal"
                }

            }

        }

    ]

    result = list(orders.aggregate(pipeline))[0]

    print("=" * 100)
    print("EXECUTIVE KPI DASHBOARD")
    print("=" * 100)

    print(f"Total Orders         : {result['totalOrders']}")
    print(f"Total Revenue        : ₹{result['totalRevenue']:,.2f}")
    print(f"Average Order Value  : ₹{result['averageOrderValue']:,.2f}")

    print()


# ============================================================
# Top 10 Restaurants by Revenue
# ============================================================

def top_restaurants():

    pipeline = [

        {

            "$group": {

                "_id": "$restaurantID",

                "totalRevenue": {

                    "$sum": "$grandTotal"

                },

                "totalOrders": {

                    "$sum": 1

                }

            }

        },

        {

            "$sort": {

                "totalRevenue": -1

            }

        },

        {

            "$limit": 10

        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 100)
    print("TOP 10 RESTAURANTS")
    print("=" * 100)

    for index, restaurant in enumerate(results, start=1):

        print("-" * 100)

        print(f"Rank             : {index}")
        print(f"Restaurant ID    : {restaurant['_id']}")
        print(f"Revenue          : ₹{restaurant['totalRevenue']:,.2f}")
        print(f"Orders           : {restaurant['totalOrders']}")

    print()


# ============================================================
# Top 10 Customers
# ============================================================

def top_customers():

    pipeline = [

        {

            "$group": {

                "_id": "$customerID",

                "totalSpent": {

                    "$sum": "$grandTotal"

                },

                "totalOrders": {

                    "$sum": 1

                }

            }

        },

        {

            "$sort": {

                "totalSpent": -1

            }

        },

        {

            "$limit": 10

        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 100)
    print("TOP 10 CUSTOMERS")
    print("=" * 100)

    for index, customer in enumerate(results, start=1):

        print("-" * 100)

        print(f"Rank             : {index}")
        print(f"Customer ID      : {customer['_id']}")
        print(f"Orders           : {customer['totalOrders']}")
        print(f"Total Spent      : ₹{customer['totalSpent']:,.2f}")

    print()

    # ============================================================
# Payment Method Distribution
# ============================================================

def payment_method_distribution():

    pipeline = [

        {

            "$sortByCount": "$paymentMethod"

        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 100)
    print("PAYMENT METHOD DISTRIBUTION")
    print("=" * 100)

    for index, payment in enumerate(results, start=1):

        print("-" * 100)

        print(f"Rank              : {index}")
        print(f"Payment Method    : {payment['_id']}")
        print(f"Total Orders      : {payment['count']}")

    print()


# ============================================================
# Order Status Distribution
# ============================================================

def order_status_distribution():

    pipeline = [

        {

            "$sortByCount": "$orderStatus"

        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 100)
    print("ORDER STATUS DISTRIBUTION")
    print("=" * 100)

    for index, status in enumerate(results, start=1):

        print("-" * 100)

        print(f"Rank              : {index}")
        print(f"Order Status      : {status['_id']}")
        print(f"Total Orders      : {status['count']}")

    print()


# ============================================================
# Monthly Revenue
# ============================================================

def monthly_revenue():

    pipeline = [

        {

            "$group": {

                "_id": {

                    "$month": "$orderDate"

                },

                "totalRevenue": {

                    "$sum": "$grandTotal"

                },

                "totalOrders": {

                    "$sum": 1

                }

            }

        },

        {

            "$sort": {

                "_id": 1

            }

        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 100)
    print("MONTHLY REVENUE")
    print("=" * 100)

    for month in results:

        print("-" * 100)

        print(f"Month            : {month['_id']}")
        print(f"Total Orders     : {month['totalOrders']}")
        print(f"Revenue          : ₹{month['totalRevenue']:,.2f}")

    print()


# ============================================================
# Premium Customer Revenue
# ============================================================

def premium_customer_revenue():

    pipeline = [

        {

            "$lookup": {

                "from": "customers",

                "localField": "customerID",

                "foreignField": "customerID",

                "as": "customer"

            }

        },

        {

            "$unwind": "$customer"

        },

        {

            "$match": {

                "customer.premiumMember": True

            }

        },

        {

            "$group": {

                "_id": None,

                "premiumCustomers": {

                    "$addToSet": "$customerID"

                },

                "totalRevenue": {

                    "$sum": "$grandTotal"

                },

                "totalOrders": {

                    "$sum": 1

                }

            }

        },

        {

            "$project": {

                "_id": 0,

                "premiumCustomerCount": {

                    "$size": "$premiumCustomers"

                },

                "totalRevenue": 1,

                "totalOrders": 1

            }

        }

    ]

    result = list(orders.aggregate(pipeline))[0]

    print("=" * 100)
    print("PREMIUM CUSTOMER ANALYTICS")
    print("=" * 100)

    print(f"Premium Customers : {result['premiumCustomerCount']}")
    print(f"Total Orders      : {result['totalOrders']}")
    print(f"Total Revenue     : ₹{result['totalRevenue']:,.2f}")

    print()

    # ============================================================
# Top Cuisine Analysis
# ============================================================

def top_cuisine():

    pipeline = [

        {

            "$lookup": {

                "from": "restaurants",

                "localField": "restaurantID",

                "foreignField": "restaurantID",

                "as": "restaurant"

            }

        },

        {

            "$unwind": "$restaurant"

        },

        {

            "$sortByCount": "$restaurant.cuisine"

        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 100)
    print("TOP CUISINES")
    print("=" * 100)

    for index, cuisine in enumerate(results, start=1):

        print("-" * 100)

        print(f"Rank           : {index}")
        print(f"Cuisine        : {cuisine['_id']}")
        print(f"Orders         : {cuisine['count']}")

    print()


# ============================================================
# Average Order Value by Restaurant
# ============================================================

def average_order_by_restaurant():

    pipeline = [

        {

            "$group": {

                "_id": "$restaurantID",

                "averageOrder": {

                    "$avg": "$grandTotal"

                },

                "totalOrders": {

                    "$sum": 1

                }

            }

        },

        {

            "$sort": {

                "averageOrder": -1

            }

        },

        {

            "$limit": 10

        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 100)
    print("AVERAGE ORDER VALUE BY RESTAURANT")
    print("=" * 100)

    for index, restaurant in enumerate(results, start=1):

        print("-" * 100)

        print(f"Rank             : {index}")
        print(f"Restaurant ID    : {restaurant['_id']}")
        print(f"Average Order    : ₹{restaurant['averageOrder']:,.2f}")
        print(f"Total Orders     : {restaurant['totalOrders']}")

    print()


# ============================================================
# Customer Lifetime Value (CLV)
# ============================================================

def customer_lifetime_value():

    pipeline = [

        {

            "$group": {

                "_id": "$customerID",

                "lifetimeValue": {

                    "$sum": "$grandTotal"

                },

                "totalOrders": {

                    "$sum": 1

                }

            }

        },

        {

            "$sort": {

                "lifetimeValue": -1

            }

        },

        {

            "$limit": 10

        }

    ]

    results = orders.aggregate(pipeline)

    print("=" * 100)
    print("CUSTOMER LIFETIME VALUE")
    print("=" * 100)

    for index, customer in enumerate(results, start=1):

        print("-" * 100)

        print(f"Rank               : {index}")
        print(f"Customer ID        : {customer['_id']}")
        print(f"Total Orders       : {customer['totalOrders']}")
        print(f"Lifetime Value     : ₹{customer['lifetimeValue']:,.2f}")

    print()


# ============================================================
# Main Function
# ============================================================

def main():

    executive_kpi()

    top_restaurants()

    top_customers()

    payment_method_distribution()

    order_status_distribution()

    monthly_revenue()

    premium_customer_revenue()

    top_cuisine()

    average_order_by_restaurant()

    customer_lifetime_value()

    client.close()


if __name__ == "__main__":

    main()