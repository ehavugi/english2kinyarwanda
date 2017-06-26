bible_kin=open("../text/bysb.txt", encoding="utf8").readlines()
nimukanguke=open("../text/Nimukanguke_3_2017.txt",encoding="utf8").readlines()
print (len(bible_kin))
#bible_kin=bible_kin.split()
#nimukanguke=nimukanguke.split()

three_word=[]
one_word=[]
two_word=[]
big=0
for sentence in bible_kin:
	sentence=sentence.split()[1:]
	count=0
	print(sentence)
	#if word in one_word.keys():
	# counting=0
	# for x in sentence:
	# 	counting+=1
	# 	one_word.append(x)
	# 	print(x)
	# count2=0
	# for y in sentence:
	# 	count2+=1
	# 	if count2 <len(sentence):
	# 		y=y+" "+sentence[count2]
	# 		two_word.append(y)
	# 		print(y)
	for word in sentence:
		count+=1
		if count<len(sentence)-1:
			big+=1
			word=word+" "+sentence[count][0:2]+" "+ sentence[count+1][0:2]
			three_word.append(word)
			print (word)

print(big)
print("one word :", len(one_word))
print("two word :", len(two_word))
print("three word : ", len(three_word))
	