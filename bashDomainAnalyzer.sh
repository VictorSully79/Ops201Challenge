#!/bin/bash

# Bash  Domain Analyzer
# Victor Sullivan
# 20210811
# Create a bash script that asks a user to type a domain, then displays information about the typed domain. Operations that must be used include:
# whois
# dig
# host
# nslookup

# **** Asks user a question and assigns "domain" as variable of answer ****
read -p "What domain would you like info on? " domain

domainInfo() {
    whois $domain
    dig $domain
    host $domain
    nslookup $domain.
# **** Exports and overwrites the file at the designated path ****
    } > /mnt/c/Users/victo/documents/ops201/Ops201Challenge/domain.txt

# **** Calls the Function ****
domainInfo

# **** delays 1second before opening VScode to read file ****
sleep 1
# **** Opens the file on the path with VScode ****
 Code . /mnt/c/Users/victo/documents/ops201/Ops201Challenge/domain.txt
