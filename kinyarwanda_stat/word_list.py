# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 10:02:47 2017

@author: Emmanuel HAVUGIMANA
"""

""" Kinyarwanda single word listing"""

import os
from kinyarwanda_test import *
## navigate through kinyarwanda_text and make a set a dictionary of word and their occuracies
## rank the words and save them to a file
a=""
count=0

    
alphabetical=[]
frequency={}
sentences='43943'
sortlist=[]
def count_words(a,frequency):
    for word in a:
        if kinyarwanda_level(word)>0.7:
            if word in frequency.keys() :         
                frequency[word]=frequency.get(word)+1
            else:
                frequency[word]=1
        else:
            print(word,"not kinyarwanda")
    #l=frequency.items()
    # for key,value in l.sorted():
    # 	sortedlist1+=[key,value]
    # sortlist=sortedlist1
    # return sortlist
for m, n, l in (os.walk("./kinya_text")):
    for i in l:
        file=m+"/"+i
        print(file)
        a=open(file,encoding='utf8').read().split()
        count_words(a,frequency)
        print(len(a))
        #print(frequency)
print (frequency)