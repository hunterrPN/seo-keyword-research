
import requests
import pandas as pd

url = "https://ubersuggest-keyword-ideas.p.rapidapi.com/keyword-research"
querystring = {
    "keyword": "global internship",  
    "country": "in",
    "language_code": "en",
    "network_type": "search-plus-partners"
}

headers = {
    "x-rapidapi-key": "YOUR_API_KEY",  
    "x-rapidapi-host": "ubersuggest-keyword-ideas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

for item in data['result'][:50]:
   print(item['keyword'], "| Volume:", item['search volume'], "| Difficulty:", item['Keyword Difficulty %'])
