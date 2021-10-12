# fileEncryptionPt1.py
# Victor Sullivan
# 20211011
# Script to Encrypt File


from cryptography.fernet import Fernet
import time
# Declare Variable
file = "meOh.txt"
output = ""
# Declare functions
# function to load interface
def interface():
    global output
    print("""
    Please select a mode.
    1) Encrypt a file (mode 1)
    2) Decrypt a file (mode 2)
    3) Encrypt a message (mode 3)
    4) Decrypt a message (mode 4)
    5) exit
    """)
    userInput = input("option ? ")
    if(userInput == "1"):
        encryptFile()
        ## Encrypt file here
        print("")
    elif(userInput == "2"):
        decryptFile()
        ## Encrypt file here
        print("")
    elif (userInput == "3"):
        output = encryptMessage()
        ## Encrypt file here
        print("")
    elif (userInput == "4"):
        decryptMessage(output)
        ## Encrypt file here
        print("")
    elif (userInput == "5"):
        ## Encrypt file here
        print("Thank you using this application")
        exit(0)
    else:
        print("put right input here")
        interface()
def encryptFile():
    f = Fernet(key)
    with open(file, "rb") as fileread:
        readfile = fileread.read()
    encryptFile = f.encrypt(readfile)
    with open(file, "wb") as filewrite:
        filewrite.write(encryptFile)
        time.sleep(2)
        print("file has been encrypted")
def decryptFile():
    f = Fernet(key)
    with open(file, "rb") as fileread:
        # read the encrypted data
        encrypted_data = fileread.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(file, "wb") as filewrite:
        filewrite.write(decrypted_data)
def generateKey():
    key = Fernet.generate_key()
    with open("demo.key", "wb") as key_file:
        key_file.write(key)
def loadKey():
    return open("demo.key", "rb").read()
# Encrypt a message (mode 3)
def encryptMessage():
    f = Fernet(key)
    userMessage = input ("Enter your message to encrypt.").encode()
    encryptedMessage = f.encrypt(userMessage)
    print (encryptedMessage)
    return encryptedMessage
def decryptMessage(msg):
    f = Fernet(key)
    decryptMsg = f.decrypt(msg)
    print (decryptMsg)
# main
generateKey()
key = loadKey()
while (True):
    interface()
# End