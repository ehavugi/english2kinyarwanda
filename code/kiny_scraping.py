"""	
	what do I stored as meta data for the texts that I grab out from web?
	how to ensure that I am storing only kinyarwanda webpages only on multi-language platforms like igihe.com? and other new_online platforms?
	in what format do I store the data? as a database? as text file? --raw? or processed or cleaned up?

"""

"""
	I can automatically decide to move from one page to next by use of links and store all information that can be reached that way

"""
from kinyarwanda_test import *
from bs4 import BeautifulSoup  ##Beautifulsoup for cleaning up online data for information


import urllib.request # to grab stuff online



import sqlite3  ## for data basing stuff


#Initial list of websites that can scrawl to update the list of acceptable words
##	(with say referennce to a line in their source) --- an url or/and text(stored locally)
##  a person can make it compatible with or be  like a  ##Corporus?? (I )

base_url_list=["www.kigalitoday.com/inkuru-zicukumbuye/article/leta-ibitse-akabakaba-miliyari-2rwf-akomoka-ku-mitungo-yasizwe-na-ba-nyirayo" ,"https://rw.wikipedia.org/wiki/Intangiriro","http://ibyamamare.com/indirimbo-10-nshya-zabahanzi-nyarwanda-zigezweho-ushobora-kumva/","http://inyarwanda.com/","http://www.kigalitoday.com/umuco/ikinyarwanda/article/abanyarwanda-baba-muri-malaysia-bagiye-gutora-nyampinga"]  
base_url_list=["https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/lecture-videos/lecture-1-introduction-and-scope/"]
urls=[]
def get_urls(original_url):
	## should I care much on links in/out (like need to rank?)/
	#not at moment/
	
	html_doc=urllib.request.urlopen(original_url)
	print("r")
	#html_doc=open(html_doc)
	soup=BeautifulSoup(html_doc,"html5lib")
	#print (soup.prettify())
	#except:
	#print("nope")
	urls=[]
	try :
		
		for i in soup.find_all("a"):
			if "http" in i['href'] or "https" in i['href']:
				if i["href"] not in urls:
					urls.append(i['href'])
		return urls
	except:
		return 
def read_online(url):
	#store data(formats:database?, textFiles?)
	#Post_edit, or store clean data
	#
	data=""
	return  data 

def store(data):
	return "stored"

def clean_online_data(data):
	return 
# html=get_urls("https://rw.wikipedia.org/wiki/Imirenge_y%E2%80%99u_Rwanda")
# saving=open("text/urls.txt","w")
# #saving=read(saving)
# dictionary=[]
# # for i in range(6):
# # 	for header in html.find_all("h"+str(i)):
# # 		try:
# # 			text=header.get_text()
# # 			if not (text in dictionary):
# # 				dictionary.append(text)
# # 				print(header.get_text().strip(),"\n")
# # 		except:
# # 			print("nope")
# print("starting paragraph")
# listings=[]
#divs=html.find_all('div')
# for pragraph in divs:
# 	try:
# 		text=pragraph.get_text()
# 		#print(text.split())
# 		text=text.strip().split("\n")
# 		#print(text.split( "\n"))
# 		if kinyarwanda_level(text)>0.7:
# 			for i in text:
# 				print(kinyarwanda_level(text),i)
# 			if text not in listings:
# 				#print(text)
# 				listings=listings.append(text)
# 			else:
# 				print("what? ",text)
# 	except:
# 		#print(pragraph.get_text())
# 		continue
# 		#print("not a par")
# #print(html.get_text().strip())

