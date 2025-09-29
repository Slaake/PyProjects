# Modules
import ctypes
import os
from dotenv import load_dotenv
import requests
from pathlib import Path

# Get Wallhaven API key from .env and loads it into session
dotenv_path = Path('./.env')
load_dotenv(dotenv_path)
key = (os.getenv('wallhavenAPI'))

# Construct URL with API Key to get wallpaper
baseurl = 'https://wallhaven.cc/api/v1/'
endpoint = '/5g22q5'
apikey = '?apikey=' + key
save_as = endpoint +'.jpg'
wallpaper_path = input("Enter where to save wallpapers: ")

# Check that the path provided is formated for the folder given
if wallpaper_path[-1] != '\\':
    wallpaper_path = wallpaper_path + '\\'
    print(wallpaper_path)
    image = wallpaper_path + save_as
else:
    image = wallpaper_path + '\\' + save_as

# Gets wallpaper given by user
def wallpaper_get():
    baseurl = baseurl + 'w'
    url = baseurl+endpoint+apikey
    wallpaper_request = requests.get(url)
    if wallpaper_request.status_code == 200:
        print('Success! Saving file...')
        walldata = wallpaper_request.json()
        img = walldata['data']['path']
        return img
    else:
        print("failed with " + wallpaper_request.status_code)

# Downloads image to location given
def download_image(url, save_as):
    response = requests.get(url)
    with open(wallpaper_path +save_as, 'wb') as file:
        file.write(response.content)

# Changes the wallpaper to the newly downloaded image
def change_wallpaper(image):
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDWININICHANGE = 0x02
    try:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
        return True
    except Exception as e:
        print(f'Failed to change wallpaper: {e}')
        return False

def wallpaper_search():
    url = baseurl+ 'search' + apikey
    wallpaper_request = requests.get(url)
    if wallpaper_request.status_code == 200:
        print('Success! Saving file...')
        walldata = wallpaper_request.json()
        img = walldata['data'][1]['path']
        return img
    else:
        print("failed with " + wallpaper_request.status_code)

# imgurl = wallpaper_get()
imgurl = wallpaper_search()
download_image(imgurl, save_as)
change_wallpaper(image)
