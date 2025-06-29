import numpy as np
import pandas as pd
from scipy import stats

# Load data
data = pd.read_csv("C:\Users\nasri\OneDrive\Documents\heart.csv")
concentrations = data.iloc[:, 0].dropna().values  # Assuming single column of data

# User inputs
sample_size = int(input("Enter the sample size: "))
confidence_level = float(input("Enter the confidence level (e.g., 95 for 95%): ")) / 100
precision = float(input("Enter the desired margin of error (precision): "))

# Random sample
if sample_size > len(concentrations):
    raise ValueError("Sample size cannot exceed the number of available data points.")

sample = np.random.choice(concentrations, size=sample_size, replace=False)

# Point estimate
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)  # Sample standard deviation

# Confidence interval
z_score = stats.norm.ppf(1 - (1 - confidence_level) / 2)
margin_of_error = z_score * (sample_std / np.sqrt(sample_size))

# Compare with desired precision
if margin_of_error <= precision:
    print("✅ The desired level of precision is achieved.")
else:
    print("⚠️ The desired level of precision is NOT achieved. Consider increasing the sample size.")

# Output results
print(f"\nSample Mean: {sample_mean:.4f}")
print(f"Confidence Interval ({int(confidence_level * 100)}%): [{sample_mean - margin_of_error:.4f}, {sample_mean + margin_of_error:.4f}]")
print(f"Margin of Error: {margin_of_error:.4f}")
