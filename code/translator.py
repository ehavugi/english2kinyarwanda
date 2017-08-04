import re
import os
#os.path.abspath("c:/english2kinyarwanda/code")
phrases_morgan=open("c:/english2kinyarwanda/kinyarwanda_stat/eng_kinya/phrases_morgan.txt",encoding="utf8").read()
me=open("c:/english2kinyarwanda/kinyarwanda_stat/eng_kinya/kinya_eng_me.txt",encoding="utf8").read()
try:
	from code.number2words import tiliyoni
except:
	from number2words import tiliyoni
texts=phrases_morgan+me
texts=texts.split("\n")
phr={}
for line in texts:
	line=line.strip().split("|||")
	if len(line)>1:
		phr[line[0].strip().lower().replace(" ","")]=line[1]
#print(phr)
#import nltk
special=[", and", ", but",", or"," and "]
def translate(sentence):
	sentence1=""
	# try:
 	# 	number=int(sentence)
	# 	return tiliyoni(number)
	# except:
	# 	pass
	for i in re.split("[^a-zA-Z]",sentence):
		sentence1+=i
	
	for word in special:
		if word in sentence1: ## and constraints --like sentence consistence is fullfilled
			return handle_special(sentence1, word)
	try:
		sentence=sentence1
		return phr[sentence.lower().strip().replace(" ","")]
	except:
		return  sentence
		#print(i[0].strip().lower())
		# try:
		# 	print(i[1])
		# except:
	# 	# 	pass
	# 	# finally:
	# 	# 	pass
	# 	if word.strip().lower()==i[0]:
	# 		i_found=i

	# 	#print(word.strip().lower(),str(i_found[0].strip().lower()))
	# 		#return True 
	# #print("hell")
	# #return "wapi"
	# return i_found
# print(translate("good afternoon"))
def handle_special(sentence,word):
	sentence_s=sentence.split(word)
	if word==", and " or word=="and":
		return translate(sentence_s[0])+" na "+ translate(sentence_s[1])
	if word==", but":
		return translate(sentence_s[0])+" kandi "+ translate(sentence_s[1])
	
#print(translate("happy birthday"))

def handle_plural(word):
	"""
	 handling plural forms of words that are not in dictionary, in their plural forms
	
	1. layer of checking may be added, e.g looking if the formed words exist in monolingual dict
	2. +++ other ways to go around this

	3. I can also try handling other words say be opposite, adding "s" and then invoking ubumwe on the returned results 
	 which I can the cross check in monolingual dictionary for confidence in my results
	 
	"""
	if word.endswith("s"):
		try :
			new_word=word[:len(word)-1]
			new_word_t=translate(new_word)
		except:
			pass

		try:
			word=ubwinshi(new_word_t)
		except:
			pass
	return word

def handle_past(verb):
	"""
	template for handling pasts forms that are not recognized in dictionary
	but are derivatives of a verb that is recognized
	
	"""

	if verb.endswith("ed"):
		try:
			new_verb=verb[:len(verb)-2]
			new_verb_t=translate(verb[:len(verb)-2])
		except:
			pass
		try:
			verb=conjugate(verb,past)
		except:
			pass
		return verb
