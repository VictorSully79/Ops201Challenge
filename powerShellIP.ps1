#!/bin/bash

# PowerShell IP Analysis
# Victor Sullivan
# 20210810
# Write a Powershell script that returns the IPv4 address of the computer.
# Use Select-String cmdlet to only return the IPv4 address string and no other extraneous information.


# ****File path variable for location of new file created/deleted.****
$path="C:\Users\victo\documents\ops201\Ops201Challenge\ipv4Report.txt"

# **** Creates the function to be called later ****
function ip4Log {
# **** Pulls all ipconfig data and creates/sends file to the specified path
    ipconfig /all | out-file -FilePath $path
# **** Goes into the file at the path variable and matches ipv4 and displays line containing it.****
    Select-String -path $path -Pattern ipv4 -SimpleMatch | Select-Object -first 1 | Write-Host
# **** Removes file from the path variable ****
    remove-item $path

}
# **** Calls the Function ****
ip4Log