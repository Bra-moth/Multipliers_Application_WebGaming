import random
import csv


# Number of rounds to simulate
num_rounds = 1000  # You can change this to your desired number of rounds

# Generate random multipliers and store them in a list
multipliers = [random.uniform(1.0, 10.0) for _ in range(num_rounds)]

# Create a CSV file and write the data to it
with open('multipliers.csv', 'w', newline='') as csvfile:
    fieldnames = ['Round', 'Multiplier']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i, multiplier in enumerate(multipliers, start=1):
        writer.writerow({'Round': i, 'Multiplier': multiplier})

print(f'{num_rounds} multipliers have been saved to multipliers.csv.')





