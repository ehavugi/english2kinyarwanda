import re
import os
#os.path.abspath("c:/english2kinyarwanda/code")
phrases_morgan=open("c:/english2kinyarwanda/kinyarwanda_stat/eng_kinya/phrases_morgan.txt",encoding="utf8").read()
me=open("c:/english2kinyarwanda/kinyarwanda_stat/eng_kinya/kinya_eng_me.txt",encoding="utf8").read()

#from .number2words import tiliyoni
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