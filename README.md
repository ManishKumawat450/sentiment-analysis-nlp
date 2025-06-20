# 📝 Sentiment Analysis of Restaurant Reviews using NLP

A Streamlit-based web app that classifies restaurant customer reviews as **Positive** or **Negative** using Natural Language Processing and a Multinomial Naive Bayes classifier.

[🚀 Live App]([https://your-app-name.streamlit.app](https://nlp-sentiment-analysis-manish-kumawat.streamlit.app/)) ← Replace with your actual Streamlit link  
[📂 View Code on GitHub](https://github.com/ManishKumawat450/sentiment-analysis-nlp)

---

## 📌 Features

- Text cleaning: Lowercasing, regex, stopword removal, stemming
- Feature extraction using Bag-of-Words (CountVectorizer)
- Model: Multinomial Naive Bayes (scikit-learn)
- User interface using Streamlit
- Real-time sentiment prediction from user input

---

## 🧠 How it Works

1. The user types a review
2. Review is preprocessed and vectorized
3. Model predicts sentiment (0 = Negative, 1 = Positive)
4. Prediction is shown live on the web

---

## ⚙️ Tech Stack

- Python
- NLTK
- Scikit-learn
- Pandas
- Streamlit

---

## 🧪 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/ManishKumawat450/sentiment-analysis-nlp.git
cd sentiment-analysis-nlp

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
