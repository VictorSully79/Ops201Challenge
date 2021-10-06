# uptimeSensorTool.py
# Victor Sullivan
# 20211005
# Create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down.

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
import sys

from pythonping import ping


def twoSecondPing():
    pingStuff = ping('8.8.8.8', verbose=True, interval=2)
    print(pingStuff)


twoSecondPing()
