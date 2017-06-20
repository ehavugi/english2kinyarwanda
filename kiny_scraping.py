"""	
	what do I stored as meta data for the texts that I grab out from web?
	how to ensure that I am storing only kinyarwanda webpages only on multi-language platforms like igihe.com? and other new_online platforms?
	in what format do I store the data? as a database? as text file? --raw? or processed or cleaned up?

"""

"""
	I can automatically decide to move from one page to next by use of links and store all information that can be reached that way

"""

import bs4  ##Beautifulsoup for cleaning up online data for information

import urllib # to grab stuff online



import sqlite3  ## for data basing stuff


#Initial list of websites that can scrawl to update the list of acceptable words
##	(with say referennce to a line in their source) --- an url or/and text(stored locally)
##  a person can make it compatible with or be  like a  ##Corporus?? (I )

base_url_list=["http://www.igihe.com","http://www.inyarwanda.com"]  
#@urls, do I have to request people permission to view or reference their 
#data(or use it for building a corporus like thing)

def get_urls(original_url):
	## should I care much on links in/out (like need to rank?)/
	#not at moment/
	return "all_children urls or just do do the web_crawling"

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



