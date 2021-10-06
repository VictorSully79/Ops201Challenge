# pythonRequestLibrary.py
# Victor Sullivan
# 20210925
# Practice with Python Requests

import requests
import sys

url = input("Input your destination URL: ")
print("URL Destination is " + url)
list = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS']
print(list)
request = input("Please specify an HTTP Request Method: ")

if request == "GET":
    print('requests.get(url) response = requests.get(url)')
    resp = input('Continue? Y/N')
    if resp == 'Y':    
        requests.get(url)
        response = requests.get(url)
        if response.status_code == 200:
            print('Success!')
        elif response.status_code == 404:
            print('404 Not Found.')
    if resp == 'N':            
            print('Stopping Script')
            sys.exit(0)
    else:
        print('Invalid input. Exiting script.')
        sys.exit('Ah! An error!')
        

elif request == "POST":
    print('requests.post(url) response = requests.post(url)')
    resp = input('Continue? Y/N')
    if resp == 'Y''y':
        requests.post(url)
        response = requests.post(url)
        if response.status_code == 200:
            print('Success!')
        elif response.status_code == 404:
            print('404 Not Found.')
    elif resp == 'N''n':
            import sys
            print('Stopping Script')
            sys.exit(0)
    else:
        print('Invalid input. Exiting script.')
        sys.exit('Ah! An error!')


elif request == 'PUT':
    print('requests.put(url) response = requests.put(url)')
    resp = input('Continue? Y/N')
    if resp == 'Y':
        requests.put(url)
        response = requests.put(url)
        if response.status_code == 200:
            print('Success!')
        elif response.status_code == 404:
            print('404 Not Found.')
        elif response.status_code == 405:
            print('Method Not Allowed')
    if resp == 'N':
            import sys
            print('Stopping Script')
            sys.exit(0)
    else:
        print('Invalid input. Exiting script.')
        sys.exit('Ah! An error!')           