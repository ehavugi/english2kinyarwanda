"""
	(In development to acheive this spec)
This is an attempt to tell if a word is well written kinyarwanda or not
it is to catch wrong than right as infinitely  many right kinyarwanda words can exist and words that
 respect all word formation in Kinyarwanda may still not be kinyarwanda.
 It can be adapted to print some words that may be badly written or to detect kinyarwanda language


Kinyarwanda is Beautifully written in such way that I can parse the text and tell if words comprising the text are written or can be read as 
kinyarwnada(not necessary about meaning --syntax checking)
	Inyajwi, 
	ibihekane
	nta nyajwi zikurikirana mu ijambo
	nibyindi byakwifashishwa
reference primary 1,2 and 3 Kinyarwanda
"""

"""  on Kinyarwanda_level :: 
		it return a number between 0 and 1, with 1 as most kinyarwanda looking text
			## I tried to minimize size of depedencies(it only depend on a
			## list of consonants rather than a list of all words or common words)

	another Implemementation that I guess others to explore and compare efficiencies is
 	using word comparision or word statistics and infer the Language as most of the time the words 
 	Like "the","a","can", etc are more in English than French, Kinyarwanda

 	the like is for kinyarwanda,word stat can be great for large text as trying to go around splitting 
 	@ consonant level can be longer than at word level..

 	### Any way to infer if a text is kinyarwanda or not can be of same functionality as this...
 	## also having different way to cross check with different methods where high accuracy is needed can be great
	# coupling syntax and dictionary search can assure high accuracy(this is where redudancy can be great)

##One of  applications of a test like this is:
	+  (sorting texts)
		A web scrawling application for kinyarwanda word /text collection on web 
			(as a website can have different pages ones in English, other in Kinyarwanda)."""

kinya=open("kinya.txt").readlines()

vowels=["a","i","o","e","u"]
inyajwi=vowels ## for using either of words for reference(Convinient,though dangerous)
imibare="0123456789"
numbers=imibare
consonants=["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t", "q","w","v","y","z"]
ingobajwi=consonants
ibihekane2=["cy","nd","by","bw","mw","mv","mb","nw","mp","ns","nk","rw","pw","my","tw","dw","cw","nj","nz","gw","pf","mf","sy","ry"]
ibihekane3=["nny","mbw","nshy","nshw","nzw"]
ibihekane4=["shyw",""]
#ibihekane=ibihekane2+ibihekane3+ibihekane4+ibihekane_bruce
ibihekane_bruce_version0=["nny","shyw","ngw","mby","mp",
						"kw","cy","ny","sh","nshyw",
						"ry","nyw","shy","nd","ndw",
						"njy","nj","ndy","mbw",
						"bw","pf","ngw","gw","hw",
						"nt","rw","ns","nc","tw","shw",
						"nshw","nsh","nty","mpy","nsh","ncw",
						"mbyw","mvw","ncy"
						]

ibihekane_bruce=["by","mb","mby","mby","nc","nd","ndy","ndw","mby","pf","ngw","gw","ng","hw","ny","nyw","jy","mv","myw","nz",
				"nny","nw","nk","mp","shy","shyw","ny","nshy","mpw","mpw","nshyw","mby","mw","fw","ncw","py","nyw","shy","sh","hw",
				"ns","gw","nshyw","tsw","ts","nt","ntw","nkw","kw","nk","sy","sw","mbyw","mbw","mby","ncy","ns","sh"
				]
ibihekane=[]

for i in ibihekane2+ibihekane3+ibihekane4+ibihekane_bruce+ibihekane_bruce_version0:
	if not (i  in ibihekane):
		ibihekane.append(i)
