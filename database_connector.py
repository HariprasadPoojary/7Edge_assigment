from pymongo import MongoClient

DB_CLIENT = MongoClient("mongodb://localhost:27017")
DATABASE_NAME = "7Edge"
COLLECTION_ORDER = "orders"
COLLECTION_USER = "users"


def save_order_to_db(order_data: dict):
    payload = {
        "order_id": order_data["order_id"],
        "amount": order_data["total_amount"],
    }
    collection = DB_CLIENT[DATABASE_NAME][COLLECTION_ORDER]
    return collection.insert_one(payload)


def update_order_in_db(order_data: dict):
    collection = DB_CLIENT[DATABASE_NAME][COLLECTION_ORDER]
    payload = {"order_status": order_data["status"]}
    order_id = order_data["order_id"]

    return collection.update_one(
        {"order_id": order_id},
        {"$set": payload},
    )


def save_user_to_db(user_data: dict):
    collection = DB_CLIENT[DATABASE_NAME][COLLECTION_USER]
    return collection.insert_one(user_data)
