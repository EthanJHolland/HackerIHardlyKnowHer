# -*- coding: utf-8 -*-

import sys
import traceback
import math
from tqdm import tqdm
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup

class Scrape:
    def __init__(self):
        self.scrapers=[]
        self.url='https://en.wiktionary.org/w/index.php?title=Category:English_transitive_verbs&pagefrom='
        self.first='abacinate'

    def start(self):   
        self.pbar = tqdm(total=68, position=0,ncols=80, mininterval=1.0)

        while True:
            try:
                data = urlopen(self.url+str(self.first)).read()
                soup = BeautifulSoup(data, 'html.parser')
            except:
                print(traceback.format_exc())

            f = open("words.txt", "a",encoding='utf-8')

            for div in soup.find_all('div', 'mw-category-group'):
                for ul in div.find_all('ul'):
                    for li in ul.find_all('li'):
                        word=li.a.string
                        if len(word)>1 and not ' ' in word and not ':' in word and word[0]==word[0].lower() and not word==self.first:
                            f.write('\"'+word+'\",')
            print(word)
            self.updateProgress()
            word=word.split(' ', 1)[0]
            if(word==self.first):
                #made it to the last word
                break
            self.first=word #get the next page starting at the last word on this one
            

    def updateProgress(self):
        self.pbar.update(1)

    #print a beautifulsoup object in prettified form after removing unprintable characters
    def printSoup(self, soup):
        f = open("h.html", "w",encoding='utf-8')
        f.write(soup.prettify())
        
        

if __name__ == '__main__':
    #scrape the list of transitive verbs from wikipedia
    m=Scrape()
    m.start()