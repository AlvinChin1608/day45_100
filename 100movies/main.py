import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

all_movies = soup.find_all(name="h3", class_="title")
print(all_movies)

movie_title=[movie.getText() for movie in all_movies]
movies  = movie_title[::-1] # use slicing to make it ascending order

with open("text.txt", "w") as data:
    for movie in movies:
        data.write(f"{movie}\n")