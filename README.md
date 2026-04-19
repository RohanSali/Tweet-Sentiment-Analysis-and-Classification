# 🐦 Tweet Sentiment Analysis System

## 📌 Project Overview

This project is a complete **Machine Learning-based Tweet Sentiment Analysis System** that classifies tweets into **Positive** or **Negative** sentiments.

It includes:

* Data preprocessing and analysis
* Multiple ML models
* Hyperparameter tuning
* Model comparison
* Backend API (FastAPI)
* Frontend dashboard (Streamlit)
* Deployment-ready architecture

---

## 🧠 Features

* 🔍 Text preprocessing and cleaning
* 📊 Data visualization and analysis
* 🤖 Multiple ML models:

  * Logistic Regression
  * Multinomial Naive Bayes
  * Support Vector Machine (SVM)
* ⚙️ Hyperparameter tuning using GridSearchCV
* 📈 Model comparison (Accuracy, Precision, Recall, F1-score)
* 🌐 REST API using FastAPI
* 💻 Interactive UI using Streamlit
* 🧪 API testing using Postman

---

## 📁 Project Structure

```
tweet-sentiment-app/
│
├── backend/
│   └── api.py                  # FastAPI backend
│
├── application/
│   └── app.py                  # Streamlit frontend
│
├── modeling/
│   ├── tweet.csv               # Dataset
│   └── model_training.ipynb    # ML development notebook
│
├── sentiment_model.pkl         # Trained model (generated after training)
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Technologies Used

* Python
* Scikit-learn
* Pandas & NumPy
* Matplotlib & Seaborn
* Streamlit
* FastAPI
* Uvicorn
* Postman (for API testing)

---

## 🔬 Machine Learning Workflow

### 1. Data Preprocessing

* Lowercasing
* URL removal
* Mention removal
* Special character cleaning

### 2. Data Wrangling

* Label generation
* Dataset structuring

### 3. Feature Engineering

* TF-IDF Vectorization

### 4. Models Used

* Logistic Regression
* Multinomial Naive Bayes
* Support Vector Machine (SVM)

### 5. Model Training Strategy

* Baseline models (poor hyperparameters)
* Improved models
* Tuned model using GridSearchCV

### 6. Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-score

---

## 🚀 Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-link>
cd Tweet-Sentiment-Analysis-and-Classification
```

---

### 2. Create Virtual Environment (Recommended)

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Train the Model

* 📥 Dataset Download Instructions

The dataset used in this project is not included in the repository due to size constraints. Please follow the steps below to download and set it up:

1. Go to the dataset link:
   https://www.kaggle.com/datasets/ruchi798/data-science-tweets

2. Download the dataset (ZIP file) from Kaggle.

3. Extract the downloaded file.

4. Locate the dataset file (e.g., `tweets.csv`).

5. Place the file inside the `modeling/` folder of this project:

```
tweet-sentiment-app/
└── modeling/
    └── tweets.csv
```

⚠️ Make sure the filename matches exactly as used in the notebook (`tweets.csv`) to avoid errors.


* Open Jupyter Notebook:

```
jupyter notebook
```

* Run:

```
modeling/model_training.ipynb
```

* This will generate:

```
sentiment_model.pkl
```

**Always keep trained model in root directory!**
---

## ▶️ Running the Application

---

### 🔹 Run Backend (FastAPI)

```
uvicorn backend.api:app --reload
```

Access:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

### 🔹 Run Frontend (Streamlit)

```
streamlit run application/app.py
```

---

## 🧪 API Testing (Postman)

### Endpoint:

```
POST http://127.0.0.1:8000/predict
```

### Request Body:

```json
{
    "text": "I love this product!"
}
```

### Response:

```json
{
    "input": "I love this product!",
    "cleaned": "i love this product",
    "prediction": "positive"
}
```

---

## 📊 Model Comparison

The project compares:

* 3 Baseline Models
* 3 Improved Models
* 1 Tuned Model

Evaluation is done using:

* Accuracy
* Precision
* Recall
* F1 Score

Visualization includes:

* Bar graphs
* Performance comparison charts

---

## 🌐 Deployment

The project is deployment-ready and can be deployed using:

* Streamlit Cloud
* Render / Railway (for API)

---

## 💡 Future Improvements

* Add Deep Learning models (LSTM / BERT)
* Real-time Twitter API integration
* Multi-class sentiment classification
* Explainable AI (word importance)

---

## 👨‍💻 Author

**Rohan Sali**

---

## 📜 License

This project is for educational purposes.