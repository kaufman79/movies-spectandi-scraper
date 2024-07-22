import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
site = response.text
soup = BeautifulSoup(site, "html.parser")

movies_list = soup.find_all(class_="listicleItem_listicle-item__title__BfenH")

movies_texts = [movie.get_text() + "\n" for movie in movies_list]

movies_texts.reverse()

with open("movies.txt", 'w') as file_local:
    file_local.writelines(movies_texts)
