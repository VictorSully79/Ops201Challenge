# psutil
# Victor Sullivan
# 20210915
# Use Psutil to fetch system information

# Script:                       Op Challenge 12
# Author:                       Courtney Hans
# Date of latest revision:      9/15/20
# Purpose:                      psutil in Python

# resource: https://programmer.group/use-of-psutil-library-in-python-operation-and-maintenance-development.html
# resource: https://www.kite.com/python/answers/how-to-write-a-variable-to-a-file-in-python

import psutil



# Declaration of variables




userNormal = repr(psutil.cpu_times().user)
kernelNormal = repr(psutil.cpu_times().system)
idle = repr(psutil.cpu_times().idle)
# ****Changed lines from .nice to .user to run on windows****
userPriority = repr(psutil.cpu_times().user)
completeIO = repr(psutil.cpu_times().user)
hardInterupt = repr(psutil.cpu_times().user)
softInterupt = repr(psutil.cpu_times().user)
virtualOS = repr(psutil.cpu_times().user)
virtualCPU = repr(psutil.cpu_times().user)

# Declaration of functions

# Main
print("Time spent by normal processes executing in user mode:", userNormal, "seconds")
print("Time spent by normal processes executing in kernel mode:", kernelNormal, "seconds")
print("Time when system was idle:", idle, "seconds")
print("Time spent by priority processes executing in user mode:", userPriority, "seconds")
print("Time spent waiting for I/O to complete:", completeIO, "seconds")
print("Time spent for servicing hardware interrupts:", hardInterupt, "seconds")
print("Time spent for servicing software interrupts:", softInterupt, "seconds")
print("Time spent by other operating systems running in a virtualized environment:", virtualOS, "seconds")
print("Time spent running a virtual CPU for guest OS under the control of the Linux kernal:", virtualCPU, "seconds")

myFile = open("psutilOuput.txt", "w+")
myFile.write("Time when system was idle: " + userNormal + " seconds \n")
myFile.write("Time spent by normal processes executing in kernel mode: " + kernelNormal+" seconds \n")
myFile.write("Time when system was idle: " + idle + " seconds \n")
myFile.write("Time spent by priority processes executing in user mode: " + userPriority + " seconds \n")
myFile.write("Time spent waiting for I/O to complete: " + completeIO + " seconds \n")
myFile.write("Time spent for servicing hardware interrupts: " + hardInterupt + " seconds \n")
myFile.write("Time spent for servicing software interrupts: " + softInterupt + " seconds \n")
myFile.write("Time spent by other operating systems running in a virtualized environment: " + virtualOS + " seconds \n")
myFile.write("Time spent running a virtual CPU for guest OS under the control of the Linux kernal: " + virtualCPU +
             " seconds \n")
myFile.close()
# End