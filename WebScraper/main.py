from bs4 import BeautifulSoup
import requests

search = input("Enter search term: ")
req = requests.get(f"https://www.google.com/search?q={search}")

soup = BeautifulSoup(req.text, "html.parser")


links = soup.find_all("div", class_='BNeawe UPmit AP7Wnd')
print(links)
for link in links:
    print(link.text)

# COPING HTML PAGE IN FILE
# file = open("soup.html", "w+", encoding="utf-8")
# file.write(soup.prettify())
