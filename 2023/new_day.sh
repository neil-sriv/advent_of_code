#!/bin/zsh

day=$1
url=https://adventofcode.com/2023/day/$day

# curl --ouput $day_input.txt $url
curl $url/input --cookie session=53616c7465645f5f8596b60abec4a35d4f4361fcb20077c57633bd50392f363364432fca471531fb26ca79f1e8a5d6a95cc0354700788d12f4dd792327bcf060 --output day${day}_input.txt

echo -e "from pathlib import Path\n\ndir_path = Path(__file__).resolve().parent\nwith open(f\"{dir_path}/day${day}_input.txt\") as file:\n\tdata = file.read().splitlines()\n\n" > day$day.py

open -a Firefox -g $url
