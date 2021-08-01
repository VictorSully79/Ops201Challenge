#!/bin/bash
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