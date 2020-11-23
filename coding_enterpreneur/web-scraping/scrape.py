from datetime import datetime
from requests_html import HTML
import requests


def url_to_text(url, save=False):
    req = requests.get(url)
    if req.status_code == 200:
        html_text = req.text
        if save:
            with open(f"{datetime.now().year}-movies-box-office.html", 'w') as file:
                file.write(html_text)
        return html_text


url = 'https://www.boxofficemojo.com/year/world/'

html_text = url_to_text(url)

req_html = HTML(html=html_text)

table_class = '.imdb-scroll-table'
# table_class = '#table'
req_table = req_html.find(table_class)

# print(req_table)
table_data = []
header_names = []
if len(req_table) == 1:
    # data type of req_table is list so it's not converted or find us anything. req_table[0] do.
    # print(req_table[0].text)
    rows = req_table[0].find('tr')
    header_row = rows[0]
    header_cols = header_row.find('th')
    header_names = [header.text for header in header_cols]
    for row in rows[1:]:
        # print(row.text)
        cols = row.find('td')
        row_data = []
        # for counter, col in enumerate(cols):
        # print(counter, col.text, '\n')
        for col in cols:
            row_data.append(col.text)
        table_data.append(row_data)

print(header_names)
for data in table_data:
    print(data)
