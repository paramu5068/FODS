import numpy as np
import scipy.stats as stats

# Sample data (replace with your actual data)
drug_group = [12, 10, 14, 13, 15, 11, 9, 10, 13, 14, 12, 11, 13, 12, 10, 11, 14, 13, 12, 10, 15, 14, 13, 12, 11]
placebo_group = [5, 6, 4, 5, 5, 6, 4, 3, 6, 5, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 4, 5, 6, 4, 5]

# Function to compute 95% CI
def compute_ci(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)
    t_value = stats.t.ppf((1 + confidence) / 2, df=n - 1)
    margin_of_error = t_value * (std_dev / np.sqrt(n))
    return (mean - margin_of_error, mean + margin_of_error)

# Compute and print CIs
ci_drug = compute_ci(drug_group)
ci_placebo = compute_ci(placebo_group)

print("95% Confidence Interval for Drug Group:", ci_drug)
print("95% Confidence Interval for Placebo Group:", ci_placebo)
