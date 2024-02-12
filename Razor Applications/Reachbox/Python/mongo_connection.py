from pymongo import MongoClient

def get_mongo_connection(database_name, collection_name):
    # Replace 'your_database_uri' with your MongoDB connection string
    client = MongoClient('mongodb+srv://agreharshit610:i4ZnXRbFARI4kaSl@taskhandler.u5cgjfw.mongodb.net/')
    # Access a specific database, replace 'your_database_name' with your database name
    db = client[database_name]
    collection = db[collection_name]
    return collection
