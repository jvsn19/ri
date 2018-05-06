from spiders.basic_spider import Spider
import re

class SteamSpider(Spider):
    def __init__(self, basicUrl, pageLimit):
        Spider.__init__(self, basicUrl, pageLimit)

    def _Spider__downloadPage(self, soupObject):
        path = open('pages/steam_' + str(self._pageCount) + '.html', 'wb')
        path.write(soupObject.encode('utf-8'))
        path.close()
    
    def _Spider__getRank(self, soupObject):
        gameAreaRegex = re.compile('game_area_details_specs')
        tag = soupObject.find('div', {'class': gameAreaRegex})
        return tag != None