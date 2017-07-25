# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 10:02:47 2017

@author: Emmanuel HAVUGIMANA
"""

""" Kinyarwanda single word listing"""

import os
from code.kinyarwanda_test import *
import re
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
##return True if word end with a vowel, return false
    if not(word[len(word)-1] in vowel):
    	return False
    return True
def do_wovel_kinya(word):
   ## return True if the there are no two vowels following each other
    a=len(word)
    if a<2: return True
    for i in range(a-1):
        if word[i] in vowel and word[i+1] in vowel:
            return False
    return True
def kinya(word):
	return (do_wovel_kinya(word) and word_end_vowel(word))
def count_words(a,frequency):
    for word in a:
        if kinyarwanda_level(word)>0.5 and word_end_vowel(word)  and do_wovel_kinya(word):
            if word in frequency.keys() :         
                frequency[word]=frequency.get(word)+1
            else:
                frequency[word]=1
        else:
            continue
            #print(word, kinyarwanda_level(word))
    # # l=frequency.items()
    # for key,value in sort(l):
    #    	sortedlist1+=[key,value]
    # sortlist=sortedlist1
    # return sortlist
all_words=[]
#ordered_words=open("ordered_words.txt","w")
for m, n, l in (os.walk("kinyarwanda_stat/kinya_text")):
	## search through all texts in a certain folder and do analysis about it

    for i in l:
        file=m+"/"+i
        print(file)
        all_wordsin=[]
        counting_skips=0
        with open(file,encoding='utf8') as a:
        	#size=len(a.read())
        	count=0
	        for j in a:
	            a_split=re.split("[^a-zA-Z]",j)
	            for word in a_split:  
	            	count+=1  	
	            	if word in all_words or word in all_wordsin:
	            		#print (word)
	            		counting_skips+=1
	            		continue
	            	else:
	            		if len(word)>0 and kinya(word):
	            			counting_skips=0
	            			all_words.append(word)
        			# if (counting_skips!=0):
           #              continue
                        
        				#print(counting_skips)

        			#print(word)
        				
        		    #listingsa.append(word)
       #	print(listingsa.sort())
        #print(count_words(a,frequency)) 
        
        all_words=all_words+all_wordsin  
        with open("ordered_words.txt","w") as ordered_words:
	        print(sorted(all_words))
	        for word in sorted(all_words):
	            ordered_words.write(word+"\n")
	        
	       
print ("end")


### how how is the n^th word likely have been repeated after reading text n_1
## or how likely that the next k words have all occured before in a text with n words





###  word       lenght_up2word      number_words_skipped  locations
###  banenze        100000                  4              [1,12,34,450,345,640,5467]
###  etc

### word            frequency 

### word1 + word2    frequency

### word1 word2 word3 frequency


