import requests

url = "https://alex-njuguna.vercel.app/"

response = requests.get(url)

# get the status code of the web page
print(response.status_code)

# Get the html of the web page
print(response.text)