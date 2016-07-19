from bs4 import BeautifulSoup

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

		soup = BeautifulSoup(data, 'html.parser')

		for href in soup.find_all('a', class_=self.flag):
			self.links.append(href.get_text())






if __name__ == '__main__':
	news = News('https://news.ycombinator.com/')
	news.set_flag('storylink')
	news.find_links()
	print(news.links)
