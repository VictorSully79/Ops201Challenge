#! /bin/bash
# menuSystems.sh
# Victor Sullivan
# 20210923
# Use conditionals in menu systems



list=("Hello World" "Ping Self" "IP Info" "Exit")

# Main
echo "Here are your options: "
select choice in "${list[@]}"
do 
    case $choice in
        "Hello World")
            echo "Hello World"
            ;;
        "Ping Self")
            ping -c 4 127.0.0.1
            ;;
        "IP Info")
            ip a
            ;;
        "Exit")
            break
            ;;
    esac
done

# End