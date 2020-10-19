from bs4 import BeautifulSoup
import requests

# search = input("Enter movie name: ").replace(" ", "+")
req_extramoives = requests.get(f"https://extramovies.rest/")

soup_extramoives = BeautifulSoup(req_extramoives.text, "html.parser")

links_extramoives = soup_extramoives.find_all("article")

for link in links_extramoives:
    print(link.a.text)
    print(link.a['href'])
    print("\n")


# COPING HTML PAGE IN FILE
# file = open("soup.html", "w+", encoding="utf-8")
# file.write(soup.prettify())
