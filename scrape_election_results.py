from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL for the Lok Sabha election results
url = "https://results.eci.gov.in"

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Access the URL
    driver.get(url)
    logging.info(f"Accessed URL: {url}")

    # Wait for the tables to be present on the page
    tables = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.XPATH, '//table[contains(@class, "table-party") or contains(@id, "div1") or contains(@id, "dataTable")]'))
    )
    logging.info(f"Found {len(tables)} tables on the page.")

    for idx, table in enumerate(tables):
        # Extract headers from the table
        headers = [header.text.strip() for header in table.find_elements(By.TAG_NAME, 'th')]
        
        rows = []
        for row in table.find_elements(By.TAG_NAME, 'tr')[1:]:
            cells = row.find_elements(By.TAG_NAME, 'td')
            row_data = [cell.text.strip() for cell in cells]
            rows.append(row_data)

        # Create DataFrame and save to CSV
        df = pd.DataFrame(rows, columns=headers)
        csv_filename = f'election_results_table_{idx+1}.csv'
        df.to_csv(csv_filename, index=False)
        logging.info(f"Saved table {idx+1} to {csv_filename}")

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
finally:
    # Close the WebDriver
    driver.quit()
    logging.info("Closed the web driver.")

