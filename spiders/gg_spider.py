import re
import requests
from bs4 import BeautifulSoup
from spiders.basic_spider import Spider

class GGSpider(Spider):
    def __init__(self, basicUrl, pageLimit, level):
        Spider.__init__(self, basicUrl, pageLimit, level)

    def _crawlPage(self, page):
        # Must override the Spider Method
        if not page in self._visited:
            self._visited.add(page) #Prevent revisiting this page
            self._pageCount -= 1
            #print(page)
            pageText = requests.get(page).text
            soupObject = BeautifulSoup(pageText, 'html.parser')
            self._downloadPage(soupObject)
            for link in soupObject.findAll('a', href = True): #Search every link on the current page
                href = link.get('href')
                if self._checkRegex(href) and not href in self._visited and self._pageCount >= 0:
                    hrefSoup = None
                    if self._level > 1:
                        hrefText = requests.get(href).text
                        hrefSoup = BeautifulSoup(hrefText, 'html.parser')
                    rank = self._getRank(hrefSoup, href, level = self._level)
                    print(self._basicUrl+href)
                    self._pageHeap.put_nowait((-rank, self._basicUrl+href))

    def _downloadPage(self, soupObject):
        path = open('pages/gg_' + str(self._pageCount) + '.html', 'wb')
        path.write(soupObject.encode('utf-8'))
        path.close()
    
    def _getRank(self, soupObject, url, level):
        ranking = 0
        if level == 1:
            urlRegex = re.compile('/games/')
            if re.search(urlRegex, url):
                ranking += 1
        return ranking

    def _cleanUrl(self, url):
        return url