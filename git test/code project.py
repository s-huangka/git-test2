"""
Code Your Own Project: Random Cat Images
Kaylee Huang and Lauren Dex
"""

# Libraries and variables
from pip._vendor import requests
import pickle
import pprint
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
    print()
    
    # Quit
    if id == "Q":
        break
    
    # Generate the most recent image
    elif id == "O" and len(all_IDs) >= 1:
        
        # First API call
        url = BASE_URL + all_IDs[-1]

        response = requests.get(url)

        if response.status_code != 200:
            print("ERROR: " + str(response.status_code))
            exit()
        data = response.json()

        url=data["url"]

        # Second API call
        response = requests.get(url)

        if response.status_code != 200:
            print("ERROR: " + str(response.status_code))
            exit()
        data = response.json()
        print(data)



    # Failure to generate the most recent image
    elif id == "O" and len(all_IDs) < 1:
        print("You must generate a new image before calling this function")
        print()
        exit()

    # Generate a new image
    elif id == "N":

        # First API call
        url = BASE_URL + "search?limit=1"

        response = requests.get(url)

        if response.status_code != 200:
            print("ERROR: " + str(response.status_code))
            exit()
        data = response.json()

        url = data[0]["url"]
        print("Ctrl + click this link to view your random cat image:", url)

        new_ID = data[0]["id"]
        all_IDs.append(new_ID)

        # Second API call
        url = BASE_URL + new_ID

        response = requests.get(url)

        if response.status_code != 200:
            print("ERROR: " + str(response.status_code))
            exit()
        data = response.json()

        if "breeds" in data:
            print("Breed:", data["breeds"][0]["name"])
            if "description" in data["breeds"][0]:   
                print("Description:", data["breeds"][0]["description"])
            if "origin" in data["breeds"][0]:
                print("Origin:", data["breeds"][0]["origin"])
            if "temperament" in data["breeds"][0]:
                print("Temperament:", data["breeds"][0]["temperament"])
        if "width" in data:
            print("Width:", data["width"])

        print()
        print()
        print()
        print(data)

    # User entered invalid input
    else:
        exit()