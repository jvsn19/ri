from bs4 import BeautifulSoup
import requests

def trade_spider(max_pages = 2):
    current_page = 1
    while current_page <= max_pages:
        url = 'http://store.steampowered.com/search?page=' + str(current_page)
        source_code = requests.get(url)
        plain_text = source_code.text
        current_page += 1

trade_spider()