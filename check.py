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

sub = ['Askreddit']  # make a list of subreddits you want to scrape the data from

for s in sub:
    subreddit = reddit.subreddit(s)   # Chosing the subreddit


########################################
#   CREATING DICTIONARY TO STORE THE DATA WHICH WILL BE CONVERTED TO A DATAFRAME
########################################

#   NOTE: ALL THE POST DATA AND COMMENT DATA WILL BE SAVED IN TWO DIFFERENT
#   DATASETS AND LATER CAN BE MAPPED USING IDS OF POSTS/COMMENTS AS WE WILL
#   BE CAPTURING ALL IDS THAT COME IN OUR WAY

# SCRAPING CAN BE DONE VIA VARIOUS STRATEGIES {HOT,TOP,etc} we will go with keyword strategy i.e using search a keyword
    query = ['WouldYouRather']

    for item in query:
        post_dict = {
            "title" : [],
            "score" : [],
            "id" : [],
            "url" : [],
            "comms_num": [],
            "created" : [],
            "body" : []
        }
        comments_dict = {
            "comment_id" : [],
            "comment_parent_id" : [],
            "comment_body" : [],
            "comment_link_id" : []
        }
        for submission in subreddit.search(query,sort = "top",limit = 1):
            post_dict["title"].append(submission.title)
            post_dict["score"].append(submission.title)
            post_dict["id"].append(submission.title)
            post_dict["url"].append(submission.title)
            post_dict["comms_num"].append(submission.title)
            post_dict["created"].append(submission.title)
            post_dict["body"].append(submission.title)

            ##### Acessing comments on the post
            submission.comments.replace_more(limit = 5)
            for comment in submission.comments.list():
                comments_dict["comment_id"].append(comment.id)
                comments_dict["comment_parent_id"].append(comment.parent_id)
                comments_dict["comment_body"].append(comment.body)
                comments_dict["comment_link_id"].append(comment.link_id)

        post_comments = pd.DataFrame(comments_dict)

        post_comments.to_csv(s+"_comments_"+ item +"/WouldYouRather-C.csv")
        post_data = pd.DataFrame(post_dict)
        post_data.to_csv(s+"_"+ item +"/WouldYouRather-D.csv")
