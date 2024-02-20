from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
# Access a specific database, replace 'your_database_name' with your database name
db = client.CodeUp
collection = db.Users

class Create_User:
    def __init__(self, gmail, name, tech_list):
        self.user_created = None  # Initialize the instance variable
        # check if the gmail exists in the database or not
        find_document = collection.count_documents({"Gmail": gmail})
        if find_document > 0:
            self.user_created = False
        else:
            collection.insert_one({"Gmail": gmail})
            self.add_details(gmail, name, tech_list)
            self.user_created = True

    def add_details(self, gmail, name, tech_list):
       
        user_data = {
            "Name": name,
            "TechList": tech_list,
            "Total_post_created": 0,
            "Connects": [],
            "Posts": []
        }
        self.update_details(gmail, user_data)

    def update_details(self, gmail, user_data):
        # Update the user's details in the collection
        result = collection.update_one({'Gmail': gmail}, {'$set': user_data})
        if result.modified_count > 0:
            print(f"User details updated successfully for {gmail}")
        else:
            print(f"No user found with the email {gmail}")