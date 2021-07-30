#! /bin/bash

# bashArrays
# Victor Sullivan 
# 20210729
# Iterated through array of directory's and add a file to them.

mkdir dir1 dir2 dir3 dir4

directoryArray=("dir1" "dir2" "dir3" "dir4")

for directory in "${directoryArray[@]}"
do
echo > ${directory}/new.txt
done

