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
thousands=[" ","igihumbi","ibihumbi biri","ibihumbi bitatu","ibihumbi bine","ibihumbi bitanu","ibihumbi bitandatu",
			"ibihumbi birindwi","ibihumbi umunani","ibihumbi icyenda","ibihumbi icumi"]
millions=["", "miliyoni imwe","miliyino ebyiri","miliyoni eshatu","miliyoni enye","miliyoni eshanu","miliyoni esheshatu","miliyoni zirindwi","miliyoni umunanani"," miliyoni icyenda"]
 
billions=["","miliyari imwe", "imiliyari ebyiri","miliyairi eshatu","miliyari enye","miliyari eshanu","miliyari esheshatu","zirindwi","umunani","icyenda"]
trillions=["","tiliyoni","tiliyoni ebyeri","tiliyoni eshatu","tiliyoni enye","tiliyoni eshanu","tiliyoni esheshatu","tiliyoni zirindwi","tiliyoni umunani","tiliyoni icyenda"]
#level=["basic","tens","hundrends","thousands"]

inputs= "0722765359"

basic=[basic0,basic3,basic6,basic9,basic12]

# for i in range(10):
# 	b=i
# 	print (basic[str(i)])
# 	print(tens[str(b)])
# 	print(hundreds[str(i)])
def na_def(a):
	if "  " in a:
		a=a.replace("  "," ")
	if " na n" in a:
		a=a.replace(" na n", " n")
	if "na icu" in a:
		a=a.replace(" na icu", " na cu")
	if "na i" in a:
		a=a.replace(" na i", " n'i")
	if "na zero" in a:
		a=a.replace(" na zero","")
	if " na e" in a:
		a=a.replace(" na e", " n'e")
	return a 

def spell(inputs):
	number=len(str(inputs))
	print(number)
	for i in str(inputs):
 		print(basic[int(i)-1])


def amajana(inputs,urugero=0):

	"""
		amajana takes a number from 0 to 999 and write outs its kinyarwanda wording eg: 1 -->rimwe, 
		801 ---> magana umunani na rimwe .. it is still under developments( you can submit bugs or
		suggestions at ehavugi@mit.edu) if found before 2020

	"""
	assert (len(str(inputs))<4)#,"Not less than 999. Umubare nuri musi ya 999")ssert (len(inputs)<4)#,"Not less than 999. Umubare nuri musi ya 999")
	inputs=str(inputs)
	if inputs[0]=="0" and len(inputs)>1:
		inputs1=inputs[1:]
		amajana(inputs1)
			#continue

	
	# if int(inputs[0])==0:
	# 	inputs=inputs[1:(len(inputs)-1)]

	if len(inputs)==1:
		return (basic[urugero][str(inputs)])
	if len(inputs)==2:
		if int(inputs[1])==0:
			return (tens[str(inputs[0])])
		if int(inputs[1]) in [8,9]:
			return (tens[str(inputs[0])]+" n'"+basic[urugero][str(inputs[1])]) ## to use punctuation n' before a vowel
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
				return(hundreds[str(inputs[0])]+" n'"+ basic[urugero][str(inputs[2])])  ## A person can also implement punctuation rules a different manner
			else:
				print()
				return(hundreds[str(inputs[0])]+" na "+tens[str(inputs[1])]+" n'"+ basic[urugero][str(inputs[2])])
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
	length=len(inputs)
	if inputs.startswith("0") and length>1:
		return ibihumbi(inputs[1:])
	if len(inputs)<4:
		return (amajana(inputs))
	else:
		if len(inputs)==4:
			if int(inputs[0])==1:
				if str(inputs[1:4])!="000":
					a=("igihumbi " +amajana(inputs[1:4]))
				
					return na_def(a) 
				#elif str(inputs)
				else:
					return ("igihumbi")
			else:
				a="ibihumbi "+amajana(inputs[0:(len(inputs)-3)],1)+" na "+amajana(inputs[len(inputs)-3:len(inputs)])
				
				return na_def(a)
		elif len(inputs)>4:
			if inputs[len(inputs)-3:]=="000":
				a="ibihumbi "+amajana(inputs[:(len(inputs)-3)],1)
			else:
				a="ibihumbi "+amajana(inputs[:(len(inputs)-3)],1)+" na "+amajana(inputs[len(inputs)-3:len(inputs)])
			
			return na_def(a)
