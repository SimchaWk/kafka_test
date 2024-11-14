from app.mongo_db.connection import get_all_messages_collection

all_messages_collection = get_all_messages_collection()


def save_raw_data(data_to_add):
    data = all_messages_collection.insert_one(data_to_add)
    return data.inserted_id
