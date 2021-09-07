# systemInfo
# Victor Sullivan
# 20210907
# Get system information using Python script

# import module
# subprocesses allow interaction with the Operating System
import subprocess

# navigate through the requested info
Id = subprocess.check_output(['systemInfo']).decode('utf-8').split('\n')
new = []

# put the output in a readable format
for item in Id:
    new.append(str(item.split("\r")[:-1]))
for i in new:
    print(i[2:-2])

