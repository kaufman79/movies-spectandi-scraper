import requests
from bs4 import BeautifulSoup


class ArticlesData:
    def __init__(self):
        response = requests.get('https://news.ycombinator.com/news')

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
        int_scores = [int(score.split()[0]) for score in article_scores]
        return int_scores


if __name__ == "__main__":
    data = ArticlesData()

    # print(data.titles())
    # print(data.links())
    # print(data.upvotes())

    titles = data.titles()
    links = data.links()
    upvotes = data.upvotes()

    # find index of most upvoted article
    max_score = max(upvotes)
    max_index = upvotes.index(max_score)

    # find title & link of most upvoted article
    max_title = titles[max_index]
    max_link = links[max_index]

    print(max_title)
    print(max_link)
