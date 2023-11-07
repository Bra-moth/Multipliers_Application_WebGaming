import matplotlib.pyplot as plt
import numpy as np

# Assuming you have a dataclass_transform class with a Multiplier attribute
class dataclass_transform:
    Multiplier = np.random.randint(1, 100, 1000)

# Create a histogram of multipliers
plt.hist(dataclass_transform.Multiplier, bins=20, color='blue', alpha=0.7)
plt.xlabel('Multiplier')
plt.ylabel('Frequency')
plt.title('Distribution of Multipliers')
plt.show()

# Create a scatter plot of round number vs. multiplier
plt.scatter(range(1, 1001), dataclass_transform.Multiplier, color='green', alpha=0.5)
plt.xlabel('Round')
plt.ylabel('Multiplier')
plt.title('Round vs. Multiplier')
plt.show()

# Assuming you have a function to save the multipliers to a csv file
#save_to_csv(dataclass_transform.Multiplier, 'multipliers.csv')