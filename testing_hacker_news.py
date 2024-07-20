import requests
from bs4 import BeautifulSoup


class ArticlesData:
    def __init__(self):
        response = requests.get("https://news.ycombinator.com/news")

        yc_webpage = response.text

        self.soup = BeautifulSoup(yc_webpage, "html.parser")
        self.a_tags = []
        articles = self.soup.find_all(class_="titleline")
        for article in articles:
            self.a_tags.append(article.find(name="a"))

    def titles(self):
        """get article titles"""
        article_titles = []
        for a_tag in self.a_tags:
            article_title = a_tag.get_text()
            article_titles.append(article_title)
        return article_titles


    def links(self):
        """get article links"""
        article_links = []
        for a_tag in self.a_tags:
            article_link = a_tag.get("href")
            article_links.append(article_link)
        return article_links


    def upvotes(self):
        """get article upvotes"""
        article_scores = [score.get_text() for score in self.soup.find_all(class_="score")]
        return article_scores


if __name__ == "__main__":
    data = ArticlesData()

    print(data.titles())
    print(data.links())
    print(data.upvotes())
