# AMFI India Mutual Fund Distributor Data Extractor

This Python script is designed to extract data about mutual fund distributors from the Association of Mutual Funds in India (AMFI) website. It performs the following tasks:

1. Retrieves a list of cities where mutual fund distributors are located from the AMFI India website.
2. For each city, retrieves data about mutual fund distributors, including their names, addresses, and other details.
3. Writes the extracted data to an Excel file.

## Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- requests
- beautifulsoup4
- pandas
- lxml

You can install these libraries using pip:

```bash
pip install requests beautifulsoup4 pandas lxml
```

## Usage

1. Clone this repository to your local machine or download the script.
2. Make sure you have the required libraries installed.
3. Run the script using the following command:

```bash
python amfi_india_extractor.py
```

## Output

The script will generate an Excel file named `output.xlsx`, containing the extracted data about mutual fund distributors. Each row in the Excel file represents a different distributor, with details such as name, address, city, and more.

## Note

- The script uses multithreading to improve efficiency. You can adjust the number of threads by modifying the `max_workers` parameter in the `ThreadPoolExecutor` instance.
- The extraction process may take some time depending on the number of cities and distributors listed on the AMFI India website.

Please be respectful of website terms of use and API usage policies when using this script for data extraction.
