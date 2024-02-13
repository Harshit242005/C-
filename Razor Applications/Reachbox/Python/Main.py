# we would be creating the user and the recommendation algorithm in the main tree
import CraeteUser
import CreatePost
import ConnectUser
import ViewedBy
from mongo_connection import get_mongo_connection
# getting python packages
from datetime import datetime
from bson import ObjectId  # Import ObjectId from bson module


class reachbox:
    def __init__(self):
        return 
    
    # creating new user
    def create_user(self, gmail, name, tech_list):
        create = CraeteUser(gmail, name, tech_list)
        print(f'created user details: {create}')


    # for creating post
    def create_post(self, gmail, Heading, Description, tech_include):
        post_creation_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        unique_id = str(ObjectId())  # Generate a unique ObjectId as a string
        post_data = {
            "Created_by": gmail,
            "PostId": unique_id, # either this should be random
            "Heading": Heading,
            "Description": Description,
            "Like": 0,
            "Bookmark": 0,
            "Repost": 0,
            "Liked_by": [],
            "Reposted_by": [],
            "TechIncluded": tech_include,
            "Created_at": post_creation_time,
            "viewed_by": [] # this would help us ion creting an array that would make sure post is fresh
        }
        created_post = CreatePost(gmail, post_data)
        print(f'created post: {created_post}')

    def viewed_by(self, gmail, post_id):
        ViewedBy(gmail, post_id)

    def connect(self, gmail, other_gmail):
        connect_user = ConnectUser(gmail, other_gmail)
        print(f'connected user: {connect_user}')
        

    # this right here we would show up the user feed 
    def show_feed(self, gmail):
        # you would have some posts recommended
        
        return