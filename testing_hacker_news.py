import requests
from bs4 import BeautifulSoup


class FirstArticle:
    def __init__(self):
        response = requests.get("https://news.ycombinator.com/news")

        yc_webpage = response.text

        self.soup = BeautifulSoup(yc_webpage, "html.parser")

        article_one = self.soup.find(class_="titleline")
        self.title_and_link = article_one.find(name="a")


    def first_title(self):
        """get first article's title"""
        article_title = self.title_and_link.get_text()
        return article_title


    def first_link(self):
        """find article link"""
        article_link = self.title_and_link.get("href")
        return article_link


    def first_upvotes(self):
        """find article upvotes"""
        article_score = self.soup.find(class_="score")
        article_score = article_score.get_text()
        return article_score


if __name__ == "__main__":
    first_article = FirstArticle()

    print(first_article.first_title())
    print(first_article.first_link())
    print(first_article.first_upvotes())
