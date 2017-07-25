# Testing new features and functions 
#	 this can allow to create functions that can be imbedded into other functions as
#    reusability can be great in this type of stuff
# Testing point for new features, or testing interfacing documenation for consistence 
# a model for a finished or functionalities that can be accessed by system users

#kinya1=open("kinya1.txt").readlines() (encoding errors for texts copied from PDF document)

from code.number2words import *
#from code.EnglishTagging import *
#from code.ubuke_ubwinshi import *
from sys import *

kinyarwanda_bible=open("kinyarwanda_stat/kinya_text/bysb_patrick.txt", encoding="utf8").read()
umushyikirano=open("kinyarwanda_stat/kinya_text/umushyikirano_gov.txt",encoding="utf8").read()
amategeko=open("kinyarwanda_stat/kinya_text/amategeko_gov.txt",encoding="utf8").readlines()


#print(spell(4545))  
kinyarwanda_text="inyarwanda ni ururimi rw' abanyarwanda  ruvugwa mu Rwanda hafi ijana kw' ijana".split()
english_text="English is a  great language that is spoken by many persons accross the globe".split()

# print("English adjectives", kinyarwanda_level(adj))
# print("principles by Bridgewater dude", kinyarwanda_level(principles))
#print( "A mix of French, Kinyarwanda and English", kinyarwanda_level(amategeko))
#print(ni_igihekane("nzw"))


#classs=[ ["umu","umw"],["aba","ab"],["umu","umw"],["imi","imy"],["i","iri"],["ama","am"],["iki","icy","igi"],["ibi","iby"],["i","in","inz"],['uru',"urw"],["aka","ak","aga"],["utu","utw","udu"],["ubu","ubw"],["uku","ukw",'ugu'],["aha","ah"]]



# print(miliyoni(100))
# number32=10060
# # for i in range(109990):
# # 	number32=i*89
# # 	print(million(number32))
# count_id=7803465
	
# print('{'+'"number"'+":"+'"'+str(number32) +'", "rw": "'+ miliyoni(number32) +'", ' +' "en": "'+million(number32).strip()+'"}')
# print('{'+'"number"'+":"+'"'+str(count_id) +'", "rw": "'+ miliyoni(count_id) +'", ' +' "en": "'+million(count_id).strip()+'"}')
# #print('{'+'"number"'+":"+'"'+ '%s'  +'", "rw": "'+ '%s' +'", ' +' "en": "'+'%s'+'"}'%(str(count_id),miliyoni(count_id),million(count_id).strip()))
# print(thousands(100))
# #import re
#word_lists=[]
#kinya_word_list=open("text/kinya_word_list.txt", 'w')
#adverb=re.findall(r"\w+ly", english_bible)

# for word in kinyarwanda_bible.split():

# 	#for word in sentence.split():
# 		#a=word in word_list
#  		#if word in word_list:
# 			# print(word)
# 	word_lists=word_lists+[word]
	#print(word)
#print(len(word_lists))

## I can just keep word for adjectives or etc and get most of adverbs 
## I can then implement its kinyarwanda adverb()
## or the other way around
## levering the power of regex 
def kinyarwanda_decomposition(word):
	### use the power of regular expressions to bring forth indomo+umusozo+root+other particles on text
	##using recognized set of roots(that can be manually or ...updated)
	##
	return 
		
# for  i in adverb:
# 	a=i[:len(i)-2]
# 	if a[len(a)-1]=="i":
# 		a=a[:len(a)-1]+"y"
# 	print(a, i)
# print(ubwinshi("igare"))
# for ijambo in amagambo:
# 	print(ijambo +" ==> "+ubwinshi(ijambo))

if __name__=="__main__":
	try:	
		#print("trying")
		functionx=str(argv[1])+"("+str(argv[2])+")"
		if functionx!="None":
			eval(functionx)
	except:
		print("except",argv)
		pass
		#print (argv [3])