import requests
from bs4 import BeautifulSoup


response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

# get first article's title
article_one = soup.find(class_="titleline")
title_and_link = article_one.find(name="a")
article_title = title_and_link.get_text()
print(article_title)

# find article link
article_link = title_and_link.get("href")
print(article_link)

# find article upvotes
article_score = soup.find(class_="score")
article_score = article_score.get_text()
print(article_score)
