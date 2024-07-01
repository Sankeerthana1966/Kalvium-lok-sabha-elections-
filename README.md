# Lok Sabha Election Results Analysis

## Description
This repository contains the analysis of the recently concluded Lok Sabha elections. The data was scraped from [Election Commission of India](https://results.eci.gov.in) and analyzed to derive key insights.

## Instructions
1. Clone the repository.
2. Run `scrape_election_results.py` to fetch the latest data.
3. Run `analyze_results.py` to perform data analysis and generate visualizations.
4. Run `generate_report.py` to create the final report.

## Project Structure
- `data/`: Contains the raw and processed data files.
- `notebooks/`: Contains Jupyter notebooks for exploratory analysis.
- `reports/`: Contains the final report and visualizations.
- `scrape_election_results.py`: Script to scrape election results.
- `analyze_results.py`: Script to analyze the results.
- `generate_report.py`: Script to generate the final report.
- `README.md`: Project overview and instructions.

## Setup
1. Ensure you have Python 3.6+ installed.
2. Install required packages:
    ```sh
    pip install selenium pandas matplotlib
    ```
3. Ensure you have ChromeDriver installed and it is in your PATH.

## Running the Scripts
1. Scrape the election results:
    ```sh
    python scrape_election_results.py
    ```
2. Analyze the results and generate visualizations:
    ```sh
    python analyze_results.py
    ```
3. Generate the final report:
    ```sh
    python generate_report.py
    ```

## Viewing the Report
Open the `reports/report.md` file to view the detailed analysis and insights.