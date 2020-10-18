from bs4 import BeautifulSoup
import requests

search = input("Enter movie name: ").replace(" ", "+")
req_moviesflix = requests.get(f"https://themoviesflix.co/?s={search}")

soup_moviesflix = BeautifulSoup(req_moviesflix.text, "html.parser")

links_moviesflix = soup_moviesflix.find_all(
    "article", class_="latestPost excerpt")

for link in links_moviesflix:
    print(link.a['title'])
    print(link.a['href'])
    print("\n")


# COPING HTML PAGE IN FILE
# file = open("soup.html", "w+", encoding="utf-8")
# file.write(soup.prettify())
