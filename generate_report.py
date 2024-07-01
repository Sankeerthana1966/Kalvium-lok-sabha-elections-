import pandas as pd

# Load analysis results
total_seats_won = pd.read_csv('data/total_seats_won.csv')
vote_shares = pd.read_csv('data/vote_shares.csv')

# Generate markdown report
with open('reports/report.md', 'w') as f:
    f.write("# Lok Sabha Election Results Report\n\n")

    f.write("## Key Insights\n\n")

    f.write("1. **Total Seats Won by Each Party**:\n")
    f.write("![Total Seats Won by Each Party](total_seats_won.png)\n")
    f.write(total_seats_won.to_markdown(index=False) + "\n\n")

    f.write("2. **Vote Share Percentage by Party**:\n")
    f.write("![Vote Share Percentage by Party](vote_share_percentage.png)\n")
    f.write(vote_shares.to_markdown(index=False) + "\n\n")

    f.write("[... additional insights ...]\n\n")

    f.write("## Conclusion\n")
    f.write("[Summary of findings and implications]\n")