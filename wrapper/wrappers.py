from lxml import etree
import re

parser = etree.HTMLParser()
root = '../classifier/sites/steam/positivePages/page'
labels_general = ['Game','Price','OS','Processor','RAM','Graphics','DirectX','Storage']

def get_list_info_steam(name, listReq, list, price):
    info = []
    offset = 0
    if(name == []): info.append(None)
    else: info.append(name[0])
    if(price == []): info.append(None)
    else: 
        price = re.sub("[\t\n\r]+",'', price[0])
        info.append(price)

    if('Requires a 64-bit processor and operating system' in list): offset = 1
    for i in range(0,len(listReq)):
        if (listReq[i] == 'OS:' or listReq[i] == 'Processor:' or listReq[i] == 'Memory:'
            or listReq[i] == 'Graphics:' or listReq[i] == 'DirectX:' or listReq[i] == 'Storage:'):
            info.append(list[i + offset].lower())
        else: info.append("--")
    return info

def get_list_info_up(name, listReq, list, price):
    info = []
    offset = 0
    if(name == None): info.append(None)
    else: info.append(name[0])

    if(price == None): info.append(None)
    else: info.append(price[0])
    if('Requires a 64-bit processor and operating system' in list): offset = 1
    for i in range(0,len(listReq)):
        if (listReq[i] == 'OS:' or listReq[i] == 'Processor:' or listReq[i] == 'Memory:'
            or listReq[i] == 'Graphics:' or listReq[i] == 'DirectX:' or listReq[i] == 'Storage:'):
            info.append(list[i + offset].lower())
        else: info.append("--")
    return info

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

        express = express.group(0)
        if (express == 'OS:' or express == 'Processor:' or express == 'Memory:'
            or express == 'Graphics:' or express == 'DirectX:' or (express == 'Space:' or express == 'Storage:')):
            info.append(express.lower())
        else: info.append("--")
            
    return info

def get_atributes_steam(path):
    parser = etree.HTMLParser()
    root = path
    labels_general = ['Game','Price','OS','Processor','RAM','Graphics','DirectX','Storage']
    
    XPATH_INFO_TITLE_STEAM = '//div[@class="sysreq_contents"]/div/div[1]/ul/ul/li/strong/text()'
    XPATH_INFO_STEAM = '//div[@class="sysreq_contents"]/div/div[1]/ul/ul/li/text()'
    XPATH_PRICE_STEAM = '//div[@class="discount_final_price"]/text()'
    XPATH_PRICE_STEAM2 = '//div[@class="game_purchase_action"]/div[1]/div[1]/text()'
    XPATH_NAME_STEAM = '//div[@class="apphub_AppName"]/text()'
    
    data = []

    tree = etree.parse(root, parser)
    RAW_NAME = tree.xpath(XPATH_NAME_STEAM)
    RAW_INFO_TITLE = tree.xpath(XPATH_INFO_TITLE_STEAM)
    RAW_INFO = tree.xpath(XPATH_INFO_STEAM)
    RAW_PRICE = tree.xpath(XPATH_PRICE_STEAM)
    if(RAW_PRICE == []): RAW_PRICE = tree.xpath(XPATH_PRICE_STEAM2)
        
    FILTERED_INFO = get_list_info_steam(RAW_NAME, RAW_INFO_TITLE, RAW_INFO, RAW_PRICE)
    
    data.append(dict(zip(labels_general,FILTERED_INFO)))
        
    return data[0]

def get_atributes_uplay(path):
    parser = etree.HTMLParser()
    root = path

    data_uplay = []

    XPATH_INFO_TITLE_UP = '//article[@class="minimum"]/ul/li/font/text()'
    XPATH_INFO_UP = '//article[@class="minimum"]/ul/li/text()'
    XPATH_PRICE_UP = '//span[@class="price-sales"]/text()'
    XPATH_NAME_UP = '//h1[@class="update-product-name"]/text()'

    tree = etree.parse(root, parser)
    RAW_NAME = tree.xpath(XPATH_NAME_UP)

    RAW_INFO_TITLE = tree.xpath(XPATH_INFO_TITLE_UP)
    RAW_INFO = tree.xpath(XPATH_INFO_UP)
    RAW_PRICE = tree.xpath(XPATH_PRICE_UP)
        
    FILTERED_INFO = get_list_info_up(RAW_NAME, RAW_INFO_TITLE, RAW_INFO, RAW_PRICE)
    data_uplay.append(dict(zip(labels_general,FILTERED_INFO)))
        
    return data_uplay[0]

def get_atributes_itch(path):
    parser = etree.HTMLParser()
    root = path

    data_itch = []

    XPATH_INFO_ITCH = '//div[@id="left_col column"]/div[1]/ul/li/text()'
    XPATH_PRICE_ITCH = '//span[@class="buy_message"]/span[1]/text()'
    XPATH_NAME_ITCH = '//title/text()'

    tree = etree.parse(root, parser)
    RAW_NAME = tree.xpath(XPATH_NAME_ITCH)
    RAW_INFO = tree.xpath(XPATH_INFO_ITCH)
    RAW_PRICE = tree.xpath(XPATH_PRICE_ITCH)

    FILTERED_INFO = get_list_info_itch(RAW_NAME, RAW_INFO, RAW_PRICE)

    data_itch.append(dict(zip(labels_general,FILTERED_INFO)))
    
    return data_itch[0]

#if __name__ == "__main__":
#    print(get_atributes_uplay('../classifier/sites/uplay/positivePages/page1.html'))