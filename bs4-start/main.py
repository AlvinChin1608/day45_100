from bs4 import BeautifulSoup
# import lxml

# Beautiful Soup Doc https://www.crummy.com/software/BeautifulSoup/bs4/doc/
with open ("website.html", "r") as my_file:
    contents = my_file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title) # OUTPUT: <title>Alvin's Personal Site</title>
print(soup.title.string) # OUTPUT: Alvin's Personal Site
# print(soup.prettify())
print(soup.a)
all_anchor_tags = soup.find_all(name= "a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a") # we use CSS selector a tag within p
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)