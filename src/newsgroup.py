import requests
from bs4 import BeautifulSoup
import re
from article import Article
import json
import pickle
import os
from dotenv import load_dotenv


URL = 'http://creak.um.maine.edu/news/thread.php?group=umaine.cos451'
ALL_POSTS = True


def get_posts(from_users):
    """
    Get all posts for a user is one is specified, otherwise read all posts and create an article for it
    TODO: support for replies workflow
    """
    articles = list()
    load_dotenv()
    resp = requests.get(URL, auth=(os.getenv('NEWSGROUP_USR'), os.getenv('NEWSGROUP_PASS')))
    if resp.ok:
        content = BeautifulSoup(resp.content, 'html.parser')("tr")
        id_pattern = re.compile(r'id=(\d+)')
        for row in content[2:]:
            data = [cell.text.strip() for cell in row("td")]
            post_id = id_pattern.search(row.find_all(href=True)[0]['href']).group(1)
            if 'Re: ' not in data[1] or ALL_POSTS:
                articles.append(Article( article_id=post_id, title=data[1], author=data[3], date_posted=data[0]))
        if from_users:
            return list(filter(lambda a: a.author in from_users, articles))
        else:
            return articles

def recent_posts(from_users):
    """
    Checks posts against already parsed posts and only returns ones that have not been displayed by the bot
    """
    posts = get_posts(from_users)
    try:
        messages_shown = pickle.load(open('seen.p', 'rb'))
    except:
        messages_shown = []
    recents = []
    for p in posts:
        if p not in messages_shown:
            recents.append(p)
    messages_shown.extend(recents)
    pickle.dump(messages_shown, open('seen.p', 'wb'))
    return recents
