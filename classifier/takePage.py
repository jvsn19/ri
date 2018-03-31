import requests as rq
from bs4 import BeautifulSoup

headers = {'user-agent': 'Rodrigo'};
url = 'http://store.steampowered.com/app/601050/Attack_on_Titan_2__AOT2/';
r = rq.get(url, headers=headers);
page = BeautifulSoup(r.text, "html.parser");

with open("steam/positivePages/page10.html", "w") as file:
    file.write(str(page));