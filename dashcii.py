import json
import requests
import random

# Enter search tags into this list:
search_tags = [
    "pokemon",
    "dragon",
    "bird",
    "outer space",
    "dolphins",
    "nature",
    "linux",
    "wolves"
]

# Max dimensions of ascii
dimensions = [30, 30]

def query_asciiur(search_term, page):
    payload = {'q': search_term, 'pg': page}
    response = requests.get("https://www.asciiur.com/api", params=payload)
    art_list = []
    if response.status_code == 200:
        for x in response.json():
            art_list.append(x['body'])
        return art_list
    else:
        raise Exception("API query failed!")
    return 0

def ascii_width_height(art):
    art_array = art.strip("\r").split("\n")
    y = len(art_array)
    x = 0
    for line in art_array:
        if len(line) > x:
            x = len(line)
    return x, y

def splash(tag_list):
    new_art_list = []
    while not new_art_list:
        try:
            art_list = query_asciiur(random.choice(tag_list), 1)
            for art in art_list:
                width, height = ascii_width_height(art)
                if width <= dimensions[0]:
                    if height <= dimensions[1]:
                        new_art_list.append(art)
        except:
            pass
    return random.choice(new_art_list)

print(splash(search_tags))
