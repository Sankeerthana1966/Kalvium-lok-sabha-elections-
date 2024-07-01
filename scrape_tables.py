import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Election Commission of India results page
url = "https://results.eci.gov.in/"

# Send a request to fetch the content of the webpage
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all tables in the webpage
tables = soup.find_all('table')

# Loop through all the tables and convert them into DataFrames
for i, table in enumerate(tables):
    # Extract table headers
    headers = []
    for th in table.find_all('th'):
        headers.append(th.text.strip())

    # Extract table rows
    rows = []
    for tr in table.find_all('tr'):
        cells = tr.find_all('td')
        if len(cells) > 0:
            row = [cell.text.strip() for cell in cells]
            rows.append(row)

    # Create a DataFrame
    df = pd.DataFrame(rows, columns=headers)

    # Save the DataFrame to a CSV file
    df.to_csv(f'table_{i}.csv', index=False)

    # Print the DataFrame (for demonstration purposes)
    print(f"Table {i}:")
    print(df)
    print("\n")

print("Tables have been successfully recognized and saved as CSV files.")