import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Step 1: Load data
df = pd.read_csv("clinical_trial_data.csv")

# Step 2: Split into groups
control = df[df['group'] == 'control']['outcome']
treatment = df[df['group'] == 'treatment']['outcome']

# Step 3: Perform independent t-test
t_stat, p_value = stats.ttest_ind(treatment, control, equal_var=False)

# Step 4: Interpret result
alpha = 0.05
print(f"P-value: {p_value:.4f}")
if p_value < alpha:
    print("✅ Statistically significant difference: Treatment is effective.")
else:
    print("❌ No statistically significant difference found.")

# Step 5: Visualization
group_means = [control.mean(), treatment.mean()]
group_labels = ['Control', 'Treatment']

plt.bar(group_labels, group_means, color=['gray', 'green'])
plt.title(f"Group Means Comparison (p-value = {p_value:.4f})")
plt.ylabel("Mean Outcome")
plt.ylim(min(group_means)-1, max(group_means)+1)
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.show()
