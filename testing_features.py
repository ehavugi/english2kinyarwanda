# Testing new features and functions 
#	 this can allow to create functions that can be imbedded into other functions as
#    reusability can be great in this type of stuff
# Testing point for new features, or testing interfacing documenation for consistence 
# a model for a finished or functionalities that can be accessed by system users

#kinya1=open("kinya1.txt").readlines() (encoding errors for texts copied from PDF document)

#from code.number2words import *
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
kinyarwanda_bible=open("text/bysb.txt", encoding="utf8").readlines()

umushyikirano=open("text/umushyikirano.txt",encoding="utf8").read()
# s2=open("s2.txt", encoding="utf8").readlines()
# s5=open("s5.txt", encoding="utf8").readlines()
# s3=open("s3.txt", encoding="utf8").readlines()
# microEcon=open("micro_economics.txt", encoding="utf8").readlines()
# principles=open("principles.txt",encoding="utf8").readlines()
amategeko=open("text/amategeko.txt",encoding="utf8").readlines()


#spell(4545)  ## how can it support different formats, integers,strings of numbers, list of numbers,or another format

# print(ibihumbi("844347"),"84347")
# print(amajana("45",1))
# print(miliyoni("456674"))
kinyarwanda_text="inyarwanda ni ururimi rw' abanyarwanda  ruvugwa mu Rwanda hafi ijana kw' ijana".split()
english_text="English is a  great language that is spoken by many persons accross the globe".split()

print("English adjectives", kinyarwanda_level(adj))
# print("principles by Bridgewater dude", kinyarwanda_level(principles))
print( "A mix of French, Kinyarwanda and English", kinyarwanda_level(amategeko))
print(ni_igihekane("nzw"))


classs=[ ["umu","umw"],["aba","ab"],["umu","umw"],["imi","imy"],["i","iri"],["ama","am"],["iki","icy","igi"],["ibi","iby"],["i","in","inz"],['uru',"urw"],["aka","ak","aga"],["utu","utw","udu"],["ubu","ubw"],["uku","ukw",'ugu'],["aha","ah"]]
for line in kinyarwanda_bible:
	line=line.strip().lower()
	#print(line)
	for word in line.split() :
		if len(word)>4 :
			#print(line)
			for x in classs:
				for y in x:
					if word.startswith(y):
						print(word, " : ", y)
			else:
				continue
				#print("plural : ", word, " singular : ",word.replace('ab',"umu") )

#print(miliyoni(1))