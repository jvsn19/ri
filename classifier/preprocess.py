# -*- coding: utf-8 -*-

import glob
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
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

def stemming(vec_doc):
    stemmer = PorterStemmer()
    analyzer = CountVectorizer().build_analyzer()
    
    return (stemmer.stem(w) for w in analyzer(vec_doc))

def stop_words():
    stopWords = set(stopwords.words('english'))
    
    return stopWords

def MakeVecDoc():
    files = takeAllFiles("txt")
    
    vec_doc = [codecs.open(files[i], "r", encoding='utf-8').read() for i in range(len(files))]
    
    vec_class = [re.search("\w+/\w+/(\w+)/\w+", files[i]).group(1) == "positivePages" and 1 or 0 
                for i in range(len(files))]

    return vec_doc, vec_class

def tokenizeFiles(useStemming, useStopWords, dataName):
    vec_doc, vec_class = MakeVecDoc()
    vectorizer = None
    vectorizerTfidf = None
    if(useStemming == False and useStopWords == False): 
        vectorizer = CountVectorizer(encoding='utf-8')
        vectorizerTfidf = TfidfVectorizer(encoding='utf-8')
    
    elif(useStemming == True and useStopWords == False):
        vectorizer = CountVectorizer(encoding='utf-8', analyzer=stemming)
        vectorizerTfidf = TfidfVectorizer(encoding='utf-8', analyzer=stemming)

    elif(useStemming == False and useStopWords == True):
        vectorizer = CountVectorizer(encoding='utf-8', stop_words=stop_words())
        vectorizerTfidf = TfidfVectorizer(encoding='utf-8', stop_words=stop_words())
    else:
        vectorizer = CountVectorizer(encoding='utf-8', stop_words=stop_words(), analyzer=stemming)
        vectorizerTfidf = TfidfVectorizer(encoding='utf-8', stop_words=stop_words(), analyzer=stemming)

    doctermMatrix = vectorizer.fit_transform(vec_doc)
    doctermMatrixTfidf = vectorizerTfidf.fit_transform(vec_doc)

    dataFrameCount = pd.DataFrame(doctermMatrix.todense())
    dataFrameCount["class"] = vec_class
    dataFrameCount.to_csv("data/" + dataName + ".csv", index = False)
    
    dataFrameTfidf = pd.DataFrame(doctermMatrixTfidf.todense())
    dataFrameTfidf["class"] = vec_class
    dataFrameTfidf.to_csv("data/" + dataName + "Tfidf.csv", index = False)


def main():
    #putContentInFile("html", "txt")
    tokenizeFiles(False, False, "token")
    tokenizeFiles(False, True, "stopwords")
    tokenizeFiles(True, False, "stemming")
    tokenizeFiles(True, True, "stopNstem")

main()