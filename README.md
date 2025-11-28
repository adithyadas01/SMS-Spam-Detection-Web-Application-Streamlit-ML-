# 📧 Spam Message Classification Project

## 📝 1. Introduction
Spam messages are one of the most common cybersecurity threats faced by users today.  
They often contain misleading offers, phishing links, malware downloads, or fake promotions.  

The goal of this project is to build a **Machine Learning–based Spam Classifier** that can automatically detect whether a given SMS/text message is:
- **Spam** (unwanted/unsafe)
- **Ham** (legitimate)

This project uses Natural Language Processing (NLP) techniques and a machine learning model trained on labeled SMS data.

---

## 🎯 2. Project Objective
- Preprocess and clean text messages  
- Convert text into numerical vectors  
- Train a classification model  
- Evaluate performance  
- Deploy the final model using **Streamlit**

---

## 📂 3. Dataset Description
The dataset contains two main columns:

| Column Name | Description |
|------------|-------------|
| **label**  | Category of message — 'spam' or 'ham' |
| **message** | Actual SMS text message |

Example entries:

| label | message |
|------|---------|
| ham | "Hey, are we meeting today?" |
| spam | "You've won a FREE gift! Claim now: http://xyz.win" |

Dataset Source: Public SMS Spam Collection dataset.

---

## 🧹 4. Data Preprocessing Steps
To prepare the text for machine learning, the following steps were applied:

1. **Lowercasing**  
2. **Removing punctuation**  
3. **Tokenization**  
4. **Stopword removal**  
5. **Stemming / Lemmatization**  
6. **Text vectorization using TF-IDF**

---

## 🤖 5. Machine Learning Model

The following algorithms were evaluated:

- Naïve Bayes (MultinomialNB)
- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest

**Final Model Used:**  
⭐ **Multinomial Naïve Bayes** (Best accuracy + fastest training)

---

## 📊 6. Model Evaluation

The classifier was evaluated using:

- Accuracy  
- Precision  
- Recall  
- F1-score  
- Confusion Matrix  

**Results (Example):**

| Metric | Score |
|--------|--------|
| Accuracy | 0.97 |
| Precision | 0.96 |
| Recall | 0.98 |
| F1-score | 0.97 |

The model performs well in detecting spam with high precision and recall.

---

## 🧪 7. Example Predictions

**Input:**  
"Congratulations! You won a $500 Amazon Voucher. Click here to claim."

**Output:**  
`spam`

**Input:**  
"Can we meet tomorrow at 4 PM?"

**Output:**  
`ham`

---

## 🖥️ 8. Streamlit App Overview

The Streamlit app allows users to:

- Enter a custom text message  
- Click **Predict**
- View whether it's **Spam** or **Ham**
- Background image added for UI enhancement  
- Model loaded using `pickle`

Features include:

- Clean UI  
- Fast predictions  
- Real-time text classification  

---

## 🗂️ 9. Project Structure

Spam-Detection/
│
├── app.py # Streamlit UI
├── model.pkl # Trained ML model
├── vectorizer.pkl # TF-IDF vectorizer
├── spam.jpg # Background image
├── README.md # Project documentation
└── dataset.csv # SMS spam dataset


---

## 📧 10. Sample Spam Messages (For Testing)

- "Claim your FREE prize now!!! Click here"
- "You won ₹10,000 Cashback. Visit link immediately!"
- "Your bank account is blocked. Click the link to verify."
- "Exclusive offer!! Buy 1 Get 3 free!"

---

## ✅ 11. Conclusion

This project demonstrates how NLP and Machine Learning can be used effectively to classify spam messages.  
The final system:

- Identifies spam with high accuracy  
- Provides fast real-time prediction  
- Is deployed using an interactive Streamlit interface  
- Can be extended to email filtering, fraud detection, and SMS monitoring  

This Spam Detection System is a practical and deployable solution for real-world text classification.

---

## 🚀 12. Future Improvements
- Deep learning models (LSTM, BERT)  
- Real-time email integration  
- Multi-language spam detection  
- Browser-based extension  

---

## 🙌 13. Acknowledgements
- SMS Spam Collection Dataset  
- Scikit-learn  
- Streamlit  

