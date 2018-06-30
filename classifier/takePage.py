import requests as rq
from bs4 import BeautifulSoup

headers = {'user-agent': 'Rodrigo'}
#url of the html page
url = 'https://store.steampowered.com/app/537800/Bomber_Crew/'
r = rq.get(url, headers=headers)
page = BeautifulSoup(r.text, "html.parser")

#Y = 'negative' or 'positive'
#X = number of the html page
# foldername = name of the site  
with open("sites/steam/positivePages/page3.html", "w") as file:
    file.write(str(page))
