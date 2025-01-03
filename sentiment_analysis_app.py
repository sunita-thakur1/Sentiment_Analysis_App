# -*- coding: utf-8 -*-
"""Sentiment_Analysis_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14J1-5m5kSPKHRTC-_3bQ1CwOgt4F_C7m
"""

#!pip install streamlit
import streamlit as st
#import nltk
#nltk.download('vader_lexicon')
#!pip install sentiment
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
#from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

"""The **SentimentIntensityAnalyzer** class provides a method called polarity_scores() that takes a piece of text as input and returns a dictionary containing the sentiment scores for the text. The dictionary contains four keys: neg, neu, pos, and compound.                                               

neg: the negative sentiment score (between 0 and 1)                              
neu: the neutral sentiment score (between 0 and 1)                               
pos: the positive sentiment score (between 0 and 1)                              
compound: the overall sentiment score (between -1 and 1)                         
Link: https://medium.com/@rslavanyageetha/vader-a-comprehensive-guide-to-sentiment-analysis-in-python
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# # Initialize VADER SentimentIntensityAnalyzer
# from nltk.sentiment.vader import SentimentIntensityAnalyzer      #import again otherwise throws error
# sia = SentimentIntensityAnalyzer()
# 
# # Function to perform sentiment analysis using VADER
# def analyze_sentiment_vader(review):
#     sentiment_score = sia.polarity_scores(review)
#     if sentiment_score['compound'] >= 0.05:
#         return "Positive"
#     elif sentiment_score['compound'] <= -0.05:
#         return "Negative"
#     else:
#         return "Neutral"
# 
# # Streamlit app
# #import streamlit as st    #import again otherwise throws error
# st.title("Restaurant or Other Reviews Sentiment Analysis")
# 
# # Input: restaurant review from the user
# review = st.text_area("Enter the restaurant or other review here:")
# 
# # If the user submits a review
# if st.button("Analyze Sentiment"):
#     if review:
#         sentiment = analyze_sentiment_vader(review)
#         st.write(f"The sentiment of the review is: **{sentiment}**")
#     else:
#         st.warning("Please enter a review to analyze.")

#!streamlit run app.py & npx localtunnel --port 8501
#Run the app if name == “main”: main()

"""Steps to run the app:
1. Click: your url is: https://evil-showers-remain.loca.lt
2. Enter Tunnel Address as 35.237.49.77 from the output External URL.            
External URL: http://35.237.49.77:8501

To run the above app they ask you to submit or enter Tunnel Address or ipv4 or ipv6 address which is                                                  
35.237.49.77                                                                     
from the External URL link shown in the above output :External URL:
 http://35.237.49.77:8501/

 If it changes then update the Tunnel address accordingly.
"""
