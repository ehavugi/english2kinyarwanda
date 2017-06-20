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


basic={"0":"zero","1":"rimwe","2":"kabiri","3":"gatatu", "4":"kane","5":"gatanu",
		"6":"gatandutu","7":"karindwi","8":"umunani","9":"icyenda"}
tens={"0":"", "1":"icumi","2":"makumyabiri","3":"mirongo itatu","4":"mirongo ine","5":"mirongo itanu",
		"6":"mirongo itandatu","7":"mirongo irindwi","8":"mirongo inani","9":"mirongo icyenda"}
hundreds={"0":"", "1":"ijana","2":"magana abari","3":"managana atatu","4":"magana anane","5":"magana atanu",
			"6":"magana atandatu","7":"magana arindwi","8":"magana umunani","9":"magana icyenda"}
thousands=["","igihumbi","ibihumbi biri","ibihumbi bitatu","ibihumbi bine","ibihumbi bitanu","ibihumbi bitandatu",
			"ibihumbi birindwi","ibihumbi umunani","ibihumbi icyenda","ibihumbi icumi"]

level=["basic","tens","hundrends","thousands"]

inputs= "0722765359"


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


def amajana(inputs):

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
		return (basic[str(inputs)])
	if len(inputs)==2:
		if int(inputs[1])==0:
			return (tens[str(inputs[0])])
		if int(inputs[1]) in [8,9]:
			return (tens[str(inputs[0])]+' n\' '+basic[str(inputs[1])]) ## to use punctuation n' before a vowel
		else:
			return (tens[str(inputs[0])]+' na '+basic[str(inputs[1])])
	else:
		if int(inputs[2])==0:
			if int(inputs[1])==0:
				return(hundreds[str(inputs[0])])
			else:
				return (hundreds[str(inputs[0])]+" na "+tens[str(inputs[1])])
		if int(inputs[2]) in [8,9]:
			if int(inputs[1])==0:
				return(hundreds[str(inputs[0])]+" n' "+ basic[str(inputs[2])])  ## A person can also implement punctuation rules a different manner
			else:
				return(hundreds[str(inputs[0])]+" na "+tens[str(inputs[1])]+" n' "+ basic[str(inputs[2])])
		else:
			if int(inputs[1])==0:
				return(hundreds[str(inputs[0])]+" na "+ basic[str(inputs[2])])
			else:
				return(hundreds[str(inputs[0])]+" na "+tens[str(inputs[1])]+" na "+ basic[str(inputs[2])])

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
				return (thousands[int(inputs[0])]+" na "+amajana(inputs[1:4]))
		if len(inputs)==5:
			print("ibihumbi"+ "----")
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


#print(amajana("999"),999)
# for i in range(1000):
# 	print (amajana(i)," : ", i)

#print(hundred_s(98))
# for i in range(2000):
# 	print(ibihumbi(i),i)


## On text to speech Kinyarwanda
#http://people.csail.mit.edu/hubert/pyaudio/docs/
#If there a way to concatenates audios, I can record voices for each letter combination (50-60*5=200, to 300 audio files and play back them concatenate with some delays or speed up)
