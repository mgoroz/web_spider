# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DropdsoundsScraperItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    picture_href = scrapy.Field()
