from abc import ABC, abstractmethod
import requests

class Spider(ABC):
    def __init__(self, basic_url):
        self.__basic_url = basic_url

    @abstractmethod
    def search_pages(self, deep):
        pass

    @abstractmethod
    def get_page_attributes(self, url):
        pass