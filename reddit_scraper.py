# Importing the packages
import numpy as np
import pandas as pd
import praw


# Let's access the reddit API

reddit = praw.Reddit(client_id = "", # My Personal Client ID
                     client_secret = "m4SwkYvXN6MsBIdjAV_qp2gT1jI", # Your client secret
                     user_agent = "", # User Agent Name
                     username = "", # Reddit username
                     password = "")

# Make a list of all subreddits you want to scrape the data from
reddit_list = ['Askreddit']

for text in reddit_list:
    subreddit = reddit.subreddit(text) # Chooses the subreddit
    print(text)
