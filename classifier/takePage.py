import requests as rq
from bs4 import BeautifulSoup

headers = {'user-agent': 'Rodrigo'};
url = 'http://store.steampowered.com/app/734580/BattleRush/';
r = rq.get(url, headers=headers);
page = BeautifulSoup(r.text, "html.parser");

with open("steam/positivePages/page4.html", "w") as file:
    file.write(str(page));