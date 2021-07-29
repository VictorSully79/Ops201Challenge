#! /bin/bash

# echo Hello World!

# name=Victor

# read -p "What is your name? " name
# echo "Hello, $name, what brings your here?"

whosBeenHere() {
  read -p "How far back would you like to go? " times
  
  echo "Here are the last $times visitors:"
  last -$times
}

whosBeenHere