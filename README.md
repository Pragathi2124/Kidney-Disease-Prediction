# 🩺 Kidney Disease Prediction using Machine Learning
“Machine learning model to predict kidney disease”
## 🚀 Overview
This project aims to develop a robust machine learning model capable of accurately classifying whether a patient has Chronic Kidney Disease (CKD) based on a comprehensive set of clinical and laboratory attributes. It includes data preprocessing, model training, evaluation, and a user-friendly Streamlit web application for interactive predictions.

## ✨ Features
* **Data Preprocessing:** Handling missing values, encoding categorical features, and scaling numerical data to prepare the dataset for model training.
* **Exploratory Data Analysis (EDA):** In-depth analysis and visualization of clinical and laboratory attributes to understand their distribution, relationships, and correlation with CKD.
* **Machine Learning Model Development:** Training and evaluation of a classification model (e.g.,Logistic Regression, Decision Tree, Random Forest, XGBoost, SVM, KNN, Naive Bayes) for accurate CKD prediction.
* **Model Persistence:** Saving the trained machine learning model (`classifier.pkl`) and the data scaler (`scaler.pkl`) using `pickle` for easy deployment and future use.
* **Interactive Web Application:** A Streamlit-based interface (`app.py`) for real-time patient data input and instant CKD risk prediction, making the model accessible and usable.

## 📊 Dataset
The model is trained on a dataset containing various clinical and laboratory attributes related to kidney function. Key features, used as input for the prediction, include:
* **Clinical:** Age, Blood Pressure, Specific Gravity, Albumin, Sugar, Hypertension, Diabetes Mellitus, Coronary Artery Disease, Appetite, Pedal Edema, Anemia.
* **Laboratory:** Red Blood Cells, Pus Cells, Pus Cell Clumps, Bacteria, Blood Glucose Random, Blood Urea, Serum Creatinine, Sodium, Potassium, Hemoglobin, Packed Cell Volume, White Blood Cell Count, Red Blood Cell Count.

  ## 🛠️ Technologies Used
* **Programming Language:** Python 3.x
* **Data Manipulation & Analysis:** `pandas`, `numpy`
* **Visualization:** `matplotlib`, `seaborn`
* **Machine Learning:** `scikit-learn` (for preprocessing, model selection, and classification algorithms)
* **Web Application Framework:** `streamlit`
* **Model Persistence:** `pickle`
* **Development Environment:** Jupyter Notebook
* **Version Control:** Git, GitHub

A Streamlit web app that predicts the likelihood of kidney disease based on patient medical input using a Voting Classifier model.

## 📊 Features

- User input form for 24 medical parameters
- Data preprocessing with StandardScaler
- VotingClassifier model (Logistic Regression, Decision Tree, Random Forest, XGBoost, SVM, KNN, Naive Bayes)
- Clean UI with prediction output

  After clicking Predict, the model outputs:

✅ "The patient is not likely to have Kidney Disease"

❌ "The patient is likely to have Kidney Disease"


## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/kidney-disease-predictor.git
cd kidney-disease-predictor

### 2. Install Requirements

```bash
pip install -r requirements.txt

### 3. Run the Streamlit App
```bash
streamlit run app.py




