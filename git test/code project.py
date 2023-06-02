"""
Code Your Own Project: Random Cat Images
Kaylee Huang and Lauren Dex
"""

# libraries and variables
from pip._vendor import requests
import pickle
from os import path

def save(object, file):
    with open(file, "wb") as f:
        pickle.dump(object, f)

def load(file):
    if path.exists(file):
        with open(file, "rb") as f:
            return pickle.load(f)
    return None

ID_FILE = "IDS.pkl"
all_IDs = load(ID_FILE)
if all_IDs is None:
    all_IDs = []

while True:
    BASE_URL = "https://api.thecatapi.com/v1/images/"

    print()
    id = input("Enter \"n\" to generate a new image, \"o\" to generate the most recent image, or \"q\" to quit: ").capitalize()
    if id == "Q":
        break
    elif id == "O":
        url = BASE_URL + all_IDs[-1]
    elif id == "N":
        url = BASE_URL + "search?limit=1"
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
    else:
        exit()