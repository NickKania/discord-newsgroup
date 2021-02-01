import requests
from bs4 import BeautifulSoup
import re
from article import Article

articles = list()
link = 'http://creak.um.maine.edu/news/thread.php?group=umaine.cos451'

f = open('out.html', 'r')
content = BeautifulSoup(f, 'html.parser')("tr")
f.close()
id_pattern = re.compile(r'id=(\d+)')
for row in content[2:]:
    data = [cell.text.strip() for cell in row("td")]
    post_id = id_pattern.search(row.find_all(href=True)[0]['href']).group(1)
    if 'Re: ' not in data[1]:
        articles.append(Article( article_id=post_id, title=data[1], author=data[3], date_posted=data[0]))
for a in articles:
    if a.author in ['Sudarshan S Chawathe', 'Mark Royer']:
        print (a)
        print('-' * 20)
