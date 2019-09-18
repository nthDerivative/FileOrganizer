# import the os module
import os
import shutil

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

replacechars = ["[", "(", "]", ")", "_", ",", "-"]
commonwordsarr = []
i = 0
directory = os.fsencode(path)

#todo check if file exists
f= open("//192.168.1.2/Movies/data/results.txt","w+")
line = f.readline()
count = 0
while line:


#iterates thru directory
for file in os.listdir(directory):

    filename = (os.path.splitext(str(file, 'utf-8'))[0]).replace(" ", ".")
    for char in replacechars:
        filename = filename.replace(char, "")

    filebywords = filename.split('.')

    for words in filebywords:
        if any(words in sublist for sublist in commonwordsarr):
            x = [x for x in commonwordsarr if words in x][0]
            commonwordsarr[commonwordsarr.index(x)][0] = int(commonwordsarr[commonwordsarr.index(x)][0]) + 1
        elif  IsYear(words):
            print(words)
        else:
            commonwordsarr.append([1, words])

commonwordsarr.sort(reverse=True)

while i < len(commonwordsarr):
	f.write(str(commonwordsarr[i]) + "\n")
	i += 1

f.close


