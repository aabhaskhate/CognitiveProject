import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained model
with open("rf.pkl", "rb") as file:
    model = joblib.load(file)

# Title and Header
st.set_page_config(page_title="ASTRA - Advanced System for Transaction Risk Analysis", layout="wide")
st.title("🔍 ASTRA - Advanced System for Transaction Risk Analysis")
st.markdown("### Predict fraudulent transactions with accuracy and speed.")

# File Upload Section
uploaded_file = st.file_uploader("Upload Transaction Data (CSV format)", type=["csv"])

if uploaded_file is not None:
    # Load data
    data = pd.read_csv(uploaded_file)

    # Display data preview
    st.write("### Data Preview")
    st.dataframe(data.head())

    # Required feature columns
    required_features = ['Gender', 'Age', 'State', 'City', 'Bank_Branch', 'Account_Type', 
                         'Transaction_Device', 'Device_Type', 'Merchant_Category', 
                         'Transaction_Location', 'Account_Balance']

    # Encode categorical variables
    encoder = LabelEncoder()
    for col in required_features:
        if data[col].dtype == 'object':
            data[col] = encoder.fit_transform(data[col].astype(str))

    # Select only required features
    features = data[required_features]

    # Prediction
    try:
        predictions = model.predict(features)
        
        data['Fraud_Prediction'] = ['🔴 FRAUD' if pred == 1 else '🟢 NOT FRAUD' for pred in predictions]
        data['Prediction'] = predictions

        # Display Results
        st.write("### Predictions")
        st.dataframe(data[['Customer_ID', 'Transaction_Amount', 'Fraud_Prediction']])

        # Summary Statistics
        fraud_count = data['Prediction'].sum()
        total_transactions = len(data)
        fraud_percentage = (fraud_count / total_transactions) * 100

        st.markdown(f"✅ **Total Transactions:** {total_transactions}")
        st.markdown(f"🚨 **Detected Fraudulent Transactions:** {fraud_count}")
        st.markdown(f"📊 **Fraud Percentage:** {fraud_percentage:.2f}%")

    except Exception as e:
        st.error(f"Error during prediction: {e}")

    # Download Results
    st.download_button(
        label="📥 Download Results",
        data=data.to_csv(index=False).encode('utf-8'),
        file_name='ASTRA_Predictions.csv',
        mime='text/csv'
    )

# Footer
st.markdown("---")
st.markdown("💻 **Developed by Anirudh Sharma** | 🚀 Powered by Random Forest")