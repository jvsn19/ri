import glob
import re
from bs4 import BeautifulSoup

def removeHtmlContent(path):
    page = BeautifulSoup(open(path), "html.parser")
    [s.extract() for s in page("script")]

    return page.get_text().encode("utf-8")

def findAllHtmlFiles():
    files = glob.glob("*/*/*.html")
    
    for i in range(len(files)):
        path_output = re.sub('.html', '.txt', files[i])
    
        file = open(path_output, "w")
        file.write(removeHtmlContent(files[i]))
        file.close()