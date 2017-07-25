"""
	get English tagged list and devise a kinyarwanda version using kinyarwanda sentence formation rules, word formation rules
	and compound sentence formation both in Kinyarwanda and English..

"""
try :
	from core.kinyarwanda_test import *
except:
	from kinyarwanda_test import *
#from EnglishTagging import *
### a person to learn from :: how did he do with kiswahili? can I get his progress by today and inform him any of my progress "http://keshav.is/building/swahili-translator/"
noun_examples=["umwana","abana","umurima","imirima","iriba","amariba","icyebo","ibyebo","inka","inzuzi","urukwavu","inkwavu",]
noun_class=["mu","ba","mu","mi","ri","ma","ki", "bi","n","n","ru","ka","tu","bu","ku","ha"]
subject_marker=["a","ba","u","i",""]
object_marker=["mu","ba",""] ### I can ask a person who know them

kinya_regular=['gend',"z","gur","gurish","hamagar","ig","fash","kor","gend","sha","ry","vug","andik","hindur","ibuk","tegerez","onger","vug"]
subjects_rw=["n","u","a","tu","mu","ba"]


def tense_marker(tense):
	if tense=="present":
		return ["ra","a"] ## nakubisse umwana ## ndahinga, urahinga, arahinga, turahinga,barahinga
	if tense=="past":
		return ["a", "e"]  ## narahinze, warahinze, barahinze,twarahinze,barahinze
	if tense=="future":
		return "inzagihe marker"  #nzahinga
	if tense=="x":
		return "x"
	else:
		return 
#print("example on each noun_class",len(noun_examples))
#print("noun class : ", len(noun_class))
#print("subject makers: ", len(subject_marker))
#print("object marker : ", len(object_marker))
 


def kinya_constr(list):
	"""
		construct kinyarwanda wording from list of english tagged lists:
		tags: verb, tense, subject=="with kinyarwanda classifier equi", object="with kinyarwanda classfier tag"

	"""
	return 
	
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
	if "uu" in constructed_word:
		word=word.replace("uu","wu")
	if "xy" in constructed_word:
		return "do this, that"
	if "io" in constructed_word:
		word=word.replace("io","yo")
	if 'ai' in constructed_word:
		word=word.replace("ai","i")
	if "nr" in constructed_word:
		word=word.replace("nr","nd")
	if "aa" in constructed_word:
		word=word.replace("aa","a")

	## iyandika bihekane  (n)kw,(n)gw,hw --o,u
	if "kwo" in constructed_word :
		word=word.replace("nkwo","nko")
	if "kwu" in  constructed_word:
		word=word.replace("nkwu","nku")
	if "gwo" in constructed_word:
		word=word.replace('ngwo',"ngo")
	if "gwu" in constructed_word:
		word=word.replace("ngwu","ngu")
	if "hwu" in constructed_word:
		word=word.replace("hwu","hu")
	if "hwo" in constructed_word:
		word =word.replace("hwo","ho")
## iyandikwa rya (n)jy, (n)cy, i , and e
	if "jyi" in constructed_word:
		word=word.replace("jyi","gi")
	if "jye" in constructed_word:
		word=word.replace("jye",'ge')
	if "cyi" in constructed_word:
		word=word.replace("cyi","ki")
	if "cye" in constructed_word:
		word=word.replace("cye","ke")
	return word

	if kinyarwanda_level([word])>0.8:
		return word
	else:
		return 

## Kinyarwanda auto_conjugation

inshinga=["ba","gir",""]  ## roots, I have to get roots and autogenerate

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
	if tense=="past":
		ending="ye"
	constructed=subject+tense_markers[tense]+objects+stem+ending
	return uturemajambo(constructed)

possible_tenses=["present","past","future"]

# for verb in kinya_regular:

# 	for a in subjects_rw:
# 		#continue
# 		for tense in possible_tenses:
# 				#continue
# 				print (a, verb,tense,":" , kiny_conjugate(verb,a,"",tense))