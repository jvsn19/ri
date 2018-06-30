from spiders.basic_spider import Spider
import re

class OnePlaySpider(Spider):
    def __init__(self, basicUrl, pageLimit, level):
        Spider.__init__(self, basicUrl, pageLimit, level)

    def _checkRegex(self, page):
        return re.search('^/en/.*/', page)

    def _downloadPage(self, soupObject):
        path = open('pages/oneplay_' + str(self._pageCount) + '.html', 'wb')
        path.write(soupObject.encode('utf-8'))
        path.close()
    
    def _getRank(self, soupObject, url, level):
        #The oneplay's url with /detail/ normally refers to game page. So we can priorize them
        return bool(re.search('/details/', url))

    def _cleanUrl(self, url):
        return url

    def _fixUrl(self, url):
        print(self._basicUrl[:-1] + url)
        return self._basicUrl[:-1] + url