import os
import shutil
from pathlib import Path

def IsYear(s):
    try: 
        int(s)
        if int(s) > 1900:
            return True
        else:
            return False
    except ValueError:
        return False

#define path
path = "//192.168.1.2/Movies/"
directory = os.fsencode(path)
f= open("//192.168.1.2/Movies/data/removables.txt","r")
line = f.readline()
replacechars = ["[", "(", "]", ")", "_", ",", "-"]
removables = []
count = 0

#Check for removable words or phrases
while line:
    removables.append(line.split("'")[1])
    line = f.readline()

f.close()

#iterate thru files
for file in os.listdir(directory):
    fileext = (os.path.splitext("/" + str(file, 'utf-8'))[1])
    filename = (os.path.splitext("/" + str(file, 'utf-8'))[0])
    
    #Checks if Directory or File
    if not os.path.isdir(os.path.join(directory, file)):
        newfilename = filename.replace(" ", ".")

        for char in replacechars:
            newfilename = newfilename.replace(char, "")
    
        filenamewordlist = []
        filenamewordlist = newfilename.split(".")

        newfilename = ""

        #Iterate thru all words thru file in order to build correct filename
        for word in filenamewordlist:
            if word not in removables:
                if len(newfilename) == 0:
                    newfilename = word.replace("/","")
                elif IsYear(word) is True:
                    newfilename = newfilename + " (" + word + ")"
                    break
                else:
                    newfilename = newfilename + " " + word

        moviedir = path + newfilename
        try:
            os.mkdir(moviedir)
            os.rename(path + "/" + str(file, 'utf-8'), moviedir + "/" + newfilename + fileext)
            shutil.move
        except OSError:
            print("Creation of the directory %s failed" + moviedir)
        else:
            print("Successfully created the directory %s " + moviedir)
    else:
        #Renames Folder to remove periods
        newmoviefolder = ""

        moviefolder = str(file, 'utf-8')

        if moviefolder != "data":

            print(moviefolder)

            oldmoviefolder = moviefolder.replace("."," ")
            wordsinmoviefolder = []
            wordsinmoviefolder = oldmoviefolder.split(" ")
            wordcount = 0
            titlecontainsthe = False
            year = ""

            for word in wordsinmoviefolder:
                wordcount = wordcount + 1
                if word not in removables:
                    year = word.replace("(","").replace(")","").replace("'","")
                
                    if IsYear(year):
                        movieyear = "(" + year + ")"
                    elif (word == "The") or (word == "the"):
                        if wordcount < 2:
                            titlecontainsthe = True
                    else:
                            newmoviefolder = newmoviefolder + word.capitalize() + " "

            if titlecontainsthe == True:
                newmoviefolder = newmoviefolder[:-1] + ", The " #+ movieyear
            else:
                newmoviefolder = newmoviefolder #+ movieyear

            try:
                    os.rename(os.path.join(str(directory, 'utf-8'), str(file, 'utf-8')), os.path.join(str(directory, 'utf-8'), newmoviefolder))
            except OSError:
                print("Rename of the directory %s failed" + moviefolder)