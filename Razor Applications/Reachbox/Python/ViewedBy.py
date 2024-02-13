from mongo_connection import get_mongo_connection

class Viewed_by:
    def __init__(self, gmail, post_id):
        self.collecton = get_mongo_connection("CodeUp", "Users")
       
        document = self.collecton.find_one({"Gmail": gmail})
        if document:
            self.add_view_by(gmail, post_id)
            


    def add_view_by(self, gmail, post_id):
        collection = get_mongo_connection("CodeUp", "Posts")
        post_doc = collection.find_one({"PostId": post_id})
        if post_doc:
            # Update the "viewed_by" array using $addToSet
            collection.update_one(
                {"PostId": post_id},
                {"$addToSet": {"viewed_by": gmail}}
            )
            print(f"Post {post_id} viewed by {gmail}")
        else:
            print(f"No post found with ID {post_id}")