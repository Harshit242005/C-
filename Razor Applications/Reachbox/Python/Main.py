# we would be creating the user and the recommendation algorithm in the main tree
import CraeteUser
import CreatePost
import ConnectUser
class reachbox:
    def __init__(self):
        return 
    
    # creating new user
    def create_user(self, gmail, name, tech_list):
        create = CraeteUser(gmail, name, tech_list)
        print(f'created user details: {create}')


    # for creating post
    def create_post(self, gmail, Heading, Description, tech_include):
        post_data = {
            "Heading": Heading,
            "Description": Description,
            "TechIncluded": tech_include
        }
        created_post = CreatePost(gmail, post_data)
        print(f'created post: {created_post}')

    def connect(self, gmail, other_gmail):
        connect_user = ConnectUser(gmail, other_gmail)
        print(f'connected user: {connect_user}')


    # this right here we would show up the user feed 
    def show_feed(self, gmail):
        # you would have some posts recommended
        
        return