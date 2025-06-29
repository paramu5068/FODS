# Step 1: Import the matplotlib library
import matplotlib.pyplot as plt

# Step 2: Define the data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [1200, 1500, 1700, 1600, 1800, 2000]

# Step 3: Create a line plot
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker='o', color='blue', linestyle='-')
plt.title('Monthly Sales - Line Plot')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 4: Create a bar plot
plt.figure(figsize=(8, 5))
plt.bar(months, sales, color='orange')
plt.title('Monthly Sales - Bar Plot')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
