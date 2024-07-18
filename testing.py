from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, features="html.parser")

# print(soup.prettify())
# print(soup.li)

anchors_tags = soup.find_all(name="a")
h_three_tags = soup.find_all(name="h3")

# for tag in anchors_tags:
#     # print(tag.get_text())
#     print(tag.get("href"))
#
# print("\n")
#
# for tag in h_three_tags:
#     if tag.get_text() == "Other Pages":
#         print(tag.get_text())

# heading = soup.find(name="h1", id="name")
# print(heading)

# 'class' is a reserved keyword in python, so we use class_ to reference css class
section_headings = soup.find_all(name="h3", class_="heading")

for section_heading in section_headings:
    # .get returns a list here but we can grab just the string
    string = section_heading.get("class")[0]
    print(string)

# getting a select url, since there are often many on any given site
# first, find specifics of the html code its in. for the appbrewery site,
# its the first link in a p tag and an a tag, so we can use the selector
# with p and a
company_url = soup.select_one(selector="p a")
company_url = company_url.get("href")
print(company_url)

# note the following two lines seem to do the same thing, but I guess
# select is more for CSS elements
print(soup.select_one("#name"))
print(soup.find(id="name"))

headings = soup.select(".heading")
print(headings)
