from datetime import datetime
import os

username, password = (os.getenv('NEWSGROUP_USR'), os.getenv('NEWSGROUP_PASS'))

class Article():
    """
    Object to hold information for each post made
    """

    def __init__(self, article_id, title, author, date_posted):
        self.title = title
        self.article_id = article_id
        self.author = author
        self.responses = list()
        self.date_posted = datetime.strptime(date_posted, "%Y-%m-%d").date()
        self.post_url = f'http://{username}:{password}creak.um.maine.edu/news/article.php?id={self.article_id}&group=umaine.cos451'

    def __str__(self):
        return "Title: [%s](%s)\nAuthor: %s\nDate Posted: %s" % (
            self.title, self.post_url, self.author, self.date_posted)

    def to_dict(self):
        return {
            "title": self.title,
            "article_id": self.article_id,
            "author": self.author,
            "date_posted": self.date_posted
        }

    def __eq__(self, obj):
        return isinstance(obj, Article) and obj.title == self.title
