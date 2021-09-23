#!/bin/sh
#Script Name - appendDateandTime.bash
#Author - Victor Sullivan
#Date of last revision - 20210920
#Description of purpose - Copy system log files to the PWD and appends current date and time. 
#Main

cp -v /var/log/syslog "$PWD/syslog-$(date +"%Y-%m-%d-%H:%M:%S")"

#End