##numbering
"""
 This number2words includes functions to translate numbers into Kinyarwanda wording, for phone, for buying stuff, interacting banks where by confirming 
 by wording or speaking is neccessary.

 Especially can be helpful as reference for correct writing of numbers in Kinyarwanda:
 	+ currently, it does not support class modifiers which can be great ---> it may be added to other versions
 	+ it will have interface names available in Kinyarwanda and English for easy use of nmemonic names of functions
 

 future versions may include or may help implement:
 	1. add voice for autamatic spelling of nembers and phone mumber speaking
 	2. Add phone checking on top of spelling and telling the network "Tigo,Airtel,MTN" and countries
 	3.

"""


basic0={"0":"zero","1":"rimwe","2":"kabiri","3":"gatatu", "4":"kane","5":"gatanu",
		"6":"gatandutu","7":"karindwi","8":"umunani","9":"icyenda"}
basic3={"1":"kimwe","2":"bibiri","3":"bitatu","4":"bine","5":"bitanu","6":"bitandatu","7":"birindwi","8":"umunani","9":"icyenda"}
basic6={"1":"imwe","2":"ebyiri","3":"eshatu","4":"enye","5":"eshanu", "6":"esheshatu","7":"zirindwi","8":"umunani","9":"icyenda"}
basic9=basic6
basic12=basic6
tens={"0":"", "1":"icumi","2":"makumyabiri","3":"mirongo itatu","4":"mirongo ine","5":"mirongo itanu",
		"6":"mirongo itandatu","7":"mirongo irindwi","8":"mirongo inani","9":"mirongo icyenda"}
hundreds={"0":"", "1":"ijana","2":"magana abari","3":"managana atatu","4":"magana anane","5":"magana atanu",
			"6":"magana atandatu","7":"magana arindwi","8":"magana umunani","9":"magana icyenda"}
thousands=["","igihumbi","ibihumbi biri","ibihumbi bitatu","ibihumbi bine","ibihumbi bitanu","ibihumbi bitandatu",
			"ibihumbi birindwi","ibihumbi umunani","ibihumbi icyenda","ibihumbi icumi"]
millions=["", "miliyoni imwe","miliyino ebyiri","miliyoni eshatu","miliyoni enye","miliyoni eshanu","miliyoni esheshatu","miliyoni zirindwi","miliyoni umunanani"," miliyoni icyenda"]
 
billion=["miliyari", "imiliyari ebyiri","eshatu","enye","eshanu","esheshatu","zirindwi","umunani","icyenda"]
trillion=["tiliyoni","tiliyoni ebyeri","eshatu","enye","eshanu","esheshatu","zirindwi","umunani","icyenda"]
#level=["basic","tens","hundrends","thousands"]

inputs= "0722765359"

basic=[basic0,basic3,basic6,basic9,basic12]

# for i in range(10):
# 	b=i
# 	print (basic[str(i)])
# 	print(tens[str(b)])
# 	print(hundreds[str(i)])
def spell(inputs):
	number=len(str(inputs))
	print(number)
	for i in str(inputs):
 		print(basic[str(i)])


def amajana(inputs,urugero=0):

	"""
		amajana takes a number from 0 to 999 and write outs its kinyarwanda wording eg: 1 -->rimwe, 
		801 ---> magana umunani na rimwe .. it is still under developments( you can submit bugs or
		suggestions at ehavugi@mit.edu) if found before 2020

	"""
	inputs=str(inputs)
	assert (len(inputs)<4)#,"Not less than 999. Umubare nuri musi ya 999")
	# if int(inputs[0])==0:
	# 	inputs=inputs[1:(len(inputs)-1)]

	if len(inputs)==1:
		return (basic[urugero][str(inputs)])
	if len(inputs)==2:
		if int(inputs[1])==0:
			return (tens[str(inputs[0])])
		if int(inputs[1]) in [8,9]:
			return (tens[str(inputs[0])]+' n \' '+basic[urugero][str(inputs[1])]) ## to use punctuation n' before a vowel
		else:
			return (tens[str(inputs[0])]+' na '+basic[urugero][str(inputs[1])])
	else:
		if int(inputs[2])==0:
			if int(inputs[1])==0:
				return(hundreds[str(inputs[0])])
			else:
				return (hundreds[str(inputs[0])]+" na "+tens[str(inputs[1])])
		if int(inputs[2]) in [8,9]:
			if int(inputs[1])==0:
				return(hundreds[str(inputs[0])]+" n' "+ basic[urugero][str(inputs[2])])  ## A person can also implement punctuation rules a different manner
			else:
				print()
				return(hundreds[str(inputs[0])]+" na "+tens[str(inputs[1])]+" n' "+ basic[urugero][str(inputs[2])])
		else:
			if int(inputs[1])==0:
				return(hundreds[str(inputs[0])]+" na "+ basic[urugero][str(inputs[2])])
			else:
				return(hundreds[str(inputs[0])]+" na "+tens[str(inputs[1])]+" na "+ basic[urugero][str(inputs[2])])

