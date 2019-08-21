import os
import shutil

#movefiles
path = "//192.168.1.2/Movies/data"
replacechars = ["[", "(", "]", ")", "_", ",", "-"]

directory = os.fsencode(path)

for file in os.listdir(directory):
    fileext = (os.path.splitext("/" + str(file, 'utf-8'))[1])
    filename = (os.path.splitext("/" + str(file, 'utf-8'))[0])

    newfilename = filename.replace(" ", ".")

    for char in replacechars:
        newfilename = newfilename.replace(char, "")

    print(newfilename)
    moviedir = path + newfilename
    try:
        os.mkdir(moviedir)

        os.rename(path + "/" + str(file, 'utf-8'), moviedir + "/" + newfilename + fileext)
        #shutil.move
    except OSError:
        print("Creation of the directory %s failed" + moviedir)
    else:
        print("Successfully created the directory %s " + moviedir)