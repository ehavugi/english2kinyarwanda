# Testing new features and functions 
#	 this can allow to create functions that can be imbedded into other functions as
#    reusability can be great in this type of stuff
# Testing point for new features, or testing interfacing documenation for consistence 
# a model for a finished or functionalities that can be accessed by system users

#kinya1=open("kinya1.txt").readlines() (encoding errors for texts copied from PDF document)

from EnglishTagging import *

from kinyarwanda_test import *
from making_kinyarwanda import *
from kiny_scraping import *

from translator import  translate,eng2Kin,kin,eng


#translate("I would like a ro *bust way to translate english to kinyarwanda. it would be neat",eng2Kin)

from number2words import amajana,spell,phone

adj=open("adj.txt").readlines()
# s2=open("s2.txt", encoding="utf8").readlines()
# s5=open("s5.txt", encoding="utf8").readlines()
# s3=open("s3.txt", encoding="utf8").readlines()
# microEcon=open("micro_economics.txt", encoding="utf8").readlines()
# principles=open("principles.txt",encoding="utf8").readlines()
amategeko=open("amategeko.txt",encoding="utf8").readlines()

kiny=kin
kinyarwanda=kiny
english=eng
#spell(4545)  ## how can it support different formats, integers,strings of numbers, list of numbers,or another format

#print(amajana(132))
kinyarwanda_text="inyarwanda ni ururimi rw' abanyarwanda  ruvugwa mu Rwanda hafi ijana kw' ijana".split()
english_text="English is a  great language that is spoken by many persons accross the globe".split()
#print(len((ibihekane+consonants+vowels)))
#print((consonants_in(kinyarwanda_text)))

#print(phone(945))

#print(" Kinyarwanda medium text : length ", len(kin), ":", kinyarwanda_level(kin), "\n English medium text : lenght ", len(english), kinyarwanda_level(english))
#print(" kinyarwanda short sentence : length ",len(kinyarwanda_text), " Length: " , kinyarwanda_level(kinyarwanda_text))
#print("English short sentence : length ",len(english_text), " , level  :", kinyarwanda_level(english_text))
#print(kinyarwanda_level(["inyarwanda ni indirimbo nyarwanda"]))  ## I am havign a varying level depending on other tests, how can i make it instance independent

#print(consonants_in(kiny))
# print("s2 textbook of Kinyarwanda ", (kinyarwanda_level(s2)))
# print("s3 textbook of Kinyarwanda ",(kinyarwanda_level(s3)))
# print("s5 textbook of Kinyarwanda ", (kinyarwanda_level(s5)))
# print("Micro Economics text book", kinyarwanda_level(microEcon))
print("English adjectives", kinyarwanda_level(adj))
# print("principles by Bridgewater dude", kinyarwanda_level(principles))
print( "A mix of French, Kinyarwanda and English", kinyarwanda_level(amategeko))
print(is_igihekane("nzw"))

#print (is_special("and"))


print(base_url_list)





