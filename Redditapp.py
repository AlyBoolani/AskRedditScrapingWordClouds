import numpy as np
import pandas as pd
import spacy
import streamlit as st
import joblib, os
from WordCloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib

# Bringing in the NLP from spacy
nlp = spacy.load('en')
matplotlib.use('Agg')



def main():
    """
    This function will help navigate through the application.
    """
    st.title('AskReddit Topic Discovering using NLP')
    st.subheader('Identify Topics within the AskReddit subreddit')
    st.markdown('Application created by Aly Boolani using Streamlit')

    activities = ['AskReddit', 'Gaming', 'Sports', 'FiftyFifty']
    choice = st.sidebar.dropdown('Choose Activity', activities)

    # Letting the user pick the options
    if choice == 'Ask Reddit':
        st.info("Using the subreddit: AskReddit")
        reddit = praw.Reddit(client_id = "", # My Personal Client ID
                             client_secret = "", # Your client secret
                             user_agent = "", # User Agent Name
                             username = "Psychological-Elk232", # Reddit username
                             password = "Webscraping101!")

        # Make a list of all subreddits you want to scrape the data from
        reddit_list = ['Askreddit']

        for text in reddit_list:
            subreddit = reddit.subreddit(text) # Chooses the subreddit
            print(text)
