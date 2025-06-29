import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [25, 27, 30, 33, 35, 34, 32, 31, 30, 28, 26, 24]  # in °C
rainfall = [60, 50, 70, 120, 200, 250, 300, 270, 190, 100, 80, 65]  # in mm

# Line plot for temperature
plt.figure(figsize=(8, 4))
plt.plot(months, temperature, marker='o', color='red', linestyle='-')
plt.title('Monthly Temperature Line Plot')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Scatter plot for rainfall
plt.figure(figsize=(8, 4))
plt.scatter(months, rainfall, color='blue', s=80)
plt.title('Monthly Rainfall Scatter Plot')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.tight_layout()
plt.show()
