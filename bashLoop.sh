#!/bin/bash

pids=($(ps ax | awk '{print $1}'))

PS3='Select a number or type quit: '


#select PID in ${pids[@]}
#do
 # if [$PID = "Quit" ]
  #then
   # break
  #fi
  #echo 
  #done