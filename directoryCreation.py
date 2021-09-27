# directoryCreation
# Victor Sullivan
# 20210908
# Create a Python script that generates all directories, sub-directories and files for a user-provided directory path

# Import libraries
import os

# Variables
path=input("FilePath goes here: ")

# Functions
def dirreader():
    for (root, dirs, files) in os.walk(path):
        print(root)

        dirs[:] = [x for x in dirs if not x.startswith('.')]

        for dir in dirs:
            print(os.path.join(root, dir))
        
        files[:] = [x for x in files if not x.startswith('.')]

        for file in files:
            print(os.path.join(root, file))        

# Main
dirreader()

# End