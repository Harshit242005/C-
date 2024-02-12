from mongo_connection import get_mongo_connection

class ConnectUser:
    def __init__(self, gmail, other_gmail):
        self.collection = get_mongo_connection("CodeUp", "Users")

        if self.both_exist(gmail, other_gmail):
            self.connect(gmail, other_gmail)
        else:
            return "User does not exist for connecting"

    def both_exist(self, gmail, other_gmail):
        find_gmail = self.collection.find({"Gmail": gmail})
        find_other_gmail = self.collection.find({"Gmail": other_gmail})
        if find_gmail.count() > 0 and find_other_gmail.count() > 0:
            return True
        return False

    def connect(self, gmail, other_gmail):
        # Check if users are already connected
        user_data = self.collection.find_one({"Gmail": gmail})
        other_user_data = self.collection.find_one({"Gmail": other_gmail})

        if other_gmail in user_data["Connects"] and gmail in other_user_data["Connects"]:
            return "Users are already connected"

        # Add other_gmail to the "Connects" list for gmail user
        self.collection.update_one(
            {"Gmail": gmail},
            {"$addToSet": {"Connects": other_gmail}}
        )

        # Add gmail to the "Connects" list for other_gmail user
        self.collection.update_one(
            {"Gmail": other_gmail},
            {"$addToSet": {"Connects": gmail}}
        )
        return "Users connected successfully"