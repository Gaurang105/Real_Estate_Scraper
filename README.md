
# Property Scraper

This is a Python-based web scraper that extracts property information from the Delhi Government's [E-Search Portal](https://esearch.delhigovt.nic.in/Complete_search.aspx). The application uses Selenium and BeautifulSoup4 for web scraping and pandas for data manipulation.

The scraper retrieves data for a list of localities, specified by the user, and exports the data to an Excel file.


## Features

- Scrape property data for multiple localities
- Navigate through multiple pages of search results
- Extracts and combines data into a pandas DataFrame
- Exports the scraped data to an Excel file


## Requirements

 - Python 3.6+
- Selenium
- BeautifulSoup4
- Pandas
- Pillow
## Usage

1. Modify the main() function in scraper.py to include your desired localities, Sub Registrar Office (SRO), and year:
```bash
localities = ['Abul Fazal Enclave*', 'Adarsh Nagar*', 'Ahata kidara*', 'Ajmal Khan Road', 'Ajmeri Gate']
sro = "Central -Asaf Ali (SR III)"
year = "2021-2022"
```

2. Run the script:
```bash
python scraper.py
```

3. When prompted, enter the captcha text displayed in the opened image. This will be required for each locality in the list.

4. The script will scrape the data for each locality and save the combined data to an Excel file (property_data.xlsx) in the current directory.
