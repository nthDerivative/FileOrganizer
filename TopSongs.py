import requests
import urllib.request
import time
from bs4 import BeautifulSoup


page = "https://www.last.fm/music/Audioslave/+tracks?date_preset=ALL#top-tracks"
response = requests.get(page)
AristPage = BeautifulSoup(response.text, "html.parser")

songs = []
i = 0

for td in AristPage.findAll('td', {'class': 'chartlist-name'}):
	for a in td.findAll('a'):
		songs.append(str((a['title'])))

print(songs)
print(len(songs))