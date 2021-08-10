#! /bin/bash

# Automated Endpoint
# Victor Sullivan   
# 20210809
# Write a Powershell script that automates the configuration of a new Windows 10 endpoint. 



    Set-NetFirewallRule -DisplayGroup "File And Printer Sharing" -Enabled True

    netsh advfirewall firewall add rule name="Allow incoming ping requests IPv4" dir=in action=allow protocol=icmpv4

    reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

    Disable-WindowsOptionalFeature -Online -FeatureName smb1protocol

    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://git.io/debloat'))

    


