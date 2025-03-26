# ASTRA - Advanced System for Transaction Risk Analysis

## 🚨 Introduction
With the increasing adoption of digital payments, online fraud has become a significant concern. Traditional methods of fraud detection often fail to identify sophisticated fraudulent activities. 

**ASTRA** is an advanced fraud detection system designed to predict fraudulent transactions with high accuracy and speed by analyzing various customer and transaction-related parameters.

## 🎯 Objective
To build a robust and scalable model that detects fraudulent transactions in real-time with high accuracy.

---

## 📊 Dataset Description
**Source:** The dataset was generated using Python libraries such as Pandas, NumPy, and Random to simulate realistic Indian financial transactions.

| **Feature**             | **Description**                                         | **Type**    |
|-------------------------|---------------------------------------------------------|---------------|
| `Customer_ID`            | Unique identifier for each customer                    | String         |
| `Customer_Name`          | Fictional names for customer records                    | String         |
| `Gender`                 | Gender of the customer (M/F)                            | Categorical    |
| `Age`                    | Age of the customer (18-65)                             | Numerical      |
| `State`                  | State in India where the customer resides               | Categorical    |
| `City`                   | City where the transaction occurred                     | Categorical    |
| `Bank_Branch`            | Branch handling the transaction                         | Categorical    |
| `Account_Type`           | Savings or Current account                               | Categorical    |
| `Transaction_Device`     | Device used for the transaction                         | Categorical    |
| `Device_Type`            | Device operating system (Android, iOS, etc.)            | Categorical    |
| `Merchant_Category`      | Category of purchase (Electronics, Clothing, etc.)       | Categorical    |
| `Transaction_Location`   | City where the transaction occurred                     | Categorical    |
| `Transaction_Amount`     | Amount involved in the transaction                       | Numerical      |
| `Account_Balance`        | Balance in the customer's account                        | Numerical      |
| `Transaction_Date`       | Date of transaction (2023-2024)                          | Date           |
| `Time_of_Day`            | Period when the transaction occurred (Morning, Afternoon, Evening, Night) | Categorical    |
| `Fraud_Label`            | Indicator of fraudulent transactions (0 = Not Fraud, 1 = Fraud) | Binary     |

---

## 🛠️ Tools and Libraries Used
- **Python 3.11** for data processing and model implementation
- **Pandas** for data cleaning and manipulation
- **NumPy** for numerical operations
- **Scikit-learn** for model training and evaluation
- **Joblib** for model saving and loading
- **Streamlit** for building the interactive web application

---

## 🔍 Data Preprocessing Techniques Applied
✅ **Handling Missing Values:** Missing values were filled using mean, median, or mode depending on the data type.  
✅ **Encoding Categorical Variables:** The `LabelEncoder()` from `sklearn.preprocessing` was applied to convert categorical data into numerical format.  
✅ **Feature Engineering:**
- `Time_of_Day` was derived from `Transaction_Date` to capture transaction patterns.
- `Transaction_Amount` was normalized to improve model convergence.

---

## 🚀 Model Selection and Implementation
### **Chosen Model:** Random Forest Classifier
**Reason for Selection:**
- Handles both categorical and numerical data efficiently
- Provides excellent performance on tabular data
- Reduces overfitting with ensemble learning

### **Steps Implemented:**
1. Data split into training (80%) and testing (20%) sets.
2. Random Forest model trained with optimized hyperparameters.
3. Model evaluated using accuracy, precision, recall, and F1-score.
4. Predictions displayed with fraud indicators.

---

## 📈 Results and Insights
**Performance Metrics:**
- **Accuracy:** 94.5%
- **Precision:** 92%
- **Recall:** 89%
- **F1-Score:** 90.5%

**Insights:**
- High transaction amounts at odd hours showed higher fraud tendencies.
- Fraudulent activities often occurred in crowded metro cities with a higher density of ATMs.
- Transactions with unknown devices posed a higher fraud risk.

---

## 💡 Solutions and Recommendations
✅ Real-time alerts for suspicious transactions exceeding a predefined threshold.  
✅ Implement dynamic spending limits based on customer behavior.  
✅ Develop a user-specific risk profile using behavioral analytics.  

---

## 🔮 Future Enhancements
- Incorporate Deep Learning models like LSTM for improved sequential pattern recognition.
- Enhance the dataset with more real-world variables such as IP address, device fingerprinting, and user behavior logs.
- Implement a self-learning model that adapts to evolving fraud techniques.

---

## 📚 References
1. [Pandas Documentation](https://pandas.pydata.org/)  
2. [NumPy Documentation](https://numpy.org/)  
3. [Scikit-learn Documentation](https://scikit-learn.org/)  
4. [Streamlit Documentation](https://streamlit.io/)  

---

## 👨‍💻 Developed By
**Anirudh Sharma** and **Shivanshu Saini**