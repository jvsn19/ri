import requests
from bs4 import BeautifulSoup
import re

class Steam_Spider():
    def __init__(self, basic_url):
        self.__basic_url = basic_url
        self.__game_regex = re.compile("^http://store.steampowered.com/app/.*/[^?]+") #Catch only games' url
    
    def search_pages(self, deep = 2):
        # Get all content of a search page. From here we must navigate through all items on this and get the useful
        # attrs: name, price, review, etc.
        curr_page = 1
        url = self.__basic_url
        urls = set()
        while curr_page <= deep:
            curr_url = url + str(curr_page)
            curr_html = requests.get(curr_url) # The page will be incremented until reaches the maximum deep
            curr_html_text = curr_html.text
            soup = BeautifulSoup(curr_html_text, "html.parser")
            for game in soup.findAll('a', {'href': self.__game_regex}):
                game_url = game.get('href')
                urls.add(game_url)
            curr_page += 1
        self.download_pages(urls)
        

    def get_page_attributes(self, urls):
        pass

    def download_pages(self, urls):
        regex_game = re.compile('/.+/')
        for url in urls:
            pattern = regex_game.search(url, 34).span() #34 is the first id position (ex: 2 from 244...)
            game_name = url[pattern[0]+1:pattern[1]-1].lower()
            game_page_file = open('pages/steam_' + game_name + '.html', 'wb')
            curr_html = requests.get(url)
            soup = BeautifulSoup(curr_html.text, 'html.parser')
            game_page_file.write(soup.encode('utf-8'))

spider = Steam_Spider("http://store.steampowered.com/search?page=")
spider.search_pages()