# Initialize VADER SentimentIntensityAnalyzer
#from nltk.sentiment.vader import SentimentIntensityAnalyzer      #import again otherwise throws error
#sia = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis using VADER
def analyze_sentiment_vader(review):
    sentiment_score = sia.polarity_scores(review)
    if sentiment_score['compound'] >= 0.05:
        return "Positive"
    elif sentiment_score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Streamlit app
import streamlit as st    #import again otherwise throws error
st.title("Restaurant or Other Reviews Sentiment Analysis")

# Input: restaurant review from the user
review = st.text_area("Enter the restaurant or other review here:")

# If the user submits a review
if st.button("Analyze Sentiment"):
    if review:
        sentiment = analyze_sentiment_vader(review)
        st.write(f"The sentiment of the review is: **{sentiment}**")
    else:
        st.warning("Please enter a review to analyze.")
