from pathlib import Path

dir_path = Path(__file__).resolve().parent
with open(f"{dir_path}/day1_input.txt") as file:
	data = file.read().splitlines()

total = 0
for line in data:
    first, last = None, None
    for char in line:
        if char.isdigit():
            if first is None:
                first = char
            last = char
    total+=int(first+last)
print(total)
