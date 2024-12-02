#!/bin/zsh

day=$1
url=https://adventofcode.com/2024/day/$day

# curl --ouput $day_input.txt $url
curl $url/input --cookie session=53616c7465645f5f9fdbbaef6a6432beff24b4e6c2f5d16175845895c78fa6a1b0bde5311cafddbf35123201c13f83ebcaaac2e8a34a06b0b8689bbae3fd1ab6 --output day${day}_input.txt
curl $url --cookie session=53616c7465645f5f9fdbbaef6a6432beff24b4e6c2f5d16175845895c78fa6a1b0bde5311cafddbf35123201c13f83ebcaaac2e8a34a06b0b8689bbae3fd1ab6 | lynx -stdin -dump > day${day}_question.txt
python get_question.py $day
# echo -e "from pathlib import Path\n\ndir_path = Path(__file__).resolve().parent\nwith open(f\"{dir_path}/day${day}_input.txt\") as file:\n\tdata = file.read().splitlines()\n\n" > day$day.py
echo "\"\"\"\n" | cat - day${day}_question.txt > day$day.py
echo "\n\"\"\"\n" >> day$day.py
cat template.txt >> day$day.py

open -a Firefox -g $url
