import numpy as np
import pandas as pd
import spacy
import streamlit as st
import joblib, os
import praw
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib

# Bringing in the NLP from spacy
nlp = spacy.load('en')
matplotlib.use('Agg')

# Setting up the Reddit API
reddit = praw.Reddit(client_id="FWbEmuCqSOXSoQ",#my client id
                     client_secret="a162d_sAWRbTVxCl3ZZlvtATADo",  #your client secret
                     user_agent="ScrapingScript", #user agent name
                     username = "Psychological-Elk232",     # your reddit username
                     password = "Webscraping101!")     # your reddit password


def main():
    """
    This function will help navigate through the application.
    """
    st.title('AskReddit Topic Discovering using NLP')
    st.subheader('Identify Topics within the AskReddit subreddit')
    st.markdown('Application created by Aly Boolani using Streamlit')

    # Allowing for user to choose from type of reddit
    types_of_reddits = ['Announcements','Funny','AskReddit','Gaming','Aww','Pics','Music','Science','Worldnews','Videos']
    choice = st.sidebar.selectbox('Choose Subreddit', types_of_reddits)

    # Allowing for choosing which one they want
    ratings = ['Hot', 'New', 'Top', 'Controversial', 'Rising']

    #st.sidebar.button('Display DataFrame')

    # Letting the user select from a bunch of options
    if choice == 'Announcements':
        st.info(f"Showing {choice} posts")
        st.selectbox('Choose from one of the following:', ratings)
        announcements_posts = []
        announcements_subreddits = reddit.subreddit('announcements')
        # if users selects hot
        if ratings == 'Hot':
            for post in announcements_subreddits.hot(limit = 5):
                announcements_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
                columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
                announcements_df = pd.DataFrame(announcements_posts, columns = columns)
            st.write(announcements_df)

        # If user selects new
        if ratings == 'New':
            for post in announcements_subreddits.new(limit = 5):
                announcements_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
                columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
                announcements_df = pd.DataFrame(announcements_posts, columns = columns)
            st.write(announcements_df)

        # If user selects top
        if ratings == 'Top':
            for post in announcements_subreddits.top(limit = 5):
                announcements_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
                columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
                announcements_df = pd.DataFrame(announcements_posts, columns = columns)
            st.write(announcements_df)

        # If user selects controversial
        if ratings == 'Controversial':
            for post in announcements_subreddits.controversial(limit = 5):
                announcements_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
                columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
                announcements_df = pd.DataFrame(announcements_posts, columns = columns)
            st.write(announcements_df)

        # If user selects rising
        if ratings == 'Rising':
            for post in announcements_subreddits.rising(limit = 5):
                announcements_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
                columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
                announcements_df = pd.DataFrame(announcements_posts, columns = columns)
            st.write(announcements_df)

    # If user chooses funny
    elif choice == 'Funny':
        st.info(f"Showing {choice} posts")
        funny_posts = []
        funny_subreddits = reddit.subreddit('funny')
        for post in funny_subreddits.hot(limit = 5):
            funny_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
            columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
            funny_df = pd.DataFrame(funny_posts, columns = columns)
        st.write(funny_df)

    # If user chooses askreddit
    elif choice == 'AskReddit':
        st.info(f"Showing {choice} posts")
        AskReddit_posts = []
        AskReddit_subreddits = reddit.subreddit('AskReddit')
        for post in AskReddit_subreddits.hot(limit = 5):
            AskReddit_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
            columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
            AskReddit_df = pd.DataFrame(AskReddit_posts, columns = columns)
        st.write(AskReddit_df)

    # If user chooses gaming
    elif choice == 'Gaming':
        st.info(f"Showing {choice} posts")
        gaming_posts = []
        gaming_subreddits = reddit.subreddit('gaming')
        for post in gaming_subreddits.hot(limit = 5):
            gaming_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
            columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
            gaming_df = pd.DataFrame(gaming_posts, columns = columns)
        st.write(gaming_df)

    # If user chooses aww
    elif choice == 'Aww':
        st.info(f"Showing {choice} posts")
        Aww_posts = []
        Aww_subreddits = reddit.subreddit('aww')
        for post in Aww_subreddits.hot(limit = 5):
            Aww_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
            columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
            Aww_df = pd.DataFrame(Aww_posts, columns = columns)
        st.write(Aww_df)

    # If user choose pics
    elif choice == 'Pics':
        st.info(f"Showing {choice} posts")
        Pics_posts = []
        Pics_subreddits = reddit.subreddit('pics')
        for post in Pics_subreddits.hot(limit = 5):
            Pics_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
            columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
            Pics_df = pd.DataFrame(Pics_posts, columns = columns)
        st.write(Pics_df)

    # If user chooses music
    elif choice == 'Music':
        st.info(f"Showing {choice} posts")
        Music_posts = []
        Music_subreddits = reddit.subreddit('Music')
        for post in Music_subreddits.hot(limit = 5):
            Music_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
            columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
            Music_df = pd.DataFrame(Music_posts, columns = columns)
        st.write(Music_df)

    # If user chooses science
    elif choice == 'Science':
        st.info(f"Showing {choice} posts")
        Science_posts = []
        Science_subreddits = reddit.subreddit('Science')
        for post in Science_subreddits.hot(limit = 5):
            Science_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
            columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
            Science_df = pd.DataFrame(Science_posts, columns = columns)
        st.write(Science_df)

    # If user chooses worldnews
    elif choice == 'Worldnews':
        st.info(f"Showing {choice} posts")
        Worldnews_posts = []
        Worldnews_subreddits = reddit.subreddit('Worldnews')
        for post in Worldnews_subreddits.hot(limit = 5):
            Worldnews_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
            columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
            Worldnews_df = pd.DataFrame(Worldnews_posts, columns = columns)
        st.write(Worldnews_df)

    # If user chooses videos
    elif choice == 'Videos':
        st.info(f"Showing {choice} posts")
        Videos_posts = []
        Videos_subreddits = reddit.subreddit('Videos')
        for post in Videos_subreddits.hot(limit = 5):
            Videos_posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
            columns = ['title','score','id','subreddit','url','num_of_comments','text_body','created']
            Videos_df = pd.DataFrame(Videos_posts, columns = columns)
        st.write(Videos_df)
        if st.checkbox('WordCloud'):
                text = st.dataframe(data = Videos_df['title'])

                #wordcloud = WordCloud().generate(text)
                #plt.imshow(wordcloud, interpolation = 'bilinear')
                #plt.axis('off')
                #st.pyplot()


if __name__ == '__main__':
    main()
