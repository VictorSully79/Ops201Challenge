#!/bin/bash

# Virus Scan
# Victor Sullivan
# 20211004
# Create a PowerShell script that Antivirus installed and scanning


Set-MpPreference -DisableRealtimeMonitoring 0
Get-MpComputerStatus