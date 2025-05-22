import streamlit as st
import pandas as pd
import joblib
import numpy as np
import plotly.express as px

# Enhanced CSS styling
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background-color: #f0f2f6;
    }
    .stApp {
        background: linear-gradient(135deg, #e0e7ff 0%, #f5f7fa 100%);
    }
    .stButton>button {
        color: white;
        background: linear-gradient(90deg, #4F8BF9 0%, #235390 100%);
        border-radius: 8px;
        font-weight: bold;
        padding: 0.5em 2em;
        margin-top: 1em;
    }
    .stFileUploader {
        border: 2px solid #4F8BF9;
        border-radius: 8px;
        background: #f8fafc;
    }
    .stDataFrame {
        background: #fff;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(79,139,249,0.08);
    }
    .metric-label {
        font-size: 1.1em;
        color: #4F8BF9;
        font-weight: bold;
    }
    .metric-value {
        font-size: 2em;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://img.icons8.com/ios-filled/100/4F8BF9/fraud.png", width=80)
st.sidebar.title("Fraud Detection App")
st.sidebar.markdown(
    """
    - Upload a CSV file with **30 input features** per row.
    - The app predicts the probability of fraud and non-fraud for each entry.
    - Download the results as a CSV.
    ---
    """
)

st.title("🔍 Fraud Detection App")
st.write(
    "Upload a CSV file with 30 input features per row. "
    "The app will predict the probability of fraud and non-fraud for each entry."
)

uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.subheader("📄 Uploaded Data Preview")
        st.dataframe(df.head(), use_container_width=True)

        if df.shape[1] != 30:
            st.error(f"❌ Expected 30 input features, but found {df.shape[1]}. Please upload a valid file.")
        else:
            try:
                model = joblib.load("best_model.joblib")
            except Exception as e:
                st.error(f"Error loading model: {e}")
                st.stop()

            try:
                with st.spinner("🔎 Predicting..."):
                    probabilities = model.predict_proba(df)
                    predictions = model.predict(df)
                    results = pd.DataFrame(
                        probabilities, columns=["Non-Fraud Probability", "Fraud Probability"]
                    )
                    results["Prediction"] = predictions

                    output = pd.concat([df, results], axis=1)
                    st.success("✅ Prediction completed!")

                    st.subheader("📊 Prediction Results")
                    st.dataframe(output, use_container_width=True)

                    # Count fraud and non-fraud cases
                    fraud_count = int((predictions == 1).sum())
                    nonfraud_count = int((predictions == 0).sum())
                    total = fraud_count + nonfraud_count

                    col1, col2, col3 = st.columns(3)
                    col1.metric("Total Cases", total)
                    col2.metric("Fraudulent Cases", fraud_count, delta=f"{fraud_count/total:.1%}", delta_color="inverse")
                    col3.metric("Non-Fraudulent Cases", nonfraud_count, delta=f"{nonfraud_count/total:.1%}")

                    # Pie chart
                    pie_df = pd.DataFrame({
                        "Type": ["Fraudulent", "Non-Fraudulent"],
                        "Count": [fraud_count, nonfraud_count]
                    })
                    fig = px.pie(pie_df, names="Type", values="Count", color="Type",
                                 color_discrete_map={"Fraudulent":"#FF6361", "Non-Fraudulent":"#58508D"},
                                 title="Fraud vs Non-Fraud Cases")
                    st.plotly_chart(fig, use_container_width=True)

                    # Download results
                    csv = output.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="⬇️ Download Results as CSV",
                        data=csv,
                        file_name='fraud_detection_results.csv',
                        mime='text/csv',
                    )
            except Exception as e:
                st.error(f"Prediction error: {e}")
    except Exception as e:
        st.error(f"File error: {e}")
else:
    st.info("Please upload a CSV file to get started.")