import requests
import re
from abc import ABCMeta, abstractmethod
from queue import PriorityQueue
from bs4 import BeautifulSoup

class Spider(metaclass = ABCMeta):
    def __init__(self, basicUrl, pageLimit, level):
        self._basicUrl = basicUrl
        self._urlRegex = re.compile(basicUrl)
        self._pageCount = pageLimit #A limit of pages
        self._pageHeap = PriorityQueue()
        self._visited = set()
        self._level = level

    def __searchPages(self, startPage):
        page = (0, startPage)
        self._pageHeap.put_nowait(page) #Inserting the first page to be crawled
        while not self._pageHeap.empty() and self._pageCount >= 0:
            _, currPage = self._pageHeap.get_nowait() #Get the current page. The first element of the 2-uple is useless here
            currPage = self.__cleanUrl(currPage)
            self.__crawlPage(currPage)

    def __crawlPage(self, page):
        #Put pages in the heap
        if not page in self._visited:
            self._visited.add(page) #Prevent revisiting this page
            self._pageCount -= 1
            print(page)
            pageText = requests.get(page).text
            soupObject = BeautifulSoup(pageText, 'html.parser')
            self.__downloadPage(soupObject)
            for link in soupObject.findAll('a', href = True): #Search every link on the current page
                href = link.get('href')
                if self.__checkRegex(href) and not href in self._visited and self._pageCount >= 0:
                    hrefSoup = None
                    if self._level > 1:
                        hrefText = requests.get(href).text
                        hrefSoup = BeautifulSoup(hrefText, 'html.parser')
                    rank = self.__getRank(hrefSoup, href, level = self._level)
                    self._pageHeap.put_nowait((-rank, href))

    def __checkRegex(self, page):
        #Check if this page is relevant by matching the basicRegex with the page url
        return re.match(self._urlRegex, page)

    @abstractmethod
    def __downloadPage(self, soupObject):
        #Method to download pages
        pass
    
    @abstractmethod
    def __getRank(self, soupObject, url, level):
        #Method to priorize game pages
        pass

    @abstractmethod
    def __cleanUrl(self, url):
        #Method to remove noise
        pass

    def run(self):
        self.__searchPages(self._basicUrl)