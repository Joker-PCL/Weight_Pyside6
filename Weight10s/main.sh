#!/bin/bash

while true
do
    echo -e "<<< WEIGHT 10s' >>>\n"
    for i in {5..1}
    do
        echo -ne "Starting in $i seconds \r"
        sleep 1
    done

    echo -e "\n"
    
    cd /home/weight/Desktop/polipharm || exit
    source .env/bin/activate
    python3 main.py
done