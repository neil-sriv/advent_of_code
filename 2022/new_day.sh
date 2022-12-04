#!/bin/bash

day=$1
url=https://adventofcode.com/2022/day/$day

# curl --ouput $day_input.txt $url
curl $url/input --cookie cookies.txt --output day${day}_input.txt 

echo -e "from pathlib import Path\n\ndir_path = Path(__file__).resolve().parent\nwith open(f\"{dir_path}/day${day}_input.txt\") as file:\n\tdata = file.read().splitlines()\n\n" > day$day.py

firefox -new-tab $url