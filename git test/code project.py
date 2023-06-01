"""
Code Your Own Project: (put project idea here)
Kaylee Huang and Lauren Dex
"""

# libraries and variables
from pip._vendor import requests

BASE_URL = "https://cdn2.thecatapi.com/v1/images/search"

# user input
num = int(input("how many cat pictures do you want to see? (please enter a number between 1 and 10) "))

if num > 10:
    num = input("please enter a number between 1 and 10: ")

# first API call
url = BASE_URL + "?limit=" + str(num)

response = requests.get(url)

if response.status_code != 200:
    print("error: " + str(response.status_code))
data = response.json()

url=data["url"]
print(url)