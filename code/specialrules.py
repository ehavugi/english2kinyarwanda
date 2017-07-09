def translate (sentence):
	if "how would" in sentence:
		return "ni gute "+ translate(sentence.replace("how would",""))
	elif "how" in sentence:
		return "nigute"+translate(sentence.replace("how","")) 
	elif "who" in sentence:
		return "ninde" +translate(sentence.replace("who",""))
	else:
		return (sentence)

def is_question(sentence):
	sentence=sentence.strip().lower()
	if sentence[len(sentence)-1]=="?" and (sentence.split()[0] in ["how","who","what","where","what"]):
		return True

def is_exclamatory(sentence):
	sentence=sentence.strip().lower()
	if sentence[len(sentence)-1]=="!":
		return True


print(is_question("who am i?"))
print(translate("how would i like it ? \n"))
print(is_exclamatory("what a damn thing !   "))