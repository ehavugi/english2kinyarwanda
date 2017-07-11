# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 10:02:47 2017

@author: Emmanuel HAVUGIMANA
"""

""" Kinyarwanda single word listing"""

import os
from code.kinyarwanda_test import *
## navigate through kinyarwanda_text and make a set a dictionary of word and their occuracies
## rank the words and save them to a file
a=""
count=0

    
alphabetical=[]
frequency={}
sentences='43943'
sortlist=[]
vowel="auioe"
def word_end_vowel(word):
    if not(word[len(word)-1] in vowel ):
        return False
        print(word, "not kinya")
    return True
def do_wovel_kinya(word):
    a=len(word)
    if a<2:
        return True
    for i in range(a-1):
        if word[i] in vowel and word[i+1] in vowel:
            print("vowel problem", word)
            return False
    return True

def count_words(a,frequency):
    for word in a:
        if kinyarwanda_level(word)>0.5 and word_end_vowel(word)  and do_wovel_kinya(word):
            print(word,kinyarwanda_level(word))
            if word in frequency.keys() :         
                frequency[word]=frequency.get(word)+1
            else:
                frequency[word]=1
        else:
            continue
            #print(word, kinyarwanda_level(word))
    #l=frequency.items()
    # for key,value in l.sorted():
    # 	sortedlist1+=[key,value]
    # sortlist=sortedlist1
    # return sortlist
for m, n, l in (os.walk("./kinya_text")):
    for i in l:
        file=m+"/"+i
        print(file)
        a=open(file,encoding='utf8').read().lower().split()
        count_words(a,frequency)
        print(len(a))
        print(frequency)
print (frequency)