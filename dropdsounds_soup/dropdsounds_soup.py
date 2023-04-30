import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin


class DropdsoundsScraperItem:
    def __init__(self, title, price, picture_href):
        self.title = title
        self.price = price
        self.picture_href = picture_href

    def __repr__(self):
        return f"<DropdsoundsScraperItem title={self.title}, price={self.price}, picture_href={self.picture_href}>"


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


def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    items = []
    for product in soup.select(".product-container"):
        title = product.select_one(".product-name").text.strip()
        price = product.select_one(".price.product-price").text.strip()
        picture_href = product.select_one(".product-image-container img")["src"]
        item = DropdsoundsScraperItem(title, price, picture_href)
        items.append(item)
    return items


def get_next_page(soup):
    next_page_link = soup.select_one(".pagination a[rel='next']")
    if next_page_link:
        return next_page_link["href"]
    else:
        return None


def item_to_dict(item):
    return {
        "title": item.title,
        "price": item.price,
        "picture_href": item.picture_href,
    }


output_file = "dropdsounds_output.json"
output_items = []

for category in categories:
    url = urljoin(base_url, category)
    while url:
        html = fetch_page(url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            items = parse(html)
            for item in items:
                print(item)
                output_items.append(item_to_dict(item))
            next_page = get_next_page(soup)
            if next_page:
                url = urljoin(base_url, next_page)
            else:
                url = None
        else:
            print(f"Failed to fetch {url}")
            break

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)
