# -*- coding: utf-8 -*-

import glob
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import codecs

def takeHtmlContent(path):
    page = BeautifulSoup(open(path), "html.parser")
    [s.extract() for s in page("script")]
    [s.extract() for s in page("style")]

    page_content = page.get_text().encode("utf-8")
    return page_content

def takeAllFiles(file_type):
    files = glob.glob("sites/*/*/*." + file_type)

    return files

def removePoints(html_content):
    html_content = re.sub("\n+|\t+", " ", html_content)
    html_content = re.sub("[!\d+,.;@#?!&$--)(:/}{|=]+|•|©|﻿|™|®|×| x "," ",  html_content)
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

def Stemming(vec_doc):
    stemmer = PorterStemmer()
    analyzer = CountVectorizer().build_analyzer()
    
    return (stemmer.stem(w) for w in analyzer(vec_doc))

def stop_words():
    stopWords = set(stopwords.words('english'))
    
    return stopWords

def tokenizeFiles():
    files = takeAllFiles("txt")
    
    vec_doc = [codecs.open(files[i], "r", encoding='utf-8').read() for i in range(len(files))]
    
    vec_class = [re.search("\w+/(\w+)/\w+", files[i]).group(1) == "positivePages" and 1 or 0 
                for i in range(len(files))]
    #print(vec_doc)
    vectorizer = CountVectorizer(encoding='utf-8')
    doctermMatrix = vectorizer.fit_transform(vec_doc)
    
    dataFrame = pd.DataFrame(doctermMatrix.todense())
    dataFrame["class"] = vec_class
    dataFrame.to_csv("data/docterm.csv", index = False)

#tokenizeFiles()