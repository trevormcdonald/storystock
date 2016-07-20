import web as w

class Article(object):

	def __init__(self, url):
		self.url = url
		self.site = ""
		self.topics = []
		self.title = ""
		self.liked = 0
		self.date = None
		self.text= ""
		
	
	def get_site(self):
	
	def get_title(self):
	
	def set_liked(self, value):
		self.liked = value
		
	def get_date(self):
	
	def get_text(self):
		self.text = w.parse(self.url)
	
	
