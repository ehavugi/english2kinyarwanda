"""
	Tags can include all relevant information  like Kinyarwanda classes
 		For names and adjectives, adverbs and how to describe the
"""

#from kinyarwanda_test import *

adjectives=[]
nouns=[]

conjuctions=[", and",", but",", or",", although","that","which","neither","nor","although","after"]
verbs= ["be", "have","go","come","eat","etc"]
auxiliary_verb=["be","can","have",'must',"might","would","should"]

regular_verbs=["go","come","buy","sell","call","study","help","do","walk","burn","eat","speak","write","transform",
"remember","wait","add","say"]


#possible_tenses=["present","past","future"]

subjects=["i","you","he","she","it","we","you","they"]

def sentence_type(sentence):
	""" takes in a sentence with a punctuation and conclude about its type"""
	## it can help infer the same sentence type in corresponding type
	"""also word sequencing or verb forms can reveal some stuff
		"""
	if sentence.endswith("?"):
		return "question"
	if sentence.endswith("."):
		return "brabrah"
	if sentence.endswith("!"):
		return "exclamatory"
def object_the_actor(sentence):
	for i in sentence:
		if i=="by":
			return True


def sentence_mood(sentence):
	return "brabrah"
def is_special(word):
	"""
		with special words detection, I can devise a way to re-organize meanings as conjuctions connect idea or statements

	"""
	if word in conjunctions:
		return ["True","conjunction"]
	if word in auxiliary_verb:
		return ["True","auxiliary_verb"]
	if word in verbs: ## any other special ness
		return ["True","verb"]
	else:
		return False


def conj_have(subject,verb):
	if verb =="have":
		if subject in ["i",'you',"we","they"]:
			return  (subject, verb)
		else:
			return  (subject, "has")
	if verb=="be":
		if subject in ["you","we","they"]:
			#print(subject, "are")
			return (subject, "are")
		if subject=="i":
			return (subject, "am")
		if subject  in ['he',"she","it"]:
			return (subject, "is")

# for verb in verbs:
# 	for subject in subjects:
# 		conj_have(subject,verb)



# print(conj_have("i","be"))




def detect_special_verb(sentence):
	"""Assumption only one auxiliary verb"""
	for i in sentence:
		if i in verb_conj(axiliary_verbs):
			verb=detect_verb(i)
			tense=detect_tense(i)
			return [True,verb,tense]
def detect_verb(sentence):
	## one word level ## present, past(simple tenses)
	verbs=[]
	for word in sentence:
		if word is in_conjucted_verbs:
			## x for all verb conjugation in se
			verbs=verbs.append(x[verb])

	return verbs

def eng_conjugate_regular_verb(verb):


	def present_tense(verb):
		"""I  can store a varient. instead of all possibilities. to remove to be verbose"""
		
		subjects=["i","you","he","we","you","they"]
		conj=[] ## in order of sujects
		conj_unique=[]
		for i in subjects:
			if i in ["i","you","we","you","they"]:
				conj.append(i + " " + verb)
			elif i in ["he",'she',"it"]:
				if verb[len(verb)-1]=="o":
					verb3=verb+"e"
					conj.append(i +" " + verb3+"s")
				elif verb[len(verb)-1]=="y" and not(verb[len(verb)-2]  in "aioeu"):
					verb3=verb[:len(verb)-1]+"ies"
					conj.append(i+" "+ verb3)
				else:
					conj.append(i+" "+verb+"s")
				#print (conj)
		return conj
	return present_tense(verb)

econj=eng_conjugate_regular_verb
# for verb in regular_verbs:
# 	#continue
#     print(econj(verb))

a_sentence="is it true ?"
#print(sentence_type(a_sentence))
