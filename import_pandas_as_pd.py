import pandas as pd

# Load data from the CSV file
data = pd.read_csv('multipliers.csv')

# Display the first few rows of the data
print(data.head())

# Summary statistics
print(data.describe())
