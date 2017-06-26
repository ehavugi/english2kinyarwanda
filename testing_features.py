# Testing new features and functions 
#	 this can allow to create functions that can be imbedded into other functions as
#    reusability can be great in this type of stuff
# Testing point for new features, or testing interfacing documenation for consistence 
# a model for a finished or functionalities that can be accessed by system users

#kinya1=open("kinya1.txt").readlines() (encoding errors for texts copied from PDF document)

from code.number2words import *
from code.kinyarwanda_test import *
#from code.making_kinyarwanda import *
from code.EnglishTagging import *
#from code.

#from kinyarwanda_test import *
#from making_kinyarwanda import *
#from kiny_scraping import *


#from translator import  translate,eng2Kin,kin,eng


#translate("I would like a ro *bust way to translate english to kinyarwanda. it would be neat",eng2Kin)

#from number2words import  * 

adj=open("text/adj.txt").readlines()
# s2=open("s2.txt", encoding="utf8").readlines()
# s5=open("s5.txt", encoding="utf8").readlines()
# s3=open("s3.txt", encoding="utf8").readlines()
# microEcon=open("micro_economics.txt", encoding="utf8").readlines()
# principles=open("principles.txt",encoding="utf8").readlines()
amategeko=open("text/amategeko.txt",encoding="utf8").readlines()


#spell(4545)  ## how can it support different formats, integers,strings of numbers, list of numbers,or another format

print(ibihumbi("844347"),"84347")
print(amajana("45",1))
print(miliyoni("456674"))
kinyarwanda_text="inyarwanda ni ururimi rw' abanyarwanda  ruvugwa mu Rwanda hafi ijana kw' ijana".split()
english_text="English is a  great language that is spoken by many persons accross the globe".split()

print("English adjectives", kinyarwanda_level(adj))
# print("principles by Bridgewater dude", kinyarwanda_level(principles))
print( "A mix of French, Kinyarwanda and English", kinyarwanda_level(amategeko))
print(ni_igihekane("nzw"))

#print (is_special("and"))
urls=[]

# for url in base_url_list:
# 	try:
# 		for url in get_urls(url):
# 			#print (url)
# 			urls.append(url)
# 	except:
# 		continue
# print("nested thing")
# print (len(urls))
# url2=[]
# for url in urls:
# 	try:
# 		for urli in get_urls(url):
# 			if not(urli in url2):
# 				#print(urli)
# 				url2.append(urli)
# 	except:
# 		continue
# print(len(url2))

# url3=[]
# for url in url2:
# 	try:
# 		for urly in get_urls(url):
# 			if not(urly in url3):
# 				print(urly)
# 				url3.append(urly)
# 	except:
# 		continue
# print(len(url3))

