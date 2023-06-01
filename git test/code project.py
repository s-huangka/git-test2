"""
Code Your Own Project: (put project idea here)
Kaylee Huang and Lauren Dex
"""

# libraries and variables
from pip._vendor import requests

all_IDs = []

BASE_URL = "https://api.thecatapi.com/v1/images/search"

# user input
#new_image = input("enter \"n\" to generate a new image: ") == "n"
"""
if new_image:
    url = BASE_URL + "?limit=1"

    response = requests.get(url)

    if response.status_code != 200:
        print("error: " + str(response.status_code))
        exit()
    data = response.json()

    url=data["url"]
    print(url)
    new_ID = data["id"]
    all_IDs.append(new_ID)
    print(all_IDs)
    """

url = BASE_URL + "?limit=1"
print(url)

response = requests.get(url)

if response.status_code != 200:
    print("error: " + str(response.status_code))
    exit()
data = response.json()
print(data)

url=data[0]["url"]
print(url)

new_ID = data[0]["id"]
all_IDs.append(new_ID)
print(all_IDs)