import os, fnmatch
import shutil

def find(pattern, path):
	result = []
	for root, dirs, files in os.walk(path):
		searchstring = "*"
		for word in pattern:
			searchstring = searchstring + word + "*"
		for name in files:
			print(name + " " + searchstring)
			if fnmatch.fnmatch(name.replace("'","").replace("(","").replace(")",""), "*" + searchstring + "*"):
				result.append(os.path.join(root, name))
	return result

basepath = "//192.168.1.2/Music/80/"
f = open(basepath + 'tracks.txt')
line = f.readline()
count = 0
while line:
	songdata = line.split(' - ')
	song = songdata[0].split('. ')
	if len(song) > 1:
		
		song = song[1].replace("'","").replace("(","").replace(")","").replace("\n", "")

		#if list containts a song and artist - array size 2 or greater
		if len(songdata) > 1:

			#track list contains artist and track name
			artist = songdata[1].replace("\n", "")
			if len(artist) < 3:
				artist = "Missing Artist"
			artistfolder = basepath + artist

		elif len(songdata) == 1:
			#in the event of no arist - array size of 1

			artist = "Missing Artist"
			artistfolder = basepath + artist
	
		songpath = find(song.split(" "), basepath)
	
		if len(songpath) > 0:	

			if not os.path.exists(artistfolder):
				os.mkdir(artistfolder)
			
			shutil.move(str(songpath[0]), artistfolder + "/" + str(os.path.basename(str(songpath)).replace("\\",""))[:-2])
	line = f.readline()
f.close()

