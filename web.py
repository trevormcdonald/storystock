#!/usr/bin/python
"""
This Python script will take in a website at the command line
, fetch the page, extract the paragraphs, and join them into
one big string.

Inspiration: 
https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html
"""


from bs4 import BeautifulSoup

import requests

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim


class App(object):
	
	def __init__(self):
		self.urls = []
		self.texts = []
		self.prepped_texts = []
		self.tokenizer = RegexpTokenizer(r'\w+')
		self.stops = get_stop_words('en')
		self.stemmer = PorterStemmer()
		

	def get_urls(self, fname):
		with open(fname) as f:
			#content is list of sites to extract text from
			content = [line.strip('\n') for line in f]
		self.urls.extend(content)

	def parse(self, url):
		r = requests.get(url)

		data = r.text

		soup = BeautifulSoup(data, "html.parser")

		pars = ""

		for paragraph in soup.find_all('p'):
			pars+=paragraph.get_text()
	
		return pars
		
		
	def get_texts(self):
		
		for u in self.urls:
			self.texts.append(self.parse(u))
			
	def prep_for_lda(self):
		#tokenize, stop, stem
		for t in self.texts:
			t = t.lower()
			tokens= self.tokenizer.tokenize(t)
			stopped_tokens = [i for i in tokens if not i in self.stops]
			stems = [self.stemmer.stem(i) for i in stopped_tokens]
			self.prepped_texts.append(stems)
		
	
	

if __name__ == '__main__':
	print("weeee")
	app = App()
	app.get_urls("sites.txt")
	app.get_texts()
	app.prep_for_lda()
	
	
	
