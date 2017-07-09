"""
 Get sentence and translate it
"""
import nltk
def translate(sentence):
	for word in special:
		if word in sentence: ## and constraints --like sentence consistence is fullfilled
			return handle_special(sentence, word)
	if sen:
		print("hell")

print("wow")


special=[", and", ", but",", or", ]

def handle_special(sentence,word):
	sentence_s=sentence.split(word)
	if word==", and ":
		return translate(sentence_s[0])+" na "+ translate(sentence_s[1])
	if word==", but":
		return translate(sentence_s[0])+" kandi "+ translate(sentence_s[1])