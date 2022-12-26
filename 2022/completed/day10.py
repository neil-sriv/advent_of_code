from pathlib import Path
from collections import deque
from typing import Optional

dir_path = Path(__file__).resolve().parent
with open(f"{dir_path}/day10_input.txt") as file:
    data = file.read().splitlines()


def cycle(input: list[str]) -> list[int]:
    stack = deque()
    for line in input:
        if "noop" in line:
            stack.append(None)
        else:
            _, val = line.split(" ")
            stack.append(int(val))
    cycle, X = 0, 1
    cycles = list()
    while len(stack) > 0:
        register = stack.popleft() if stack else None
        if register:
            cycles.append(X)
            cycles.append(X)
            X += register
        else:
            cycles.append(X)
    return cycles


def calculate_signals(cycles: list[int]) -> list[tuple[int, int]]:
    return [
        (cycles[x], (x + 1) * cycles[x])
        for x in range(len(cycles))
        if x + 1 in {20, 60, 100, 140, 180, 220}
    ]


def draw_sprite(cycles: list[int]) -> None:
    for x in range(0, 240, 40):
        draw_line(cycles[x : x + 40])


def draw_line(cycles: list[int]) -> None:
    line = ""
    for i, idx in enumerate(cycles):
        if i in [idx-1, idx, idx+1]:
            line+='#'
        else:
            line+='.'
    print(line)

cycles = cycle(data)

signals = calculate_signals(cycles)
print(sum([y for x, y in signals]))

draw_sprite(cycles)
