# recursiveAddOn.py
# Victor Sullivan
# 20211012
# Script to Recursively Encrypt

# Importing Library
from cryptography.fernet import Fernet
import time, os

#Declare a variable

path = "./newFolder"
output = ""

#Declare Functions

def mode_entry():
    global output
print('''Options to select:
        (mode 1)Encrypt a file
        (mode 2)Decrypt a file
        ''')
        user_input=input("plese enter mode: ")

        if(user_input == "mode1"):
            encryptFile(file, key)
        elif(user_input == "mode2"):
            decryptFile(file, key)
        else:
            print("This is the end!")
            exit(0)
            
def getFiles(dirNames):
    completeFileList = list()
    for (dirPath, dirName, fileName) in os.walk(dirNames):
        completeFileList += [os.path.join(dirPath, file) for file in fileName]
    for fil in completeFileList:
        print(fil)
        
def encryptFile(file,key):
    f = Fernet(key)
    with open(file, "rb") as fileread:
        readfile = fileread.read()
    encryptFile = f.encrypt(readfile)
    with open(file, "wb") as filewrite:
        filewrite.write(encryptFile)
        time.sleep(2)
        print("file encrypted")
        
def decryptFile(file, key):
    f = Fernet(key)
    with open(file, "rb") as fileread:
        # read the encrypted data
        encrypted_data = fileread.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(file, "wb") as filewrite:
        filewrite.write(decrypted_data)
#Main
getFiles(path)
write_key()
# load the previously generated key
key = load_key()
while(1):
    mode_entry()


#End
