import os
import pandas as pd
import requests
import json
from dotenv import load_dotenv

load_dotenv()

url_list = []

for page in range(1, 12):
    url = f"https://content.guardianapis.com/search?q=adani&api-key={os.getenv("API_KEY")}&from-date=2022-08-08&page={page}&type=article"

    url_list.append(url)

def get_articles(url_list):
    # Fetch all articles and add them to a list
    articles = []
    for url in url_list:
        response = requests.get(url)
        if int(response.status_code) == 200:
            blob = response.json()
            articles.append(blob)
        else:
            continue

    # with open("contents.json", mode="w") as file:
    #     file.write(json.dumps(articles))

    return articles

get_articles(url_list)