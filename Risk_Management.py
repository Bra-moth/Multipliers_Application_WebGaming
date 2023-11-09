import pandas as pd

# Load player behavior data
data = pd.read_csv('player_behavior_data.csv')

# Identify players with unusually high losses
high_loss_players = data[data['Loss'] > data['Loss'].mean() + 2 * data['Loss'].std()]

print("Players with unusually high losses:")
print(high_loss_players)