utwatuzo=[";",".", " ", " "]
punctuation=utwatuzo
## it is possible to train or get ibihekane from a document and learn new ibehakane warabyibagiwe, noneho ukongera ibihekane muri list 
#umaze kwemeza ko ari ibehekane
#consonants_combo=[]
#consonants_combo=[" ","","\n"]
#consonants_combo.append(utwatuzo)
#consonants_combo.append(vowels)
#consonants_combo.append(consonants)
#consonants_combo.append(ibihekane2)
def consonants_in(kinyaR):
	""""takes a list of words and return consonants combinations
		#split word with space, vowels, and then get out constants combinations..
		"""
	#kinyaR=kinyaR.split()

	consonants_combo=[] ##I had it outside at first and was messing up results that were called successively 
	for a in kinyaR:
		a=a.lower().strip()
		#if a in ["aioue"]:
		a=a.split(" ")
		#a=a.split("i")
		#print(a)
		for i in a:
			k=i.split("i")
			for b in k:
				c=b.split("o")
				for d in c:
					g=d.split("u")
					#print(g)
					for h in g: 
						m=h.split("a")
						#print(m)
						for j in m:
							q=j.split("e")
							#print(q)
							for i in q:
								consonants_only=True
								b.strip()
								for b in i:
									if b not in consonants or (b in imibare):
										consonants_only=False
								if consonants_only:
									if not ( i in consonants_combo or  ( i in imibare)) :				
										consonants_combo.append(i)
										#print(i, " rw")
									
									else:
										consonants_combo.append(i)
										#print(i, "  kinya")
								else:
									continue
									#print(i, "not consonants only")
						#print(q)
	return consonants_combo
#print(consonants_combo)
#print("inyajwi : ", len(vowels))
#print ("ingobajwi : ",len(consonants))
#print ("ibihekane by'ingobajwi ebyiri : ", len(ibihekane2))
#print("ibihekane nahawe na Bruce, wiga muwa gatatu mu mashuri abanza version 0 : ",len(ibihekane_bruce_version0))
#print("ibihekane nahawe na Bruce, wiga muwa gatatu mu mashuri abanza : ",len(ibihekane_bruce) ," ", ibihekane_bruce)

#print (consonants_in(["kinyarwanda ni ururimi ryiza. abana n'abantu bakuru bagomba kurugira urwabo"," "]))

#print((consonants_in (kinya)))


def ni_igihekane(word):
	"""
		takes a string and return True if string is  igihekane, False otherwise
		For example  ni_igihekane("nx"), will return False, while ni_igihekane("ng") will return True

	"""
	if word in ibihekane:
		return True
	else:
		return False

def is_kinya_consonant_combo(word):
	"""
		takes in a string without vowels and decide if it is a good consonant combination in kinyarwanda
	"""
	if word in ibihekane+vowels+consonants+ [" ","\n","::"] or word in numbers:
		return True
	else:
		return False
is_igihekane=ni_igihekane

def kinyarwanda_level(texts):
	"""
		Kinyarwanda_level returns the  a number between 0 and 1 level of  kinyarwanda_ness  
		for example kinyarwanda-level(["inyarwanda ni indirimbo nyarwanda"]) returns 1.0

		by syntax, not by semantics in any sense. it can be used to tell if a document after clearning is kinyarwanda or not, you can add twist to it and be more effective major
		to decide if a document is not in Kinyarwanda if it has a lower number after good cleaning of punctuations, or strange symbols
	"""
	count=0
	total=0

	## how i can decide it is not kinyarwanda(if it ends with a constant) a test like that
	# for word in texts:
	# 	if word[len(word)-1] in consonants:
	# 		count+=1
	# 		text=text.remove(word)
	for i in (consonants_in(texts)):
		if len(i)>1:
			total+=1
			if is_kinya_consonant_combo(i):
				count+=1
			else:## Switch, continue for not printing the consonants combination , comment to see the combinations that are failing 
				continue
				#print(i)
	#print("count : ", count, "\n", "total : ", total,"\n", "percentage :", count/total*100,"%")
	return count/total  ## how to escape zerodevision errors?

	