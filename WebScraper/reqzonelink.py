from bs4 import BeautifulSoup
import requests

search = input("Enter movie name: ").replace(" ", "+")
req_reqzone = requests.get(f"https://reqzone.com/?s={search}")

soup_reqzone = BeautifulSoup(req_reqzone.text, "html.parser")

links_reqzone = soup_reqzone.find_all("div", {"class": "post-wrap"})

for link in links_reqzone:
    print(link.header.h1.a.text)
    print(link.header.h1.a['href'])
    print("\n")


# COPING HTML PAGE IN FILE
# file = open("soup.html", "w+", encoding="utf-8")
# file.write(soup.prettify())
