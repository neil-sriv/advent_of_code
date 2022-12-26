from pathlib import Path
from pprint import pprint
from collections import deque

dir_path = Path(__file__).resolve().parent
with open(f"{dir_path}/day12_input.txt") as file:
    data = file.read().splitlines()


def find_start_and_end(input: list[str]) -> tuple[tuple[int, int], tuple[int, int]]:
    start, end = (-1, -1), (-1, -1)
    for i, row in enumerate(input):
        for j, c in enumerate(row):
            if c == "S":
                start = (i, j)
            if c == "E":
                end = (i, j)
    return start, end


def find_all_starts(input: list[str]) -> list[tuple[int, int]]:
    starts = list()
    for i, row in enumerate(input):
        for j, c in enumerate(row):
            if c == "S" or c == "a":
                starts.append((i, j))
    return starts


def find_exits(
    input: list[list[str]], start: tuple[int, int], end: tuple[int, int]
) -> int:
    stack = deque([(start[0], start[1], 0)])
    small = None
    # pprint(input)
    while len(stack) > 0:
        i, j, num = stack.popleft()
        # print(i, j, num)
        # pprint(input)
        if small and num >= small:
            continue
        if input[i][j] == "E":
            if small is None or num < small:
                small = num
            continue
        if input[i][j] == "X":
            continue
        find_paths(i, j, num + 1, stack, input)
        # print(stack)
        input[i][j] = "X"
    # pprint(input)
    return small  # type: ignore


def find_paths(
    row: int,
    col: int,
    journey: int,
    stack: deque[tuple[int, int, int]],
    input: list[list[str]],
) -> None:
    curr = input[row][col]
    # print("adding...")

    def check_temp(row: int, col: int):
        temp = input[row][col]
        if curr == "S" and temp == "a":
            stack.append((row, col, journey))
        if temp == "E":
            temp = "z"
        if temp.isupper():
            return
        elif ord(temp) - ord(curr) <= 1:
            # print(row, col, temp, curr)
            stack.append((row, col, journey))

    if row > 0:
        check_temp(row - 1, col)
    if row < len(input) - 1:
        check_temp(row + 1, col)
    if col > 0:
        check_temp(row, col - 1)
    if col < len(input[0]) - 1:
        check_temp(row, col + 1)


def find_shortest_start(
    starts: list[tuple[int, int]], end: tuple[int, int], input: list[list[str]]
) -> list[int]:
    from copy import deepcopy

    exits = list()
    for start in starts:
        copied = deepcopy(input)
        exits.append(find_exits(copied, start, end))
    return sorted([exit for exit in exits if exit is not None])


start, end = find_start_and_end(data)
starts = find_all_starts(data)
data = [[c for c in line.strip()] for line in data]
# print(find_exits(data, start, end))
print(find_shortest_start(starts, end, data))
