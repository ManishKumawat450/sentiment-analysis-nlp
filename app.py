import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk

nltk.download('stopwords')

# Load the model and vectorizer
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

ps = PorterStemmer()

def preprocess_review(review):
    review = re.sub('[^a-zA-Z]', ' ', review)
    review = review.lower().split()
    review = [ps.stem(word) for word in review if word not in stopwords.words('english')]
    return ' '.join(review)

def predict_sentiment(text):
    processed = preprocess_review(text)
    vectorized = vectorizer.transform([processed]).toarray()
    result = model.predict(vectorized)
    return "✅ Positive Review" if result[0] == 1 else "❌ Negative Review"

# Streamlit app layout
st.title("🍽️ Restaurant Review Sentiment Analyzer")
st.markdown("Enter your review and check if it's Positive or Negative.")

input_review = st.text_area("📝 Type your review here:")

if st.button("Predict Sentiment"):
    if input_review.strip():
        result = predict_sentiment(input_review)
        st.success(f"Prediction: {result}")
    else:
        st.warning("⚠️ Please type something to analyze.")
