""" 	  
 kinyarwanda_test comprise of functions on testing kinyarwanda_ness (syntactically)
 main function kinyarwanda_level that return a float between 0 and 1
"""
vowels=["a","i","o","e","u"]
imibare=["0","1","2","3","4","5","6","7","8","9"]
consonants=["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t", "q","w","v","y","z"]
ibihekane=["ny","sh","pf","ts",
"mb","mf","mp","nd","ng","nk","ns","nsh","nshy","nt","nt","nz",
"bw","bg","cw","dw","fw","gw","hw","jw","kw","mw","nw","nyw","pfw","pw","rw","shw","shyw","sw","tsw","tw","vw","zw",
"by","cy","jy","my","nny","pfy","py","ry","sy","ty","vy",
"byw","myw","pfyw","ryw","vyw",
"mbw","mfw","mpw","mvw","ndw","ngw",
"njw","nkw","nkw","nshw","nshyw","nsw","ntw","nzw","ntw","nzw",
"mby","mpy","mvy","ncy","ndy","njy","nsy","nty",
"mbyw","mvyw","njyw"]

utwatuzo=[".", "?", "!",",","...",":",";",'" ',"(",")","-","[","]","/"]

def consonants_in(kinyaR):
	""""takes a list of words,  and return consonants combination """
	consonants_combo=[]
	for a in kinyaR:
		a=a.lower().strip()
		# if i in "aioeu":
		# 	a=a.replace(i,",")

		a=a.split(" ")
		for i in a:
			k=i.split("i")
			for b in k:
				c=b.split("o")
				for d in c:
					g=d.split("u")
					for h in g: 
						m=h.split("a")
						for j in m:
							q=j.split("e")
							for i in q:
								consonants_only=True
								for b in i:
									if b not in consonants or (b in imibare):
										consonants_only=False
								if consonants_only:
									if not ( i in consonants_combo or  ( i in imibare)) :				
										consonants_combo.append(i)							
									else:
										consonants_combo.append(i)
								
								else:
									continue
									
	return consonants_combo


def ni_igihekane(word):
	"""	takes a string and return True if string is  igihekane, False otherwise
		For example  ni_igihekane("nx"), will return False, while ni_igihekane("ng") will return True """
	if word in ibihekane:
		return True
	else:
		return False

def is_it_kinya_consonant_combo(consonant_sequence):
	if consonant_sequence in ibihekane+vowels+consonants+imibare+[" ","\n","::"]:
		return True
	else:
		return False

def kinyarwanda_level(texts):
	"""	Kinyarwanda_level takes in a text returns the  a number between 0 and 1 level of  kinyarwanda_ness  
		for example kinyarwanda-level(["inyarwanda ni indirimbo nyarwanda"]) returns 1.0"""
	count=0
	total=0
	for i in (consonants_in(texts)):
		if len(i)>1:
			total+=1

			if is_it_kinya_consonant_combo(i):
				count+=1
			else:
				continue
	try:
		return count/total 
	except:
		if len(texts)>=3:
			for i in texts:
				if not(i in consonants+vowels):
					return 0
			return 1
		else:
			return 0


# print(kinyarwanda_level(["English is great language"]))
#print(kinyarwanda_level(["Ikinyarwanda ni n'icya mbere"]))
