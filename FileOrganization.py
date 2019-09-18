import os
path = "//192.168w.1.2/Movies/"

for dirs in os.walk(path):
    if len(dirs[1]) > 0:
        print(str(dirs[1][0]))
        if str(dirs[1][0]).find("feat") < 0:
            "found"
            print(str(dirs[0]) + "/" + str(dirs[1][0]))
