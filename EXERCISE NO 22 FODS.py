import pandas as pd
import numpy as np
from scipy import stats

# Load the dataset
df = pd.read_csv("customer_reviews.csv")

# Extract ratings from the 'Mobile Phones' category
ratings = df[df['category'] == 'Mobile Phones']['rating'].dropna()

# Calculate statistics
sample_mean = np.mean(ratings)
sample_std = np.std(ratings, ddof=1)
n = len(ratings)

# Confidence level
confidence_level = 0.95
alpha = 1 - confidence_level
t_crit = stats.t.ppf(1 - alpha/2, df=n-1)

# Margin of Error
margin_error = t_crit * (sample_std / np.sqrt(n))

# Confidence Interval
lower = sample_mean - margin_error
upper = sample_mean + margin_error

# Output
print(f"Sample Mean Rating: {sample_mean:.2f}")
print(f"95% Confidence Interval: [{lower:.2f}, {upper:.2f}]")
