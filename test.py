import pandas as pd
import random
import numpy as np
from faker import Faker

fake = Faker('en_IN')

# Sample data generation
data = []

for _ in range(100):
    customer_id = fake.uuid4()
    customer_name = fake.name()
    gender = random.choice(['Male', 'Female'])
    age = random.randint(18, 70)
    state = random.choice(['Delhi', 'Maharashtra', 'Karnataka', 'Tamil Nadu', 'West Bengal'])
    city = random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata'])
    bank_branch = fake.company()
    account_type = random.choice(['Savings', 'Current'])
    transaction_id = fake.uuid4()
    transaction_date = fake.date_this_year().strftime('%Y-%m-%d')
    transaction_time = fake.time()
    transaction_amount = round(random.uniform(500, 100000), 2)
    merchant_id = fake.uuid4()
    transaction_type = random.choice(['Online', 'POS', 'ATM'])
    merchant_category = random.choice(['Grocery', 'Electronics', 'Fashion', 'Entertainment'])
    account_balance = round(random.uniform(1000, 200000), 2)
    transaction_device = random.choice(['Mobile', 'Laptop', 'ATM'])
    transaction_location = city
    device_type = random.choice(['Android', 'iOS', 'Windows']),
    transaction_currency = 'INR'
    customer_contact = fake.phone_number()

    data.append([customer_id, customer_name, gender, age, state, city, bank_branch,
                 account_type, transaction_id, transaction_date, transaction_time,
                 transaction_amount, merchant_id, transaction_type, merchant_category,
                 account_balance, transaction_device, transaction_location,
                 device_type, transaction_currency, customer_contact])

# DataFrame creation
df = pd.DataFrame(data, columns=[
    'Customer_ID', 'Customer_Name', 'Gender', 'Age', 'State', 'City', 'Bank_Branch',
    'Account_Type', 'Transaction_ID', 'Transaction_Date', 'Transaction_Time',
    'Transaction_Amount', 'Merchant_ID', 'Transaction_Type', 'Merchant_Category',
    'Account_Balance', 'Transaction_Device', 'Transaction_Location', 'Device_Type',
    'Transaction_Currency', 'Customer_Contact'
])

# Save to CSV
df.to_csv('fraud_prediction_data.csv', index=False)

# Display sample data
df.head()
