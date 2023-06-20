import requests, os
from bs4 import BeautifulSoup
from googleapiclient.discovery import build

# ====== [YouTube API Testing] ======
# hidden YouTube API Key in OS Environment Vars
api_key = os.environ.get('api_key')
youtube = build('youtube', 'v3', developerKey=api_key)

# ====== [BeautifulSoup Scraping] ======
# URL will be our <input> from index.html
req = requests.get('https://www.youtube.com/playlist?list=PLyBc7mndZD4GDX23dhS1WxdzTCXPmOsqA')

# parsing the html
soup = BeautifulSoup(req.content, 'html.parser')
with open("playlist.html", "w", encoding = 'utf-8') as file:
    file.write(str(soup.prettify()))

# read the output file for "id="video-title""
# skip until "title="""
# artistName = "" until '-' or '/'
# songName until """>" 
# start over for next song 