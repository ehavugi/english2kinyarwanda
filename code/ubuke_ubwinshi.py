def word_in_kinyarwanda(word):
		return False
def post_processor(word):
	## can be used say to conclude if the word already exists which can boast 
	#the confidence in the return value
	## Say, I can use to decide whether to return a word with a flag that it
	## I don't have its occurance in literature(in my database)
	if not is_kinyarwanda(word):
		return uturemajambo(word)## syntax wise
	if word_in_kinyarwanda(word):
		return word
	else:
		return word
		#do something else
## it seems to me away to first decompose the word and then do analysis after can be better
def ubwinshi(ijambo):
	"""should take a word (ijambo) in singular and return its plural form"""
	if ijambo=="wa":
		return "ya"  ##Or ba (depending class of nearby word)
	if ijambo.startswith("si"):
		return "si"+ubwinshi(ijambo[2:])
	if ijambo.startswith("ubw") or ijambo.startswith("ubu"):
		## ubwoko ==> amoko, ubwato==>amato,etc
		return "ama"+ijambo[1:]
	if ijambo.startswith("umu") or ijambo.startswith("umw"):
		##umwana==> abana, umwami==>abami
		## umunyeshuri==>abanyeshuri
		ijambo1="aba"+ijambo[3:]
		ijambo2="imi"+ijambo[3:]
		if word_in_kinyarwanda(ijambo2):
			return ijambo2
		else: return ijambo1
	if ijambo.startswith("igi") or ijambo.startswith("iki"):

		##Igikorwa==>ibikorwa, igiti ==>ibiti
		#igice ==> ibice
		#igiti ==>ibiti
		return "ibi"+ijambo[3:]
	if ijambo.startswith("icya"):
		return "ibya" +ijambo[4:]
	
	if ijambo.startswith("uku"):
		return "ama"+ijambo[3:]
	if ijambo.startswith("ak"):
		return "utu"+ijambo[3:]
	if ijambo.startswith("in"):
		return ijambo
	if ijambo.startswith("uru"):
		return "in"+ijambo[3:]
	if ijambo.startswith('ya'):
		return "za"+ijambo[2:]
	if ijambo.startswith("wa"):
		return "ba"+ijambo[2:]
	if ijambo[0] in ["ioeau"]:
		return ijambo[0]+ubwinshi(ijambo[0:])
	if ijambo.startswith("i"):
		return "ama"+ijambo[1:]
	if ijambo.startswith("u"):
		return "mu"+ijambo[1:]
	if ijambo.startswith("n"):
		return "tu"+ijambo[1:]
	if ijambo.startswith("ara"):
		return "bara"+ijambo[3:]
	if ijambo.startswith("ura"):
		return "mura"+ijambo[3:]
	if ijambo.startswith("nda"):
		return "tura"+ijambo[3:]
	if ijambo[0] in ["ioeau"]:
		return ijambo[0]+ubwinshi(ijambo[0:])
	
	else:
		return ""





amagambo=["urugo","urugero","umwana","ikinyarwanda",
"ndagushimiye","urashaka","icyaha","umuntu",
"icyayi","ubwato","icyabitse"
,"icyebo","igitabo",'urakora',"sinumva","ariko",
"inyugu","inyoni","inka",
"mfasha"
"umugabo","umugore","umusore",'umukobwa',
"arakora","ndakora","urakora",
"umugabo","umugora","umwigisha","umusaza","umukiza","yange","wange","wandebeye"]

for ijambo in amagambo:
	print(ijambo +" ==> "+ubwinshi(ijambo))