#spell(inputs)
# vuga=spell
# imibare=inputs
# vuga(imibare)
def ibihumbi(inputs):
	"""
		built to take inputs as number from 0 to 999,999 and return rwanda wording
		net yet stable ... :

		issues to fix:"grammar"
		igihumbi na  na mirongo itatu 1030
		igihumbi na  na mirongo itatu na rimwe 1031
		igihumbi na  na mirongo itatu na kabiri 1032

	"""
	inputs=str(inputs)
	assert len(inputs)<7
	if len(inputs)<4:
		return (amajana(inputs))
	else:
		if len(inputs)==4:
			if int(inputs[1])==1:
				return (thousands[int(inputs[0])]+" n \'"+amajana(inputs[1:4]))
			else:
				return "ibihumbi "+amajana(inputs[0:(len(inputs)-3)],1)+" na "+amajana(inputs[len(inputs)-3:len(inputs)])
		elif len(inputs)>4:
			return "ibihumbi "+amajana(inputs[:(len(inputs)-3)],1)+" na "+amajana(inputs[len(inputs)-3:len(inputs)])

def miliyoni(inputs):
	inputs=str(inputs)
	assert len(inputs)<10
	if len(inputs)<7:
		return ibihumbi(inputs)
	else:
		if len(inputs)==7:
			#if input[1:7]>0:
			return millions[int(inputs[0])]+ ibihumbi(inputs[1:7])
		elif len(inputs)>7:
			return "miliyoni"+" "+  amajana(inputs[:len(inputs)-6],2)+" " + ibihumbi(inputs[len(inputs)-6:len(inputs)])  

hundred_s=amajana


## templates for functions to seek support or work on(no guarantee they will be built or are possible)


def phone(number):
	"""for phone number functionalities, including country code recognition,etc(type of things)"""
	return  
def speak(number):
	"""with audio files for basic numbers, is it possible to combine the numbers and get sounds for any
	 number up to our desire number
	"""
	return 


# print(amajana("999"),999)
# for i in range(100000,120000):
# 	print (i, ":" , miliyoni(i))

# #print(hundred_s(98))
# # for i in range(2000):
# # 	print(ibihumbi(i),i)


# ## On text to speech Kinyarwanda
# #http://people.csail.mit.edu/hubert/pyaudio/docs/
# #If there a way to concatenates audios, I can record voices for each letter combination (50-60*5=200, to 300 audio files and play back them concatenate with some delays or speed up

# print(miliyoni(465656478))


## i will have to fix na repeatability and na  ijana (and same issues)
 
# 100000 : ibihumbi ijana na 
# 100001 : ibihumbi ijana na  na rimwe
# 100002 : ibihumbi ijana na  na kabiri
# 100003 : ibihumbi ijana na  na gatatu
# 100004 : ibihumbi ijana na  na kane



# 100106 : ibihumbi ijana na ijana na gatandutu
# 100107 : ibihumbi ijana na ijana na karindwi
# 100108 : ibihumbi ijana na ijana n' umunani
# 100109 : ibihumbi ijana na ijana n' icyenda
# 100110 : ibihumbi ijana na ijana na icumi


# 100106 : ibihumbi ijana na ijana na gatandutu
# 100107 : ibihumbi ijana na ijana na karindwi
# 100108 : ibihumbi ijana na ijana n' umunani
# 100109 : ibihumbi ijana na ijana n' icyenda
# 100110 : ibihumbi ijana na ijana na icumi