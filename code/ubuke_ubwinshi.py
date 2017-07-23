from making_kinyarwanda import uturemajambo
def word_in_kinyarwanda(word):
		return False
def post_processor(word):
	## can be used say to conclude if the word already exists which can boast 
	#the confidence in the return value
	## Say, I can use to decide whether to return a word with a flag that it
	## I don't have its occurance in literature(in my database)
	if not is_kinyarwanda(word):
		return uturemajambo(word)## syntax wise
	else:
		return word
		
## it seems to me away to first decompose the word and then do analysis after can be better
replacements0={"wa":"ya", 	"ubw":"ama",	"ubu":"ama","umu":"aba","umwa":"aba",
"ig":"ib","nda":"tura","yange":"zange","m":"","ik":'ib',"ura":"mura",
"ar":"bara","icy":"iby","aka":"utu"}


def ubwinshi1(ijambo):
	"""should take a word (ijambo) in singular and return its plural form"""
	#pronouns=
	for i in replacements0:
		if ijambo.startswith(i):
			return ijambo.replace(i,replacements0[i])	
	
	if ijambo.startswith("uku"):
		return "ama"+ijambo[3:]
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
	
	
	if ijambo[0] in ["ioeau"]:
		return ijambo[0]+ubwinshi(ijambo[0:])
	# if "da"==ijambo[1:3]
	
	else:
		return ijambo


def ubwinshi(word):
	return uturemajambo(ubwinshi1(word))


amagambo={"urugo":"ingo","urugero":"ingero","umwana":"abana",
"ikinyarwanda":"ibinyarwanda","icyaha":"ibyaha","umuntu":"abantu","icyayi":"ibyayi",
"ubwato":"amato","icyabitse":"ibyabitse","icyebo":"ibyebo","igitabo":"ibitabo",
"urakora":"murakora","inyungu":"inyungu","inyoni":"inyoni","inka":"inka",
"umugabo":"abagabo","arakora":"barakora","ndakora":"turakora","urakora":"murakora","imana":"imana"}


examples={"umuntu":"abantu","ikintu":'ibintu',"ahantu":"ahantu","icyatsi":"ibyatsi"}
count=0
total=0
for x in amagambo.keys():
	total=1+total
	if ubwinshi(x)==amagambo[x]:
		count+=1
	else:
		print(x,ubwinshi1(x),ubwinshi(x))

print(count/total)



