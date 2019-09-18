import requests
import urllib.request
import time
from bs4 import BeautifulSoup

Arist = ""
page = "https://www.last.fm/music/" + Arist + "/+tracks?date_preset=ALL#top-tracks"
response = requests.get(page)
AristPage = BeautifulSoup(response.text, "html.parser")

songs = []
i = 0

for td in AristPage.findAll('td', {'class': 'chartlist-name'}):
	for a in td.findAll('a'):
		songs.append(str((a['title'])))

#textToSearch = 'hello world'
#query = urllib.parse.quote(textToSearch)
#url = "https://www.youtube.com/results?search_query=" + query
#response = urllib.request.urlopen(url)
#html = response.read()
#soup = BeautifulSoup(html, 'html.parser')
#for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    #print('https://www.youtube.com' + vid['href'])
