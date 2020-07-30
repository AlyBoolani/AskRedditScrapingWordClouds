# Here we're going to first make all imports
# Imports for application set up
import streamlit as st
import joblib, os

# EDA Packages
import numpy as np
import pandas as pd

# Importing Wordcloud
from wordcloud import WordCloud
from PIL import Image

# Visualization
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# Vectorizing our texts
from sklearn.feature_extraction.text import CountVectorizer

# Importing Natural Language ToolKit and its essential packages
import nltk
# For removing stopwords
from nltk.corpus import stopwords

# For lemmatizing our words
from nltk.stem import WordNetLemmatizer

# Now that our imports are done, let's set up a list of stopwords using the NLTK library
stopwords = nltk.corpus.stopwords.words('english')
listofstopwords = list(stopwords)

# To lemmatize our words, let's get that done # TODO:
lemmatizer = WordNetLemmatizer()

def lemmatization(text):
    for word in text:
        listofwords = text.split(' ')

    lemmatized_words = []

    for word in listofwords:
        if (not word in listofstopwords) and (word != ''):
            lemmatized_text = lemmatizer.lemmatize(word)
            lemmatized_words.append(lemmatized_text)

    return lemmatized_words


def main():
    '''Identify the topics being discussed in various subreddits'''
    st.title('Identification of topics being discussed in subreddits')
    st.subheader("Identies the reddit posted by users within the subreddit and produces a wordcloud and some analytics that'll be coming up in the future" )
    st.markdown('Owned by Aly Boolani')

    options = [ "Check what's happening in multiple subreddits?", "Just show what's being scraped!", ""]

    choice = st.sidebar.selectbox("Choose from one of the following options:",options)

    if choice == "Check what's happening in multiple subreddits?":
        st.info('This will show different word clouds of subreddits, please check which ones you want to display below:')

        # User will be provided with a checkbox to summon a WordCloud given user decides to see what's happening in subreddits
        if st.checkbox('WordCloud'):
            wordcloud = WordCloud().generate()
            plt.imshow(wordcloud, interpolation = 'bilinear')
            plt.axis('off')
            st.pyplot()

    #     if st.checkbox("Tabulize the data"):
    #     ### FILL IN HERE ###
    #
    # if choice == "Just show what's being scraped!":
    #     st.info('Shows the data being scrapped from reddit')

    # This will be the last line
    if __name__ == '__main__':
    	main()
