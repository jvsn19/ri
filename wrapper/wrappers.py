from lxml import etree
import re

parser = etree.HTMLParser()
root = '../classifier/sites/steam/positivePages/page'
labels_general = ['Game','Price','OS','Processor','RAM','Graphics','DirectX','Storage']

def get_list_info_steam(name, listReq, list, price):
    info = []
    offset = 0
    if(name == []): info.append(None)
    else: info.append(name)
    if(price == []): info.append(None)
    else: 
        price = re.sub("[\t\n\r]+",'', price)
        info.append(price)

    if('Requires a 64-bit processor and operating system' in list): offset = 1
    for i in range(0,len(listReq)):
        if (listReq[i] == 'OS:' or listReq[i] == 'Processor:' or listReq[i] == 'Memory:'
            or listReq[i] == 'Graphics:' or listReq[i] == 'DirectX:' or listReq[i] == 'Storage:'):
            info.append(list[i + offset].lower())
    return info

data_steam = []


XPATH_INFO_TITLE_STEAM = '//div[@class="sysreq_contents"]/div/div[1]/ul/ul/li/strong/text()'
XPATH_INFO_STEAM = '//div[@class="sysreq_contents"]/div/div[1]/ul/ul/li/text()'
XPATH_PRICE_STEAM = '//div[@class="discount_final_price"]/text()'
XPATH_PRICE_STEAM2 = '//div[@class="game_purchase_action"]/div[1]/div[1]/text()'
XPATH_NAME_STEAM = '//div[@class="apphub_AppName"]/text()'

for i in range (1,11):
    tree = etree.parse(root + str(i) + ".html", parser)
    RAW_NAME = tree.xpath(XPATH_NAME_STEAM)
    RAW_INFO_TITLE = tree.xpath(XPATH_INFO_TITLE_STEAM)
    RAW_INFO = tree.xpath(XPATH_INFO_STEAM)
    RAW_PRICE = tree.xpath(XPATH_PRICE_STEAM)
    if(RAW_PRICE == []): RAW_PRICE = tree.xpath(XPATH_PRICE_STEAM2)
    
    FILTERED_INFO = get_list_info_steam(RAW_NAME, RAW_INFO_TITLE, RAW_INFO, RAW_PRICE)
   
    data_steam.append(dict(zip(labels_general,FILTERED_INFO)))
    
for i in range (0,len(data_steam)):
    print(data_steam[i])
    #print()
print(len(data_steam))

root = '../classifier/sites/uplay/positivePages/page'

def get_list_info_up(name, listReq, list, price):
    info = []
    offset = 0
    if(name == None): info.append(None)
    else: info.append(name)
    
    if(price == None): info.append(None)
    else: info.append(price)
    if('Requires a 64-bit processor and operating system' in list): offset = 1
    for i in range(0,len(listReq)):
        if (listReq[i] == 'OS:' or listReq[i] == 'Processor:' or listReq[i] == 'Memory:'
            or listReq[i] == 'Graphics:' or listReq[i] == 'DirectX:' or listReq[i] == 'Storage:'):
            info.append(list[i + offset].lower())
    return info

data_uplay = []

XPATH_INFO_TITLE_UP = '//article[@class="minimum"]/ul/li/font/text()'
XPATH_INFO_UP = '//article[@class="minimum"]/ul/li/text()'
XPATH_PRICE_UP = '//span[@class="price-sales"]/text()'
XPATH_NAME_UP = '//h1[@class="update-product-name"]/text()'

for i in range (1,11):
    tree = etree.parse(root + str(i) + ".html", parser)
    RAW_NAME = tree.xpath(XPATH_NAME_UP)
    RAW_INFO_TITLE = tree.xpath(XPATH_INFO_TITLE_UP)
    RAW_INFO = tree.xpath(XPATH_INFO_UP)
    RAW_PRICE = tree.xpath(XPATH_PRICE_UP)
    #print(RAW_NAME)
    #print(RAW_INFO_TITLE)
    #print(RAW_INFO)
    
    FILTERED_INFO = get_list_info_up(RAW_NAME[0], RAW_INFO_TITLE, RAW_INFO, RAW_PRICE[0])
    #RAW_PRICE_SUBMARINO = tree.xpath(XPATH_PRICE_STEAM)
    #FILTERED_INFO.append(RAW_PRICE_SUBMARINO[0])
    #FILTERED_INFO.append(i)
    #print(dict(zip(labels_general,FILTERED_INFO)))
    data_uplay.append(dict(zip(labels_general,FILTERED_INFO)))
    
for i in range (0,len(data_uplay)):
    print(data_uplay[i])
    #print()
print(len(data_uplay))

root = '../classifier/sites/itch/positivePages/page'

def get_list_info_itch(name, listReq, price):
    info = []
    
    if(name == []): info.append(None)
    else: info.append(name[0])
    if(price == []): info.append("Free")
    else: info.append(price[0])

    for i in range(0,len(listReq)):
        if(listReq == 'Recommended:' or listReq == 'Additional Notes:'): break
            
        express = re.search('(\w+\:)', listReq[i])
        if(express == None): break
        print(express.group(1))
        express = express.group(0)
        if (express == 'OS:' or express == 'Processor:' or express == 'Memory:'
            or express == 'Graphics:' or express == 'DirectX:' or (express == 'Space:' or express == 'Storage:')):
            info.append(express.lower())
    return info

data_itch = []

XPATH_INFO_ITCH = '//div[@id="left_col column"]/div[1]/ul/li/text()'
XPATH_PRICE_ITCH = '//span[@class="buy_message"]/span[1]/text()'
XPATH_NAME_ITCH = '//title/text()'

for i in range (1,11):
    tree = etree.parse(root + str(i) + ".html", parser)
    RAW_NAME = tree.xpath(XPATH_NAME_ITCH)
    RAW_INFO = tree.xpath(XPATH_INFO_ITCH)
    RAW_PRICE = tree.xpath(XPATH_PRICE_ITCH)

    FILTERED_INFO = get_list_info_itch(RAW_NAME, RAW_INFO, RAW_PRICE)

    data_itch.append(dict(zip(labels_general,FILTERED_INFO)))
    
for i in range (0,len(data_itch)):
    print(data_itch[i])
    #print()
print(len(data_itch))