import requests
from bs4 import BeautifulSoup
import re
from article import Article
import json
import pickle

articles = list()
link = 'http://creak.um.maine.edu/news/thread.php?group=umaine.cos451'

def get_posts(from_users):
    f = open('out.html', 'r')
    content = BeautifulSoup(f, 'html.parser')("tr")
    f.close()
    id_pattern = re.compile(r'id=(\d+)')
    for row in content[2:]:
        data = [cell.text.strip() for cell in row("td")]
        post_id = id_pattern.search(row.find_all(href=True)[0]['href']).group(1)
        if 'Re: ' not in data[1]:
            articles.append(Article( article_id=post_id, title=data[1], author=data[3], date_posted=data[0]))
    if from_users:
        return list(filter(lambda a: a.author in from_users, articles))
    else:
        return articles

def recent_posts(from_users):
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

# recent_posts(['Mark Royer', 'Sudarshan S Chawathe'])