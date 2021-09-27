#!/bin/sh
#filerPermissions.sh    
#Victor Sullivan    
#Date of last revision 20210924
#Change file permissions by user group and other

#Main

read -p "Directory: " DIR
echo "Set $DIR as path"

read -p "Permissions: " PERM
echo "Set Permissions to $PERM"

cd $DIR
chmod -v -R $PERM $DIR

ls -l

#END