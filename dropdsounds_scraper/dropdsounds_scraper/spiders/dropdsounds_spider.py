# Author: Maksim Gorozhanko

import scrapy
from ..items import DropdsoundsScraperItem


class DropdsoundsSpider(scrapy.Spider):
    name = "dropdsounds"
    allowed_domains = ["dropdsounds.com"]

    def start_requests(self):
        base_url = "https://www.dropdsounds.com/en/"
        categories = [
            "overdrive",
            "distortion",
            "fuzz",
            "booster",
            "delay",
            "reverb",
            "looper",
            "chorus-vibrato",
            "flanger",
            "phaser",
            "tremolo",
            "vibe",
            "envelope-filter",
            "rotary-organ",
            "octave-pitch-shifter",
            "synth-pedals",
            "compressor",
            "equalizer-eq",
            "wah-wah",
            "misc-effects",
            "multi-effects",
            "bass-effects",
            "volume",
            "expression-pedals",
            "noise-reduction",
            "guitar-tuners",
            "vocal-effects",
            "drum-machines",
            "acoustic-effects",
            "eurorackmodular-effects",
            "footswitches",
            "footswitches",
        ]
        urls = [base_url + category for category in categories]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        for product in response.css(".product-container"):
            item = DropdsoundsScraperItem()
            item["title"] = product.css(".product-name::text").get().strip()
            item["price"] = product.css(".price.product-price::text").get().strip()
            item["picture_href"] = product.css(".product-image-container img::attr(src)").get()
            yield item

        # Pagination
        next_page = response.css(".pagination a[rel='next']::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
