import os
import pandas as pd
import requests
import json
from dotenv import load_dotenv

load_dotenv()

url_list = []

for page in range(1, 12):
    url = f"https://content.guardianapis.com/search?q=adani&api-key={os.getenv("API_KEY")}&from-date=2022-08-08&page={page}&type=article"
    # response = requests.get(url)
    # print(response)
    url_list.append(url)

# print(url_list)

def get_articles(url_list):
    # Fetch all articles and add them to a list
    articles = []
    for url in url_list:
        response = requests.get(url)
        if int(response.status_code) == 200:
            blob = response.json()
            articles.append(blob)

    return articles

info = get_articles(url_list)
# print(info[0]["response"]["total"])
# print(info[3]["response"]["results"][5]["webTitle"])

final_list = []

try:
    for page in range(1, 12):
        for article in range(1, 11):
            new_article = dict(
                title=info[page]["response"]["results"][article]["webTitle"].strip(),
                section=info[page]["response"]["results"][article]["sectionName"].strip(),
                published_date=info[page]["response"]["results"][article]["webPublicationDate"].strip()
            )
            final_list.append(new_article)
except IndexError:
    print("done")

# print(final_list)
data = pd.DataFrame(final_list)
print(data)


