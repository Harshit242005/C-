from pymongo import MongoClient

client = MongoClient('mongodb+srv://agreharshit610:i4ZnXRbFARI4kaSl@taskhandler.u5cgjfw.mongodb.net/')
# Access a specific database, replace 'your_database_name' with your database name
db = client.CodeUp
collection = db.Users

class Create_User:
    def __init__(self, gmail, name, tech_list):
        # check if the gmail exists in the database or not
        find_document = collection.find({"Gmail": gmail})
        if find_document.count() > 0:
            return "User with this gmail already exists"
        else:
            collection.insert_one({"Gmail": gmail})
            self.add_details(gmail, name, tech_list)
            return "User is created!"

    def add_details(self, gmail, name, tech_list):
       
        user_data = {
            "Name": name,
            "TechList": tech_list,
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