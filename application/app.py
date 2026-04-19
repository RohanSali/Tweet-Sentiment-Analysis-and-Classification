import streamlit as st
import pickle
import re

st.set_page_config(
    page_title="Tweet Sentiment Analyzer",
    page_icon="🐦",
    layout="wide"
)

@st.cache_resource
def load_model():
    with open("../sentiment_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

def clean_tweet_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\.\S+', ' ', text)
    text = re.sub(r'@\w+', ' ', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

st.sidebar.title("📊 About This App")

st.sidebar.markdown("""
### 🐦 Tweet Sentiment Analyzer

This app uses a Machine Learning model to classify tweets into:

- 😊 **Positive**
- 😡 **Negative**

---

### ⚙️ Model Info
- TF-IDF Vectorization
- Logistic Regression / Naive Bayes
- Trained on tweet dataset

---

### 🧠 How It Works
1. Cleans tweet text
2. Converts to numerical vectors
3. Predicts sentiment

---

### ✍️ Try Examples:
- "I love this product!"
- "Worst service ever"
- "This is amazing 🔥"
- "I hate this so much"

---
""")

st.markdown(
    "<h1 style='text-align: center;'>🐦 Tweet Sentiment Analyzer</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Analyze sentiment of tweets using Machine Learning</p>",
    unsafe_allow_html=True
)

st.divider()

col1, col2 = st.columns([3, 1])

with col1:
    user_input = st.text_area("✍️ Enter Tweet", height=150)

with col2:
    st.write("")
    st.write("")
    analyze_btn = st.button("🚀 Analyze", use_container_width=True)

if "history" not in st.session_state:
    st.session_state.history = []

if analyze_btn:
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a tweet")
    else:
        cleaned = clean_tweet_text(user_input)
        prediction = model.predict([cleaned])[0]

        # Confidence (if available)
        try:
            proba = model.predict_proba([cleaned])[0]
            confidence = max(proba)
            confidence_percent = int(confidence * 100) if confidence else 0
        except:
            confidence = None
            confidence_percent = None

        # Store history
        st.session_state.history.append((user_input, prediction))

        st.divider()

        # -----------------------------
        # Result Display
        # -----------------------------
        if confidence is not None:
            confidence_text = f"{confidence:.2f}"
        else:
            confidence_text = "N/A"

        if prediction == "positive":
            st.markdown(
                f"""
                <div style="
                    background-color:#d4edda;
                    padding:20px;
                    border-radius:10px;
                    text-align:center;
                ">
                    <h2>😊 Positive Sentiment</h2>
                    <p>Confidence: {confidence_text}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="
                    background-color:#f8d7da;
                    padding:20px;
                    border-radius:10px;
                    text-align:center;
                ">
                    <h2>😡 Negative Sentiment</h2>
                    <p>Confidence: {confidence_text}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        st.markdown("### 📊 Confidence Level")

        # Color logic
        if confidence_percent >= 75:
            color = "#28a745"  # green
        elif confidence_percent >= 50:
            color = "#ffc107"  # yellow
        else:
            color = "#dc3545"  # red

        # Custom progress bar
        st.markdown(
            f"""
            <div style="
                background-color:#e9ecef;
                border-radius:10px;
                padding:5px;
            ">
                <div style="
                    width:{confidence_percent}%;
                    background-color:{color};
                    padding:10px;
                    border-radius:10px;
                    text-align:center;
                    color:white;
                    font-weight:bold;
                ">
                    {confidence_percent}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

if st.session_state.history:
    st.divider()
    st.subheader("📜 Prediction History")

    for text, pred in reversed(st.session_state.history[-5:]):
        if pred == "positive":
            st.success(f"{text} → Positive")
        else:
            st.error(f"{text} → Negative")