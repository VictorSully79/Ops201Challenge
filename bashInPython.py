# bashInPython.py
# Victor Sullivan
# 20210923
# Manipulate bash with Python




import os

os.system("sudo bash lshw.sh")
print("This looks like good info to store.")

import time ; time.sleep(3)
os.system("sudo bash infotofile.sh")

import time ; time.sleep(3)
print("Use Control x to enter nano.")

import socket
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
print("Host Name: " + h_name)
print("This IP address is: " + IP_addres)

