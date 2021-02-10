from datetime import datetime
from json import JSONEncoder
from sqlalchemy import Column, ForeignKey, String, Boolean, Integer, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Article(Base):
	"""docstring for article"""
    __tablename__ = 'articles'
    art_id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(Integer, ForeignKey('user.usr_id'))
    date_posted = Column(Date, default=datetime.now())
    viewed = Column(Boolean, default=False)



	def __init__(self, article_id, title, author, date_posted):
		self.title = title
		self.article_id = article_id
		self.author = author
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

class User(Base):
    __tablename__ = 'user'
    usr_id = Column(Integer, primary_key=True)
    posts = relationship('Article')
    def __init__(self, name):
        self.name = name
