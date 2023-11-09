import pandas as pd
import matplotlib.pyplot as plt

# Load player interaction data (replace 'player_data.csv' with your dataset)
data = pd.read_csv('player_data.csv')

# Display the first few rows of the data to get an overview
print(data.head())

# Basic player statistics
total_players = data['Player_ID'].nunique()
total_bets = data['Bet'].sum()
total_wins = data['Win'].sum()
total_losses = data['Loss'].sum()

print(f'Total Players: {total_players}')
print(f'Total Bets: ${total_bets}')
print(f'Total Wins: ${total_wins}')
print(f'Total Losses: ${total_losses}')

# Player behavior analysis and visualization
# Example: Creating a histogram of player bets
plt.hist(data['Bet'], bins=20, color='blue', alpha=0.7)
plt.xlabel('Bet Amount')
plt.ylabel('Frequency')
plt.title('Distribution of Player Bets')
plt.show()

# Example: Creating a bar chart of the most popular games
popular_games = data['Game_Name'].value_counts().head(10)
popular_games.plot(kind='bar', color='green', alpha=0.7)
plt.xlabel('Game Name')
plt.ylabel('Number of Plays')
plt.title('Most Popular Games')
plt.show()
