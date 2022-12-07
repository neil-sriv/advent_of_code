from collections import deque
from pathlib import Path
from typing import Deque

dir_path = Path(__file__).resolve().parent
with open(f"{dir_path}/day6_input.txt") as file:
    data = file.read()


def find_first_marker_idx(data: str, unique_len: int) -> int:
    window = deque(data[:unique_len])
    idx = unique_len
    while idx < len(data):
        curr = data[idx]
        print(f"1: {window=}, {curr=}, {idx=}")
        if len(window) < unique_len:
            window.append(curr)
            idx += 1
            continue
        print(f"2: {window=}, {curr=}, {idx=}")
        if not _check_unique(window):
            while curr in window:
                window.popleft()
        print(f"3: {window=}, {curr=}, {idx=}")
        if len(window) == unique_len and _check_unique(window):
            return idx
        elif len(window) < unique_len:
            continue
        else:
            window.popleft()
    return -1


def _check_unique(window: Deque) -> bool:
    return len(set(window)) == len(window)


print(find_first_marker_idx(data, 4))
print(find_first_marker_idx(data, 14))
