# Modules
import os
from dotenv import load_dotenv
import requests
from pathlib import Path

# Get Wallhaven API key from .env and loads it into session
dotenv_path = Path('./.env')
load_dotenv(dotenv_path)
key = (os.getenv('wallhavenAPI'))

# Construct URL with API Key to get wallpaper
baseurl = 'https://wallhaven.cc/api/v1/w/'
endpoint = '218wwx'
apikey = '?apikey=' + key
url = baseurl+endpoint+apikey
save_as = endpoint+'.jpg'
wallpaper_path = input("Enter where to save wallpapers: ")

def wallpaper_get():
    wallpaper_request = requests.get(url)
    if wallpaper_request.status_code == 200:
        print('Success! Saving file...')
        walldata = wallpaper_request.json()
        img = walldata['data']['path']
        return img
    else:
        print("failed with " + wallpaper_request.status_code)

def download_image(url, save_as):
    response = requests.get(url)
    with open(wallpaper_path +save_as, 'wb') as file:
        file.write(response.content)

imgurl = wallpaper_get()
download_image(imgurl, save_as)