from spiders.basic_spider import Spider
import re

class SteamSpider(Spider):
    def __init__(self, basicUrl, pageLimit, level):
        Spider.__init__(self, basicUrl, pageLimit, level)

    def _Spider__downloadPage(self, soupObject):
        path = open('pages/steam_' + str(self._pageCount) + '.html', 'wb')
        path.write(soupObject.encode('utf-8'))
        path.close()
    
    def _Spider__getRank(self, soupObject, url, level):
        ranking = 0
        if level == 1:
            urlRegex = re.compile('/app/')
            if re.search(urlRegex, url):
                ranking += 1
        if level == 2:
            gameAreaRegex = re.compile('game_area_details_specs')
            tag = soupObject.find('div', {'class': gameAreaRegex})
            ranking += (tag != None)
        return ranking