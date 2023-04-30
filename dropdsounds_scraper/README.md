### Author: Maksim Gorozhanko

#Dropdsounds Scraper using Scrapy

This script scrapes product information from the Dropdsounds website (https://www.dropdsounds.com/en/) using the Scrapy web scraping framework. The scraped data is saved to a JSON file named output_dropdsounds.json.

To initialize the project following command was used:  

`scrapy startproject dropdsounds_scraper`

Requirements
1. Python 3.6 or higher
2. 'scrapy'

Inside the dropdsounds_scraper directory, the content of the items.py file was replaced with initialization of class DropdsoundsScraperItem.

Inside the spiders directory of the project a new file named dropdsounds_spider.py was created.

settings.py was updated to output data in json in a separate file.

To run the scraper you should use:

`scrapy crawl dropdsounds`

The spider will start fetching and parsing data from the Dropdsounds website. As the spider runs, you'll see the progress and status messages being printed to the console.

Once the spider is finished, you'll find a file named output_dropdsounds.json in the project directory. This file contains the scraped product information in JSON format.

####Output
The output JSON file will contain a list of dictionaries, each representing a product. Each dictionary has the following keys:

1. title: The product's title.

2. price: The product's price, including the Euro sign (€).

3. picture_href: The URL of the product's image.
