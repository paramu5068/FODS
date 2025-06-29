import pandas as pd

# Sample data (replace with your actual DataFrame)
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'age': [25, 30, 25, 40, 30, 25],
    'purchased': [True, False, True, True, False, True]
}

# Step 1: Create DataFrame
df = pd.DataFrame(data)

# Step 2: Filter only customers who made a purchase
purchased_customers = df[df['purchased'] == True]

# Step 3: Get frequency distribution of their ages
age_frequency = purchased_customers['age'].value_counts().sort_index()

# Step 4: Display the result
print("Frequency Distribution of Customer Ages:")
print(age_frequency)
