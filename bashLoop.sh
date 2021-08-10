#!/bin/bash

# bashLoops
# Victor Sullivan
# 20210730
# Write a script that displays running processes, asks the user for a PID, then kills the process with that PID.

ps

pids=($(ps ax | awk '{print $1}'))

PS3="What process PID would you like to terminate? "
killOrder() {
  select PID in "${pids[@]}"
  do
    if  [ "$PID" == "quit" ]
      then
        break
        else kill -9 "$PID"
          break
  fi
  done
}
killOrder