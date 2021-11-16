# Credit for web-scraping help:
# https://stackoverflow.com/questions/44704099/python-scrape-table-from-website

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.currentresults.com/Weather/US/average-annual-state-temperatures.php"

page = requests.get(url)
html = page.text

soup = BeautifulSoup(html, features="lxml")
table = soup.findAll("table", {"class": "articletable"})
data = []
for state in table:
    # row = state.find("tr")
    # print(row)
    # for row in rows[1:]:
    # Find all data entries
    cols = state.findAll("td")
    # Remove whitespace from data entries
    cols = [i.text.strip() for i in cols]
    # print(cols[0])
    # Add data element to data table
    # data.append([i for i in cols if i])
    for i in range(len(cols)):
        # print(cols[0])
        if i % 4 == 0:
            data.append(cols[i: i+4])

# table = soup.find_next("table", {"class": "articletable"})
# rows = table.find_all("tr")
# for row in rows[1:]:
#     # Find all data entries
#     cols = row.find_all("td")
#     # Remove whitespace from data entries
#     cols = [i.text.strip() for i in cols]
#     # Add data element to data table
#     data.append([i for i in cols if i])

df = pd.DataFrame(data, columns=["State", "AvgF", "AvgC", "Rank"])
df.to_csv("weather.csv")


# doc = lh.fromstring(page.content)

# elts = doc.xpath("//tr")
# cols = []

# for elt in elts[0]:
#   name = elt.text_content
#   cols.append((name, []))
