from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, features="html.parser")

# print(soup.prettify())
# print(soup.li)

anchors_tags = soup.find_all(name="a")

for tag in anchors_tags:
    print(tag.get_text())