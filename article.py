from datetime import datetime
from json import JSONEncoder

class Article():
	"""docstring for article"""
	def __init__(self, article_id, title, author, date_posted):
		self.title = title
		self.article_id = article_id
		self.author = author
		self.responses = list()
		self.date_posted = datetime.strptime(date_posted, "%Y-%m-%d").date()

	def addResonse(self, article):
		self.responses.add(article)

	def getContent():
		return content

	def __str__(self):
		return "Title: %s\nID: %s\nAuthor: %s\nDate Posted: %s" % (self.title, self.article_id, self.author, self.date_posted)

	def to_dict(self):
		return  {
			"title": self.title,
			"article_id": self.article_id,
			"author": self.author,
			"date_posted": self.date_posted
		}