"""
This is file is a work on idea that when :I detect verb in english sentence
@@ and get a translation table of sentence """

import nltk


text_en="peter like paul"
text_rw="petero akunda polo"

text={}
count=0
for line_eng in (text_en()):
	line_rw=text_rw[count]
	def get(sentence):
		""" Should return a verb in the sentence --main verb."""
		return "verb"
	verb=get(line_eng)
	if verb not in text.keys():
		text[verb]=list(line_eng+"||"+line_rw)
		print(text)
	else:
		text[verb]=text[verb].append(line_eng+"||"+line_rw)
		print(text)

	count+=1
