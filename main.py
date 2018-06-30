from spiders.steam_spider import SteamSpider #ok
from spiders.gg_spider import GGSpider #fail
from spiders.gamersgate_spider import GamersGateSpider #ok 
from spiders.oneplay_spider import OnePlaySpider #fail
from spiders.gog_spider import GOGSpider #to improve
from spiders.humblebundle_spider import HumbleBundleSpider #fail
from spiders.origin_spider import OriginSpider #fail
from spiders.nuuven_spider import NuuvemSpider # ok
from spiders.itch_spider import ItchSpider #ok
from spiders.uplay_spider import UplaySpider

if __name__ == '__main__':
    #steam = SteamSpider('https://store.steampowered.com/', 1001, level = 1)
    #steam.run()
    #greengaming = GGSpider('https://www.greenmangaming.com/', 100, level = 1)
    #greengaming.run()
    #gamersgate = GamersGateSpider('https://br.gamersgate.com/', 1001, 1)
    #gamersgate.run()
    #oneplay = OnePlaySpider(basicUrl = 'http://www.oneplay.com/', 100, 1)
    #oneplay.run()
    #gog = GOGSpider('https://www.gog.com/', 1001, 1)
    #gog.run()
    #humblebundle = HumbleBundleSpider('https://www.humblebundle.com/', 100, 1)
    #humblebundle.run()
    #origin = OriginSpider('https://www.origin.com/', 100, 1)
    #origin.run()
    #nuuvem = NuuvemSpider('https://www.nuuvem.com/', 1001, 1)
    #nuuvem.run()
    #itch = ItchSpider('https://itch.io/', 1001, 1)
    #itch.run()
    ubisoft = UplaySpider('https://store.ubi.com/', 1001, 1)
    ubisoft.run()
    pass
