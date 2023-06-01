"""
Code Your Own Project: (put project idea here)
Kaylee Huang and Lauren Dex
"""

import requests

BASE_URL = "https://cdn2.thecatapi.com/v1/images/search"



url = BASE_URL + 

response = requests.get(url)
if response.status_code != 200:
    print("error: " + str(response.status_code))
data = response.json()