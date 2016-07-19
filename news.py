from bs4 import BeautifulSoup, SoupStrainer

import requests

class News(object):

	def __init__(self, url):
		self.url = url
		self.flag = ""
		self.links = []

	def set_url(self, u):
		self.url = u

	def set_flag(self, f):
		self.flag = f

	def find_links(self):
		r = requests.get(self.url)

		data = r.text

		soup = BeautifulSoup(data, 'html.parser', parse_only=SoupStrainer('a'))

		for a in soup.find_all('a', class_=self.flag, href=True):
			self.links.append(a['href'])






if __name__ == '__main__':
	news = News('https://news.ycombinator.com/')
	news.set_flag('storylink')
	news.find_links()
	print(news.links)
