from spiders.basic_spider import Spider
import re

class ItchSpider(Spider):
    def __init__(self, basicUrl, pageLimit, level):
        Spider.__init__(self, basicUrl, pageLimit, level)

    def _checkRegex(self, page):
        return re.match('^https?://.*\.itch\.io.*$', page)

    def _downloadPage(self, soupObject):
        path = open('pages/itch_' + str(self._pageCount) + '.html', 'wb')
        path.write(soupObject.encode('utf-8'))
        path.close()
    
    def _getRank(self, soupObject, url, level):
        return 0

    def _cleanUrl(self, url):
        return url

    def _fixUrl(self, url):
        if re.search('https?://.*', url):
            return url
        return self._basicUrl[:-1] + url