#!/bin/bash

# Conditionals
# Victor Sullivan
# 20210802
# Create a Bash script that detects if a file or directory exists, then creates it if it does not exist.  Your script must use at least one list, one loop, and one conditional.

# Asks a question



read -p "Would you like to search for a file or directory? " fileOrDirectory

read -p "Please input the file or directory path. Directory paths need to end with a '/'. " path

# creates arbitrary log to meet list requirement + if you give it the wrong path you may need to find it. Happy Happy Happy
changeInfo=($fileOrDirectory, $path)
printf "%s\n" "${changeInfo[@]}" >> conditionalOutput.txt


if [ $fileOrDirectory == "file" ]
  then  
    echo "Firing up the hamster wheel to search for $path"
      fi

if [ -f $path ]
  then
    echo "Found it!"
      else
        echo > $path
        echo "It wasn't there so I made you a shiny new one!"
          fi
          

if [ $fileOrDirectory == "directory" ]
  then  
    echo "Ludicrous speed engaged! Destination $path"
      fi

if [ -d $path ]
  then
    echo "Here it is! "
      else
        mkdir $path 
        echo "It wasn't there so I made you a shiny new one!"
          fi



            