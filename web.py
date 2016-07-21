#!/usr/bin/python
"""
This Python script will take in a website at the command line
, fetch the page, extract the paragraphs, and join them into
one big string.

Inspiration: 
https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html

Also good:
https://radimrehurek.com/gensim/wiki.html#latent-dirichlet-allocation
"""


from bs4 import BeautifulSoup, SoupStrainer

import requests

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

import news as n


class App(object):
	
	def __init__(self):
		#urls stored as strings
		self.urls = []
		#retrieved texts stored as strings
		self.texts = []
		#texts stored as unicode lists after
		#stopping and stemming
		self.prepped_texts = []
		
		self.tokenizer = RegexpTokenizer(r'\w+')
		self.stops = get_stop_words('en')
		self.stemmer = PorterStemmer()
		
		self.dictionary= corpora.Dictionary()
		self.model = None
		

	def get_urls(self, fname):
	
		with open(fname) as f:
			#content is list of sites to extract text from
			content = [line.strip('\n') for line in f]
		self.urls.extend(content)
		
	def get_news(self, url, flag):
		#given a news site, tries to extract article links
		#definitely works for Hacker News
		
		#returns list of urls for articles as a list of strings (unicode)
		news = n.News(url)
		news.set_flag(flag)
		news.find_links()
		return news.links
		

	def parse(self, url):
		#retrieves all <p> elements from the url
		#returns as single string
		r = requests.get(url)

		data = r.text

		soup = BeautifulSoup(data, "html.parser", parse_only=SoupStrainer('p'))

		pars = ""

		for paragraph in soup.find_all('p'):
			pars+=paragraph.get_text()
	
		return pars
		
		
	def get_texts(self):
		
		for u in self.urls:
			self.texts.append(self.parse(u))
			
	def prep_for_lsi(self):
		#tokenize, stop, stem
		for t in self.texts:
			t = t.lower()
			tokens= self.tokenizer.tokenize(t)
			stopped_tokens = [i for i in tokens if not i in self.stops]
			stems = [self.stemmer.stem(i) for i in stopped_tokens]
			#stems = [self.stemmer.stem(i) for i in tokens if not i in self.stops]
			self.prepped_texts.append(stems)
		
	def lsi_once(self, topics, iters, words):
		#add texts to dictionary for ids
		dictionary = corpora.Dictionary(self.prepped_texts)
		#create bag-of-words from the texts
		corpus = [dictionary.doc2bow(text) for text in self.prepped_texts]
		#make the LDA model from our dictionary and corpus
		lsimodel= gensim.models.lsimodel.LsiModel(corpus, num_topics=topics, id2word = dictionary, onepass=False, power_iters=iters)
		self.model = lsimodel
		
		print(lsimodel.print_topics(num_topics=topics, num_words=words))
	
	def save(self):
		self.model.save("lsi.model")
		
	def load(self):
		self.model = models.LsiModel.load("lsi.model")
	

if __name__ == '__main__':
	print("weeee")
	app = App()
	#fetch the sites
	app.get_urls("sites.txt")
	#extract the paragraphs
	app.get_texts()
	#tokenize, remove stop words, and stem
	app.prep_for_lsi()
	#Find and print 5 topics
	app.lsi_once(5, 10, 10)
	#save the model
	app.save()
	
	
	
