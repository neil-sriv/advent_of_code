from pathlib import Path

dir_path = Path(__file__).resolve().parent
with open(f"{dir_path}/day_input.txt") as file:
	data = file.read().splitlines()


