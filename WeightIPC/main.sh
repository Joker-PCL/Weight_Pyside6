#!/bin/bash

while true
do
    echo -e "<<< WEIGHT IPC >>>"
    for i in {5..1}
    do
        echo -ne "Starting in $i seconds \r"
        sleep 1
    done

    echo -e "\n"
    
    cd /home/polipharm/Desktop/polipharm || exit
    source env/bin/activate
    python3 ./weightIPC/main.py
done