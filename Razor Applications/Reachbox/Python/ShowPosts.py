# here we would get the post for the user 
# according to his specification

# priorities of the post appearance - 
#   - connect
#   - interest

from mongo_connection import get_mongo_connection

class GetPosts:
    def __init__(self, gmail):
        # user gamil who is trying to get the post
        self.connect_users = self.get_user_connect(gmail)
        self.posts = self.get_posts(self.connect_users)
        self.all_posts = self.get_all_pos()
        self.not_viewed_by_me = self.get_not_viewed(self.posts, gmail)
        self.liked_by_my_connects = self.liked_by_connects(self.all_posts, self.connect_users)
        self.repost_by_my_connects = self.repost_by_connects(self.all_posts, self.connect_users)
        self.return_all_post(self.not_viewed_by_me, 
                             self.liked_by_my_connects,
                             self.repost_by_my_connects)


    def get_user_connect(self, gmail):
        users = get_mongo_connection('CodeUp', 'Users')
        # got the user doc
        document = users.find_one({"Gmail": gmail})
        if document:
            connect_users = document["Connects"]
            return connect_users
        else:
            print("user does not exist for getting his posts")

    def get_posts(self, users):
        # getting each users posts
        users_collection = get_mongo_connection('CodeUp', 'Users')
        # all the users 
        all_posts = []
        for user in users:
            user_doc = users_collection.find_one({"Gmail": user})
            if user_doc:
                posts = user_doc["Posts"]
                # assuming the posts is list
                all_posts.append(posts)
        print(f'all posts are: {all_posts}')
        return all_posts
    
    def get_not_viewed(self, posts, gmail):
        # get all the post which are not viewed by me 
        all_posts_not_viewed_by_me = []
        for post in posts:
            if gmail not in post["viewed_by"]:
                all_posts_not_viewed_by_me.append(post)
        print(f'posts not viewed by me: {all_posts_not_viewed_by_me}')
        return all_posts_not_viewed_by_me
    
    # get post liked by my connects
    def get_like_by_connects(self, all_posts, connects):
        
        return
    
    # get all post retweet by my connects
    def get_repost_by_connects(self, all_posts, connects):
        return 
    

    def return_all_post(self, not_viewed_post, connects_liked_post, connects_repost_post):
        all_post = []
        all_post += not_viewed_post
        all_post += connects_liked_post
        all_post += connects_repost_post

        return all_post