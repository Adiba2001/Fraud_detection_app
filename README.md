# 🔍 Fraud Detection Web Application

An interactive machine learning web app developed to **spot total fraudulent and non-fraudulent credit card transactions** in real time. The project showcases end-to-end model development — from raw data analysis to a streamlined deployment using **Streamlit**.

---

## 🧠 About the Project

This tool leverages anonymized transactional data comprising **30 engineered features** ('Time',`V1` to `V28`, and `Amount`) to build a classification system that flags suspicious activity. It incorporates:
- Early data exploration
- Multiple model trials
- Feature transformation and tuning
- Model deployment via an intuitive web interface

---
## Project Layout ##
📁 fraud-detection-app/
│── app.py                                                # Main Streamlit interface
├── .gitignore                                            # Mentioning directories to ignore in version control.
├── Fraud_detection(by_Adiba) day(1-3).ipynb              # Notebook for initial data analysis & training and testing Base Line Models
├── Finalmodel_for_fraud_detection(day4).ipynb            # Final notebook for training and evaluating model(RandomForest Classifier)
├── best_model.joblib                                     # Saved and Load ML model
├── app_functioning-video.webm                            # App functioning video
└── requirements.txt                                      # Python package dependencies

---
## 🛠️ Phased Development Timeline

### ✅ Phase 1: Initial Data Exploration (EDA)
- Retrieved and examined the dataset from **Kaggle**.
- Identified severe class imbalance between fraud and non-fraud cases.
- Used visual tools (heatmaps, distribution plots) to understand feature behavior.
- Discovered outliers and the need for scaling (especially for the `Amount` feature).

---

### ✅ Phase 2: Building Baseline Models
- Tested a range of classification algorithms:
   🔹 Logistic Regression
   🔹 K-Nearest Neighbors (KNN)
   🔹 Decision Tree
   🔹 Naive Bayes
    
- Metrics used for evaluation:
   ✔️ Accuracy
   ✔️ Precision / Recall / F1-Score / Log loss
   ✔️ ROC-AUC
   ✔️ Confusion Matrix

### ✅ Phase 3: Feature Refinement + Model Optimization
✔️ Enhanced preprocessing pipeline:
  🔹 Normalization of skewed features
  🔹 Balanced class distribution using **undersampling** and **class_weight**
  🔹 Selected impactful features through recursive feature elimination
✔️ Hyperparameter tuning via `RandomizedSearchCV`
✔️ Finalized **Random Forest** as the optimal model for deployment

---

## 🖥️ App Preview

🎬 A demonstration video is available:  
👉 _[Add your app demo link here]_ 👈

Or try the live deployment:  
🌐 _[http://192.168.0.110:8501]_ 🌐

---

## 📚 Key Insights & Takeaways

- Experience with full ML lifecycle: raw data → deployed model
- Learned the significance of **interpretable ML** in financial applications
- Efficiently deployed ML models using **Streamlit**
- Balanced precision-recall tradeoffs for high-stakes decision-making

---

## ⚙️ Tech Stack

- **Language**: Python 3.13.2  
- **ML Libraries**: Panda, Numpy, Scikit-learn, imbalanced-learn  
- **Visualization**: Matplotlib, Seaborn  
- **App Framework**: Streamlit

---

## ▶️ How to Run Locally

```bash
# Clone the repository
git clone [https://github.com/Adiba2001/Fraud_detection_app].git
cd Fraud_detection_app

# Set up dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py
    
Certainly! Here’s a **concise version** of the *Learning Outcomes* section you can directly add to your `README.md`:

---

## 📘 Learning Outcomes 

* Gained hands-on experience with the end-to-end ML pipeline: from data exploration to deployment.
* Learned to handle imbalanced datasets using class_weight and undersampling.
* Compared multiple models using precision, recall, F1-score, and ROC-AUC.
* Applied feature scaling, selection, and hyperparameter tuning via `RandomizedSearchCV`.
* Serialized models with `joblib` for reuse in production.
* Built and deployed an interactive Streamlit app for real-time fraud prediction.
* Improved project structure, documentation, and version control with Git best practices.

---


