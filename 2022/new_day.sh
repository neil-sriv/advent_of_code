#!/bin/bash

day=$1
url=https://adventofcode.com/2022/day/$day

# curl --ouput $day_input.txt $url
curl $url/input --cookie cookies.txt --output day${day}_input.txt 

echo -e "\nwith open(\"day${day}_input.txt\") as file:\n\tdata = file.read().splitlines()\n\n" > day$day.py

firefox -new-tab $url