#! /bin/bash
networkInfo(){
echo Here is your network information:
sudo ifconfig
ifconfig > output.txt
}

networkInfo