
import os
import pandas as pd
from pathlib import Path


RAW_DATA_FOLDER = "data/raw"
CITY = "munich"
PROJECT_FOLDER = Path(__file__).parent.parent

# we shall store all the file names in this list
filelist = []
folder = (PROJECT_FOLDER / RAW_DATA_FOLDER / CITY).resolve()

for root, dirs, files in os.walk(PROJECT_FOLDER):
    for file in files:
        # append the file name to the list
        filelist.append(os.path.join(root, file))
        if file.find("gz") > 0:
            print(file)


# print all the file names
# for name in filelist:
#    print(name)
