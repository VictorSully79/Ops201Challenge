#! /bin/bash

# System Process Commands
# Victor Sullivan
# 20210806

# **** Just trying to figure out commands ****
# (Get-Counter '\Process(*)\% Processor Time').CounterSamples | Where-Object {$_.CookedValue -gt 0}

# ****Print to the terminal screen all active processes ordered by highest CPU time consumption at the top.****
get-process | Sort-Object -property CPU -Descending

# **** Print active processes ordered by highest Process Identification Number at the top****
get-process | Sort-Object -Property Id -Descending

# **** Print  to the terminal screen the top five active processes ordered by highest Working Set ****
get-process | Select-Object -First 5 | Sort-Object -Property WorkingSet -Descending 

# **** Start the process Internet Explorer (iexplore.exe) and have it open https://owasp.org/www-project-top-ten/. ****
start-process "C:\Program Files\Internet Explorer\iexplore.exe" "https://owasp.org/www-project-top-ten/"

# **** Start the process Internet Explorer (iexplore.exe) ten times using a for loop. Have each instance open https://owasp.org/www-project-top-ten/.****
for ( $num = 0; $num -lt 10; $num++ ) {
  if( $num -lt 10 ) {
    start-process "C:\Program Files\Internet Explorer\iexplore.exe" "https://owasp.org/www-project-top-ten/"
}
}

# **** Close all Internet Explorer windows. ****
Stop-Process -name iexplore

# **** Kill a process by its Process Identification Number. ****
Stop-Process -Id 3212