def miliyoni(inputs):
	inputs=str(inputs)
	assert len(inputs)<10
	if inputs.startswith("0"):
		return miliyoni(inputs[1:])
	
	if len(inputs)<7:
		return ibihumbi(inputs)
	else:
		if len(inputs)==7:
			#if input[1:7]>0:
			if inputs[len(inputs)-6:]=="000000":
				a=millions[int(inputs[0])]
			else:
				a=millions[int(inputs[0])]+" na "+ ibihumbi(inputs[(len(inputs)-6):])
			
			return na_def(a)
		elif len(inputs)>7:
			if inputs[len(inputs)-6:]=="0000000":
				a=millions[int(inputs[0])]+" "+  amajana(inputs[:len(inputs)-6],2)
			else:
				a="miliyoni"+" " +amajana(inputs[:len(inputs)-6],2) +" na " + ibihumbi(inputs[len(inputs)-6:len(inputs)])  
			
			return na_def(a) 

def miliyari(inputs):
	inputs=str(inputs)
	assert len(inputs)<13
	if inputs.startswith("0"):
		return(inputs[1:])
	if len(inputs)<10:
		a=miliyoni(inputs)
		if "na zero" in a:
			a=a.replace("na zero", "")
		return na_def(a)
	else:
		if len(inputs)==10:
			#if input[1:7]>0:
			if inputs[len(inputs)-9:]=="000000000":
				a=billions[int(inputs[0])]
			else:
				a=billions[int(inputs[0])]+" na "+ miliyoni(inputs[1:10])
			return na_def(a)
		elif len(inputs)>10:
			if inputs[len(inputs)-9:]=="000000000":
				a="miliyari" +" "+ amajana(inputs[:len(inputs)-9],2)
			else:
				a="miliyari"+" "+  amajana(inputs[:len(inputs)-9],2)+" na " + miliyoni(inputs[len(inputs)-9:])  
			return na_def(a)
def tiliyoni(inputs):
	inputs=str(inputs)
	assert len(inputs)<16
	if inputs.startswith("0"):
		return(inputs[1:])
	if len(inputs)<13:
		a=miliyari(inputs)
		if "na zero" in a:
			a=a.replace("na zero", "")
		return na_def(a)
	else:
		if len(inputs)==13:
			#if input[1:7]>0:
			if inputs[len(inputs)-12:]=="000000000000":
				a=trillions[int(inputs[0])]
			else:
				a=trillions[int(inputs[0])]+" na "+ miliyari(inputs[1:13])
			return na_def(a)
		elif len(inputs)>13:
			if inputs[len(inputs)-12:]=="000000000000":
				a="tiliyoni" +" "+ amajana(inputs[:len(inputs)-12],2)
			else:
				a="tiliyoni"+" "+  amajana(inputs[:len(inputs)-12],2)+" na " + miliyari(inputs[len(inputs)-12:])  
			return na_def(a)

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

# print(hundred_s(98))
# for i in range(2000):
# 	print(ibihumbi(i),i)


#http://people.csail.mit.edu/hubert/pyaudio/docs/
# print(miliyari(1000000000))
# print(miliyari(10000000000))

# for i in range(9990,1000000000000000,100000000000):
# 	print(tiliyoni(i),":", i)
#print(tiliyoni(12))


"""
Numbers in English


"""
units=["zero","one","two","three","four","five","six","seven","eight","nine"]
uniteen=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens2=["twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]

def up100(number, country="us"):
	number=str(number)
	#assert len(number)>0
	number=str(number)
	assert len(number)<3 
	if number[0]=="0" and len(number)>1:
		number1=number[1:]
		return up100(number1)


	if len(number)==1:
		return units[int(number)]
	if len(number)==2:
		if  number[0]=="1":
			if number[1]=="0":
				return "ten"
			return  uniteen[int(number[1])-1]
		if number[1]=="0":
			return tens2[int(number[0])-2]
		return tens2[int(number[0])-2]+"-"+ units[int(number[1])]
def up1000(number, country="us"):
	number=str(number)
	assert len(number)<4
	if number[0]=="0" and len(number)>1:
		number1=number[1:]
		return up1000(number1)
	if len(number)<3:
		return up100(number)
	def countryness_and(country):
		if country=="uk":
			return " and "
		else:
			return ""
	if number[1:]=="00":
		return units[int(number[0])]+ " hundred "
	return units[int(number[0])]+ " hundred "+ countryness_and(country)+ up100(int(number[1:]))
def thousands(number, country="us"):
	number=str(number)
	assert len(number)<7
	if number[0]=="0" and len(number)>1:
		number1=number[1:]
		return thousands(number1)
	if len(number)<4:
		return up1000(number)
	return up1000(number[:len(number)-3])+ " thousand " + up1000(number[len(number)-3:])
def million(number,country="us"):
	number=str(number)
	assert len(number)<10
	if len(number)<7:
		return thousands(number,country)
	if number[len(number)-6:]=="000000":
		return thousands(number[:len(number)-6])+ " million"
	return thousands(number[:len(number)-6])+ " million " + thousands(number[len(number)-6:])

# for i in range(1000000,100000000):
# 	print(i, " : ", million(i)," \n"," "*len(str(i)) ,":", miliyari(i))



