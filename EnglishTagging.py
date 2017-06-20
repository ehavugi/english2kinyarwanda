"""
	Tags can include all relevant information  like Kinyarwanda classes
 		For names and adjectives, adverbs and how to describe the
"""
from kinyarwanda_test import *
verb_roots=open("verb_roots.txt")


adjectives=[] ## list of english adjectives as list of lists with first element being the adjectives, second the noun class relevant to it(or be dangling, "")

nouns=[] ## with name classes tages
conjuctions=["and","but","or","although","that","which","neither","nor","although","after"]
## english prototype
verbs= ["be", "have","go","come","eat","etc"] #with verbs roots, It can be great to have them in a file or data base with some way of saying which root corresponding to the verbs
auxiliary_verb=["be","can","have",'must',"might","would","should"]

## Regular verb patterns can be captured(with tenses)
## with corresponding kinyarwanda verbs(all verbs tenses can be matched and the conjugate kinyarwanda on fly)

regular_verbs=["go","come","buy","sell","call","study","help","do","walk","burn","eat","speak","write","transform",
"remember","wait","add","say"]
kinya_regular=['gend',"z","gur","gurish","hamagar","ig","fash","kor","gend","sha","ry","vug","andik","hindur","ibuk","tegerez","onger","vug"]
subjects_rw=["n","u","a","tu","mu","ba"]

possible_tenses=["present","past","future"]

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

for verb in verbs:
	for subject in subjects:
		conj_have(subject,verb)


## Kinyarwanda auto_conjugation

inshinga=["ba","gir",""]  ## roots, I have to get roots and autogenerate





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
				conj.append(verb)
			elif i in ["he",'she',"it"]:
				if verb[len(verb)-1]=="o":
					verb3=verb+"e"
					conj.append(verb3+"s")
				elif verb[len(verb)-1]=="y" and not(verb[len(verb)-2]  in "aioeu"):
					verb3=verb[:len(verb)-1]+"ies"
					return verb3
				else:
					conj.append(verb+"s")
				#print (conj)
		return conj
	return present_tense(verb)


for verb in regular_verbs:
	continue
	#print(eng_conjugate_regular_verb(verb))


def uturemajambo(constructed_word):

	"""this takes in a word made up of constituents, subject,object infixes,suffixes,or prefexies,tenses,etc)
	in the right order and make up a replace based on uturamajambo rules"""
	### Rules like this one {I think can be used at advantage of automation}
	## u→w/-j
	## a→ф/-j
	## 

	## I can nest ifs or include exceptions to these rules (if they can be coded)
	# with exceptions being handled before general case take care of them
	word=constructed_word
	if "ia" in constructed_word:
		word=word.replace("ia","ya")
	if "ua" in constructed_word:
		word=word.replace("ua","wa")
	if "xy" in constructed_word:
		return "do this, that"
	if "io" in constructed_word:
		word=word.replace("io","yo")
	if 'ai' in constructed_word:
		word=word.replace("ai","i")
	if "nr" in constructed_word:
		word=word.replace("nr","nd")
	if "aa" in constructed_word:
		word=word.replace("aa","ya")

	return word

	if kinyarwanda_level([word])>0.8:
		return word
	else:
		return 





def kiny_conjugate(stem,subject="a", objects="",tense="present",ending="a"):
	""" this function can take kinyarwanda verb root, subjec, object, and tense
		and then construct a sequence of word that can be post processed by 
		an uturemajambo rule enforcement agency"""
	tense_markers={"present":"a","past":"ra","future":"za","perfect_present":" ","perfect_past":""}
	#print(type(tense_markers[tense]))
	#print(type(stem))
	#print(type(objects))
	#print(type(subject))

	## present(stem,suject,objects):
		## any dependence may be tried and constructed
	constructed=subject+tense_markers[tense]+objects+stem+ending
	return uturemajambo(constructed)


for verb in kinya_regular:

	for a in subjects_rw:
		#continue
		for tense in possible_tenses:
				continue
				#print (kiny_conjugate(verb,a,"",tense))


a_sentence="is it true ?"
#print(sentence_type(a_sentence))
