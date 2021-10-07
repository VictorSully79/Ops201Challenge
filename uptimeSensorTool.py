#!bin
#
# uptimeSensorTool.py
# Victor Sullivan
# 20211005
# Create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.
#
# import platform
# import subprocess
#
# host = 'google.com'
#
#
# def uptimeSensor():
#     pingP = '-n' if platform.system().lower() == 'windows' else '-c'
#     command = ['ping', pingP, '1', host]
#     return subprocess.call(command) == 0
#
#
# uptimeSensor()
# import sys

# import itertools
# import subprocess
# from threading import Event
# from datetime import datetime
# from datetime import timedelta
# from pythonping import ping
# from pythonping.executor import Response
# pingStuff = "ping -n 1 " + destination
# timeNow = datetime.now()
# timeStamp = timeNow.strftime("%d/%m/%Y %H:%M:%S")
# pingStamp = (pingStuff, timeStamp)
# def pingMcpingping():
#     destination = "8.8.8.8"
#     result = os.system("ping -c 1 " + destination)
#     if result==0:
#         pingstatus = "Successful Ping"
#     else:
#         pingstatus = "Nobody appears to be answering"
#     return pingstatus


# **** I left the above comments in to reference many things that did not work ****
# **** Finished with help from Josh classmate seattle-ops-cybersecurity-401d3 ****
import os
import time
import smtplib
from time import gmtime, strftime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Variables
ip=input("Enter IP Address:")
sender_address='victorsullivan@hotmail..com'
sender_pass='xxxxxxxxxx' #password
receiver_address='victorsullivan@hotmail.com'
server_status=1

while True:
    time.sleep(2)
    ping=os.system("ping -c 1 " + ip + "> /dev/null") 
    current_time=strftime("%x %X", gmtime())
    message=MIMEMultipart()
    message['From']=sender_address
    message['To']=receiver_address
    message['Subject']='A Server Has Changed Status'

    # print server status
    if ping == 0:
        print (ip + " is AVAILABLE " + current_time)
    else:
        print(ip + " is UNAVAILABLE " + current_time)

    if ping != server_status:
        if ping == 0:
            mail_contentup=(ip + " is now AVAILABLE " + current_time) #email message
            message.attach(MIMEText(mail_contentup, 'plain')) # add variable
            session = smtplib.SMTP('smtp.hotmail.com', 587) # port for mail
            session.starttls() # enable security
            session.login(sender_address, sender_pass) # login with mail_id and password
            text = message.as_string() # string to variable
            session.sendmail(sender_address, receiver_address, text) # send mail
            session.quit()
        else:
            mail_contentdown=(ip + " is now UNAVAILABLE " + current_time) 
            message.attach(MIMEText(mail_contentdown, 'plain')) 
            session = smtplib.SMTP('smtp.gmail.com', 587) 
            session.starttls() 
            session.login(sender_address, sender_pass) 
            text = message.as_string() 
            session.sendmail(sender_address, receiver_address, text) 
            session.quit()
    server_status=ping # change variable to new server status
