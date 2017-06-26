from EnglishTagging import conjuctions
text=open("text/kinya1.txt", encoding="utf8")
text_new="" #text.replace("\n"," ")
for line in text:
	line=line.strip()
	line=line.replace("\n"," ")
	text_new+=line
for sentence in text_new.split("."):
	conj_ed=False
	if len(sentence)<5:
		print("skipped")
	else:
		for conj in  conjuctions:
			if conj in sentence:
				print(conj)
				conj_ed=True
				print(sentence+"\n")
		if not conj_ed:
			print(sentence.strip())

