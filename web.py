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


with open("sites.txt") as f:
	#content is list of sites to extract text from
	content = [line.strip('\n') for line in f]


r = requests.get(url)

data = r.text

soup = BeautifulSoup(data, "html.parser")

par_list=[]

for paragraph in soup.find_all('p'):
	par_list.append(paragraph.get_text())
	
doc = " ".join(par_list)


