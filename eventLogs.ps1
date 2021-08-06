#!/bin/bash

# Event Logs
# Victor Sullivan   
# 20210805
# Create a PowerShell script that fetches useful System event logs.

# ******Sends out a file as JSON ******
# $now=Get-Date
# $startDate=$now.adddays(-1)
# $allEventsPath='C:\Users\victo\Desktop\24hrlog.json'


# $dayLog=get-eventlog -logname system -after $startDate | ConvertTo-Json

# $dayLog | out-file $allEventsPath

# ******Sends last 24hrs of System Logs to last_24.txt******
$now= Get-Date
$startDate=$now.adddays(-1)
$allEventsPath='C:\Users\victo\Desktop\last_24.txt'

$dayLog=get-eventlog -logname system -after $startDate | Export-Csv $allEventsPath

$dayLog

# ******Sends all error events to errors.txt******
$errorEventsPath='C:\Users\victo\Desktop\errors.txt'

$errorLog=get-eventlog -logname system -EntryType Error | Export-Csv $errorEventsPath

$errorLog

# ****** Prints to screen events with ID of 16 from System Log ******
$idSixteen=get-eventlog -LogName system -instanceID 16

$idSixteen

# ****** Prints most recent 20 from event log.******
$recentTwenty=get-eventlog -LogName System -newest 20

$recentTwenty

# ****** Prints most recent 500 without the ... ******
$recentFivehundred=get-eventlog -LogName System -newest 500 | Format-Table -Wrap

$recentFivehundred
