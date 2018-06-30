from spiders.basic_spider import Spider
import re

class UplaySpider(Spider):
    def __init__(self, basicUrl, pageLimit, level):
        Spider.__init__(self, basicUrl, pageLimit, level)

    def _checkRegex(self, page):
        if re.match(".*\.jpg", page):
            return False
        if re.match("https?://.*", page):
            return re.match(".*store.uplay.*", page)
        else:
            return True

    def _downloadPage(self, soupObject):
        path = open('pages/uplay_' + str(self._pageCount) + '.html', 'wb')
        path.write(soupObject.encode('utf-8'))
        path.close()
    
    def _getRank(self, soupObject, url, level):
        return 0

    def _cleanUrl(self, url):
        return url

    def _fixUrl(self, url):
        return self._basicUrl[:-1] + url