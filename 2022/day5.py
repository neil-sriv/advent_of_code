from pathlib import Path
from collections import deque
from typing import Deque, List, Tuple

dir_path = Path(__file__).resolve().parent
with open(f"{dir_path}/day5_input.txt") as file:
    data = file.read().splitlines()


def read_stacks(data: List[str]) -> Tuple[List[Deque[str]], List[List[str]], int]:
    stacks = list()
    drawing = list()
    start = 0
    for idx, row in enumerate(data):
        if not row:
            start = idx
            break
        drawing.append([row[sub : sub + 3] for sub in range(0, len(row), 4)])
    stacks_num = len(drawing.pop())
    for idx in range(stacks_num):
        stacks.append(deque([row[idx][1:2] for row in drawing if row[idx] != "   "]))
    rows = [row.split(" ") for row in data[start + 1 :]]
    return stacks, rows, start


def move_stacks_9000(
    stacks: List[Deque[str]], rows: List[List[str]], start: int
) -> List[str]:
    for _, num, _, stack_1, _, stack_2 in rows:
        execute_move(int(num), int(stack_1) - 1, int(stack_2) - 1, stacks)

    return [stack.popleft() for stack in stacks]


def execute_move(
    num: int, stack_1: int, stack_2: int, stacks: List[Deque[str]]
) -> None:
    stacks[stack_2].extendleft(
        reversed([stacks[stack_1].popleft() for _ in range(num)])
    )


stacks, rows, start = read_stacks(data)

print(move_stacks_9000(stacks, rows, start))
