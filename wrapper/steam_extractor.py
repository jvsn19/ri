from bs4 import BeautifulSoup
import re
import requests
import os

class SteamExtractor():
    def __init__(self, filePath):
        html_text = os.open(filePath)
        self.soupObj = BeautifulSoup(html_text, 'html.parser')
        self.divClasses = ['apphub_AppName', 'game_description_snippet']

    def getGameTitle(self):
        pass


