#######
# IMPORT PACKAGES
#######
import praw
import pandas as pd


# Acessing the reddit api
reddit = praw.Reddit(client_id="FWbEmuCqSOXSoQ",#my client id
                     client_secret="a162d_sAWRbTVxCl3ZZlvtATADo",  #your client secret
                     user_agent="ScrapingScript", #user agent name
                     username = "Psychological-Elk232",     # your reddit username
                     password = "Webscraping101!")     # your reddit password

# get hottest posts from all subreddits
# hot_posts = reddit.subreddit('all').hot(limit=10)
# for post in hot_posts:
#     print(post.title)
# WE CAN SEE THAT THE API SEEMS TO BE WORKING. LET'S START TO COLLECT SOME Data

funny_posts = []

# Getting all subreddits
funny_subreddits = reddit.subreddit('funny')
for post in funny_subreddits.hot(limit = 10):
    funny_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])


columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
funny_posts = pd.DataFrame(funny_posts, columns = columns)

print(funny_posts)
