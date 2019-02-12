bible_en=open("../kinyarwanda_stat/kinya_text/kjv.txt").readlines()
verbs=["buy","pray","say","find","search"]
lines=0
words=[]
import nltk
"""a dictionary with words --linked to list of sentences that it appears $$
or List of lists 
"""

for line in bible_en:
	
	for word in line.split():
		#print(word)
		if not  (word in words):
			words.append(word)
			#print (word)
len(words)
		