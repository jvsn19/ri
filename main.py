from spiders.steam_spider import SteamSpider

if __name__ == '__main__':
    spider = SteamSpider('https://store.steampowered.com/', 100)
    spider.run()