# -*- coding: utf-8 -*-

import glob
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from bs4 import BeautifulSoup


def takeHtmlContent(path):
    page = BeautifulSoup(open(path), "html.parser")
    [s.extract() for s in page("script")]
    [s.extract() for s in page("style")]

    page_content = page.get_text().encode("utf-8")
    return page_content

def takeAllFiles(file_type):
    files = glob.glob("*/*/*." + file_type)

    return files

def removePoints(html_content):
    html_content = re.sub("\n+|\t+", " ", html_content)
    html_content = re.sub("[!\d+,.;@#?!&$--)(:/}{|=]+|•|©|﻿|™|®|×| x ","",  html_content)
    return html_content

def putContentInFile(in_type, out_type):
    files = takeAllFiles(in_type)
    for i in range(len(files)):
        path_output = re.sub('.' + in_type, '.' + out_type, files[i])
        html_content = takeHtmlContent(files[i])
        html_content = removePoints(html_content)
        file = open(path_output, "w")
        file.write(html_content)
        file.close()

putContentInFile("html", "txt")

def tokenizeFiles():
    files = takeAllFiles("txt")
    
    vec_doc = [open(files[i], "r").read() for i in range(len(files))]
    vectorizer = CountVectorizer()
    #print([open(files[0], "r").read()])
    print(vectorizer.fit_transform(vec_doc).todense())
    #vector = vectorizer.transform(files)
    #print(vectorizer.vocabulary_)

tokenizeFiles()