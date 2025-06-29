from statsmodels.stats.proportion import proportions_ztest

# Sample data (replace with actual numbers)
conversions = [200, 250]     # x₁, x₂
sample_sizes = [2400, 2450]  # n₁, n₂

# Perform two-proportion z-test
z_stat, p_val = proportions_ztest(count=conversions, nobs=sample_sizes)

print(f"Z-statistic: {z_stat:.4f}")
print(f"P-value: {p_val:.4f}")

# Decision
alpha = 0.05
if p_val < alpha:
    print("Reject the null hypothesis: Statistically significant difference in conversion rates.")
else:
    print("Fail to reject the null hypothesis: No statistically significant difference found.")

