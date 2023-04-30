Dropdsounds Scraper using Beautiful Soup

This script scrapes product information from effects section of the Dropdsounds website (https://www.dropdsounds.com/en/) using Beautiful Soup and the requests library. The scraped data is saved to a JSON file named dropdsounds_output.json.

Requirements
Python 3.6 or higher
beautifulsoup4
requests
You can install the required packages using pip:

`pip install beautifulsoup4 requests`

To run the script you can call in from terminal:

`python dropdsounds_scraper.py`

The script will start fetching and parsing data from the Dropdsounds website. As the script runs, you'll see the extracted items being printed to the console.

Once the script is finished, you'll find a file named dropdsounds_scraper_output.json in the same directory as the script. This file contains the scraped product information in JSON format.

####Output

The output JSON file will contain a list of dictionaries, each representing a product. Each dictionary has the following keys:

1. title: The product's title.

2. price: The product's price, including the Euro sign (€).

3. picture_href: The URL of the product's image.

The script may take a few minutes to complete, depending on the number of categories and pages to be fetched.


