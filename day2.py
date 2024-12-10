import requests
from bs4 import BeautifulSoup


url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

response = requests.get(url)

print(response.status_code)
# print(response.text)

# Work with beautiful soup to get html from the url in lxml
soup = BeautifulSoup(response.text, "lxml")
print(soup)