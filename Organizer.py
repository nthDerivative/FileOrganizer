# import the os module
import os

path = "//192.168.1.2/Movies"
replacechars = ["[", "(", "]", ")", "_", ",", "-"]
commonwordsarr = []
i = 0
directory = os.fsencode(path)

for file in os.listdir(directory):

    filename = (os.path.splitext(str(file, 'utf-8'))[0]).replace(" ", ".")
    for char in replacechars:
        filename = filename.replace(char, "")

    filebywords = filename.split('.')

    for words in filebywords:
        if any(words in sublist for sublist in commonwordsarr):
            x = [x for x in commonwordsarr if words in x][0]
            commonwordsarr[commonwordsarr.index(x)][0] = int(commonwordsarr[commonwordsarr.index(x)][0]) + 1
        else:
            commonwordsarr.append([1, words])

commonwordsarr.sort(reverse=True)

print(*commonwordsarr)