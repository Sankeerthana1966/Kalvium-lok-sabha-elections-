import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the election results data
df = pd.read_csv('election_results.csv')

# Ensure the 'reports' folder exists
import os
if not os.path.exists('reports'):
    os.makedirs('reports')

# Total Seats Won by Each Party
party_seats = df['Party'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=party_seats.values, y=party_seats.index, palette='viridis')
plt.title('Total Seats Won by Each Party')
plt.xlabel('Number of Seats')
plt.ylabel('Party')
plt.savefig('reports/total_seats_won.png')
plt.close()

# Vote Share Percentage by Party
party_votes = df.groupby('Party')['Votes'].sum()
party_votes_percentage = (party_votes / party_votes.sum()) * 100
plt.figure(figsize=(10, 6))
plt.pie(party_votes_percentage, labels=party_votes_percentage.index, autopct='%1.1f%%', colors=sns.color_palette('viridis', len(party_votes_percentage)))
plt.title('Vote Share Percentage by Party')
plt.savefig('reports/vote_share_percentage.png')
plt.close()