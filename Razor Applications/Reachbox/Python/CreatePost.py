# class for creating post 
import datetime
from mongo_connection import get_mongo_connection
class Create_post:
    def __init__(self, gmail, post_data):
        self.is_create_post = None
        self.collection = get_mongo_connection('CodeUp', 'Users')
        # check if the gmail exist as the user post or not
        if self.user_exist(gmail):
            
            if self.create_post(gmail, post_data):
                self.is_create_post = True
            else:
                self.is_create_post = False
        else:
            self.is_create_post = False


    def user_exist(self, gmail):
        
        document = self.collection.count_documents({"Gmail": gmail})
        if document > 0:
            return True
        else:
            return False
        
    def create_post(self, gmail, post_data):
        # Update the user's document and push the post_data into the "Posts" array
        result = self.collection.update_one(
            {"Gmail": gmail},
            {
                "$set": {"LastModified": datetime.datetime.utcnow()},  # Optional: Update a timestamp for the last modification
                "$push": {"Posts": post_data}
            }
        )

        if result.modified_count > 0:
            return True
        else:
            return False
