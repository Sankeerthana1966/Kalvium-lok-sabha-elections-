import requests
from bs4 import BeautifulSoup
import csv

# URLs and their respective political parties
url_party_pairs = [
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-369.htm', 'BJP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-742.htm', 'INC'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1680.htm', 'SP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-140.htm', 'AITC'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-582.htm', 'DMK'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1745.htm', 'TDP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-805.htm', 'JD(U)'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3369.htm', 'SHSUBT'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3620.htm', 'NCPSP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3529.htm', 'SHS'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3165.htm', 'LJPRV'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1888.htm', 'YSRCP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1420.htm', 'RJD'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-547.htm', 'CPI(M)'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-772.htm', 'IUML'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1.htm', 'AAAP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-852.htm', 'JMM'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-860.htm', 'JNP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-545.htm', 'CPI(ML)(L)'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-804.htm', 'JD(S)'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1847.htm', 'VCK'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-544.htm', 'CPI'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1458.htm', 'RLD'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-834.htm', 'JKN'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1998.htm', 'UPPL'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-83.htm', 'AGP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-664.htm', 'HAMS'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-911.htm', 'KEC'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1534.htm', 'RSP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1142.htm', 'NCP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3388.htm', 'VOTPP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2757.htm', 'ZPM'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1584.htm', 'SAD'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2484.htm', 'RLTP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3482.htm', 'BHRTADVSIP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1658.htm', 'SKM'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1046.htm', 'MDMK'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2989.htm', 'ASPKR'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2070.htm', 'ADAL'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-160.htm', 'AJSUP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-118.htm', 'AIMIM'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-743.htm', 'IND')
]

# Function to fetch and parse HTML content
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Failed to retrieve {url}. Status code: {response.status_code}")
        return None

# Function to extract data from tables
def extract_table(soup, party):
    extracted_data = []
    if soup:
        tables = soup.find_all('table')
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                headers = row.find_all('th')
                cells = row.find_all('td')
                if headers:
                    header_texts = [header.get_text(strip=True) for header in headers]
                    header_texts.append("Party")
                    extracted_data.append(header_texts)
                else:
                    cell_texts = [cell.get_text(strip=True) for cell in cells]
                    cell_texts.append(party)
                    extracted_data.append(cell_texts)
    else:
        print("No data available for parsing.")
    return extracted_data

# Write data to CSV
csv_file_name = "election_results.csv"
headers_added = False

with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for url, party in url_party_pairs:
        page_soup = fetch_html(url)
        table_rows = extract_table(page_soup, party)
        
        for row in table_rows:
            if not headers_added:
                writer.writerow(row)
                headers_added = True
            else:
                if row[0] != table_rows[0][0]:  # Avoid duplicate headers
                    writer.writerow(row)

print(f"Election results have been saved to {csv_file_name}")

import requests
from bs4 import BeautifulSoup
import csv

# URLs and their respective political parties
url_party_pairs = [
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-369.htm', 'BJP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-742.htm', 'INC'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1680.htm', 'SP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-140.htm', 'AITC'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-582.htm', 'DMK'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1745.htm', 'TDP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-805.htm', 'JD(U)'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3369.htm', 'SHSUBT'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3620.htm', 'NCPSP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3529.htm', 'SHS'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3165.htm', 'LJPRV'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1888.htm', 'YSRCP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1420.htm', 'RJD'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-547.htm', 'CPI(M)'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-772.htm', 'IUML'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1.htm', 'AAAP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-852.htm', 'JMM'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-860.htm', 'JNP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-545.htm', 'CPI(ML)(L)'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-804.htm', 'JD(S)'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1847.htm', 'VCK'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-544.htm', 'CPI'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1458.htm', 'RLD'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-834.htm', 'JKN'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1998.htm', 'UPPL'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-83.htm', 'AGP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-664.htm', 'HAMS'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-911.htm', 'KEC'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1534.htm', 'RSP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1142.htm', 'NCP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3388.htm', 'VOTPP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2757.htm', 'ZPM'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1584.htm', 'SAD'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2484.htm', 'RLTP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3482.htm', 'BHRTADVSIP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1658.htm', 'SKM'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1046.htm', 'MDMK'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2989.htm', 'ASPKR'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2070.htm', 'ADAL'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-160.htm', 'AJSUP'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-118.htm', 'AIMIM'),
    ('https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-743.htm', 'IND')
]

# Function to fetch and parse HTML content
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Failed to retrieve {url}. Status code: {response.status_code}")
        return None

# Function to extract data from tables
def extract_table(soup, party):
    extracted_data = []
    if soup:
        tables = soup.find_all('table')
        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                headers = row.find_all('th')
                cells = row.find_all('td')
                if headers:
                    header_texts = [header.get_text(strip=True) for header in headers]
                    header_texts.append("Party")
                    extracted_data.append(header_texts)
                else:
                    cell_texts = [cell.get_text(strip=True) for cell in cells]
                    cell_texts.append(party)
                    extracted_data.append(cell_texts)
    else:
        print("No data available for parsing.")
    return extracted_data

# Write data to CSV
csv_file_name = "election_results.csv"
headers_added = False

with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for url, party in url_party_pairs:
        page_soup = fetch_html(url)
        table_rows = extract_table(page_soup, party)
        
        for row in table_rows:
            if not headers_added:
                writer.writerow(row)
                headers_added = True
            else:
                if row[0] != table_rows[0][0]:  # Avoid duplicate headers
                    writer.writerow(row)

print(f"Election results have been saved to {csv_file_name}")
