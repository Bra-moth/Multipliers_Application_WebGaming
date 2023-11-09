import pandas as pd

# Load A/B testing data
data = pd.read_csv('ab_test_data.csv')

# Calculate and compare conversion rates for versions A and B
conversion_rate_A = data[data['Version'] == 'A']['Converted'].mean()
conversion_rate_B = data[data['Version'] == 'B']['Converted'].mean()

print(f"Conversion Rate for Version A: {conversion_rate_A}")
print(f"Conversion Rate for Version B: {conversion_rate_B}")

# Perform a statistical test (e.g., t-test) to determine if the difference is significant
