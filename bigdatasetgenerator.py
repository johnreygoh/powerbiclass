import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)

# Number of rows
n_rows = 200_000

# Function to generate random dates within a range
def generate_dates(start_date, end_date, n):
    time_between_dates = (end_date - start_date).days
    random_number_of_days = np.random.randint(0, time_between_dates, n)
    return [start_date + timedelta(days=int(x)) for x in random_number_of_days]

# Create start and end dates for different date columns
start_date = datetime(2021, 1, 1)
end_date = datetime(2023, 12, 31)

# Lists for categorical data generation
product_categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books', 'Beauty', 'Automotive']
product_subcategories = {
    'Electronics': ['Smartphones', 'Laptops', 'Tablets', 'Accessories'],
    'Clothing': ['Men', 'Women', 'Children', 'Accessories'],
    'Home & Garden': ['Furniture', 'Decor', 'Kitchen', 'Gardening'],
    'Sports': ['Equipment', 'Clothing', 'Footwear', 'Accessories'],
    'Books': ['Fiction', 'Non-Fiction', 'Academic', 'Children'],
    'Beauty': ['Skincare', 'Makeup', 'Haircare', 'Fragrances'],
    'Automotive': ['Parts', 'Accessories', 'Tools', 'Electronics']
}
payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Cash']
shipping_methods = ['Standard', 'Express', 'Next Day', 'Two-Day']
regions = ['North', 'South', 'East', 'West', 'Central']
customer_segments = ['Individual', 'Small Business', 'Enterprise', 'Wholesale']
sales_channels = ['Online', 'In-Store', 'Mobile App', 'Telephone']
order_statuses = ['Completed', 'Shipped', 'Processing', 'Returned', 'Cancelled']
genders = ['Male', 'Female', 'Other']
income_ranges = ['Low', 'Medium', 'High', 'Very High']

# Countries and states
countries = ['United States', 'Canada']
us_states = ['CA', 'NY', 'TX', 'FL', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI']
canadian_provinces = ['ON', 'QC', 'BC', 'AB', 'MB']

# Generate data
data = {
    'Transaction_ID': range(1, n_rows + 1),
    'Transaction_Date': generate_dates(start_date, end_date, n_rows),
    'Shipping_Date': [],
    'Order_Created_Date': [],
    'Return_Date': [],
    'Payment_Date': [],
    'Customer_ID': np.random.randint(1, 50000, n_rows),
    'Product_ID': np.random.randint(1, 10000, n_rows),
    'Product_Category': [],
    'Product_Subcategory': [],
    'Unit_Price': np.round(np.random.uniform(10, 1000, n_rows), 2),
    'Quantity': np.random.randint(1, 10, n_rows),
    'Discount': np.round(np.random.uniform(0, 0.3, n_rows), 2),
    'Total_Amount': [],  # Added this line
    'Payment_Method': [],
    'Shipping_Method': [],
    'Region': [],
    'City': [],
    'State': [],
    'Country': [],
    'Postal_Code': [],
    'Customer_Segment': [],
    'Order_Status': [],
    'Sales_Channel': [],
    'Promo_Code_Used': np.random.choice([True, False], n_rows),
    'Cost_of_Goods_Sold': [],
    'Profit': [],
    'Tax_Amount': [],
    'Shipping_Cost': np.round(np.random.uniform(0, 50, n_rows), 2),
    'Net_Profit': [],
    'Order_Rating': np.random.randint(1, 6, n_rows),
    'Product_Rating': np.random.randint(1, 6, n_rows),
    'Vendor_ID': np.random.randint(1, 500, n_rows),
    'Warehouse_ID': np.random.randint(1, 50, n_rows),
    'Stock_Availability': np.random.randint(0, 1000, n_rows),
    'Customer_Age': np.random.randint(18, 80, n_rows),
    'Customer_Gender': [],
    'Customer_Income_Range': [],
    'Loyalty_Points_Earned': np.random.randint(0, 1000, n_rows),
    'Customer_Feedback': []
}

# Populate complex columns
for i in range(n_rows):
    # Date calculations
    trans_date = data['Transaction_Date'][i]
    data['Order_Created_Date'].append(trans_date - timedelta(days=np.random.randint(0, 5)))
    data['Shipping_Date'].append(trans_date + timedelta(days=np.random.randint(1, 7)))
    
    # Randomly generate Return_Date for some transactions
    data['Return_Date'].append(trans_date + timedelta(days=np.random.randint(7, 30)) if np.random.random() < 0.1 else None)
    data['Payment_Date'].append(trans_date)
    
    # Category selections
    category = np.random.choice(product_categories)
    data['Product_Category'].append(category)
    data['Product_Subcategory'].append(np.random.choice(product_subcategories[category]))
    
    # Other categorical columns
    data['Payment_Method'].append(np.random.choice(payment_methods))
    data['Shipping_Method'].append(np.random.choice(shipping_methods))
    data['Region'].append(np.random.choice(regions))
    data['Customer_Segment'].append(np.random.choice(customer_segments))
    data['Order_Status'].append(np.random.choice(order_statuses))
    data['Sales_Channel'].append(np.random.choice(sales_channels))
    data['Customer_Gender'].append(np.random.choice(genders))
    data['Customer_Income_Range'].append(np.random.choice(income_ranges))
    
    # Geographic data
    country = np.random.choice(countries)
    data['Country'].append(country)
    
    if country == 'United States':
        state = np.random.choice(us_states)
        postal_code = f"{state}{np.random.randint(10000, 99999)}"
    else:
        state = np.random.choice(canadian_provinces)
        postal_code = f"{state}{np.random.randint(100, 999)}"
    
    data['State'].append(state)
    data['Postal_Code'].append(postal_code)
    
    # City generation (simplified)
    data['City'].append(f"{state} City")
    
    # Financial calculations
    unit_price = data['Unit_Price'][i]
    quantity = data['Quantity'][i]
    discount = data['Discount'][i]
    
    total_amount = unit_price * quantity * (1 - discount)
    cost_of_goods = total_amount * 0.6  # Assuming 40% gross margin
    profit = total_amount - cost_of_goods
    tax_amount = total_amount * 0.08  # 8% tax rate
    
    data['Total_Amount'].append(total_amount)
    data['Cost_of_Goods_Sold'].append(cost_of_goods)
    data['Profit'].append(profit)
    data['Tax_Amount'].append(tax_amount)
    data['Net_Profit'].append(profit - data['Shipping_Cost'][i] - tax_amount)
    
    # Customer Feedback generation
    feedback_options = ['Great Product', 'Satisfied', 'Needs Improvement', 'Poor Quality', 'Excellent Service']
    data['Customer_Feedback'].append(np.random.choice(feedback_options))

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert date columns to datetime
date_columns = ['Transaction_Date', 'Shipping_Date', 'Order_Created_Date', 'Return_Date', 'Payment_Date']
for col in date_columns:
    df[col] = pd.to_datetime(df[col])

# Display basic info and first few rows
print(df.info())
print("\nFirst few rows:\n", df.head())

# Optional: Save to CSV
df.to_csv('sales_transactions.csv', index=False)
print("\nDataset saved to sales_transactions.csv")